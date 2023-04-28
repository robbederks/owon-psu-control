#!/usr/bin/env python3

__version__ = '0.0.1'
__author__ = 'Robbe Derks'

import serial

class OwonPSU:

  SUPPORTED_DEVICES = {"OWON,SPE", "KIPRIM,DC"}

  def __init__(self, port, default_timeout=0.5):
    self.ser = None
    self.port = port
    self.timeout = default_timeout

  def open(self):
    self.ser = serial.Serial(self.port, 115200, timeout=self.timeout)
    identity = self.read_identity()
    if not any([s in identity for s in self.SUPPORTED_DEVICES]):
      self.close()
      raise Exception("Not connected to a supported PSU!")

  def close(self):
    self.ser.close()

  def __enter__(self):
    self.open()
    return self

  def __exit__(self, *args, **kwargs):
    self.close()

  def _cmd(self, command, accept_silent=False, timeout=None):
    if self.ser == None:
      raise Exception("Connection is not open!")
    self.ser.write(bytes(command, 'utf-8') + b"\n")
    self.ser.timeout = timeout if timeout is not None else self.timeout
    ret = self.ser.readline().decode('utf-8')
    if not ret.endswith("\r\n") and not accept_silent:
      raise Exception(f"No response for command: '{command}'!")
    return ret[:-2]

  def _silent_cmd(self, command, timeout=0.01):
    if self._cmd(command, accept_silent=True, timeout=timeout) == "ERR":
      raise Exception(f"Error while executing command: '{command}'")

  def read_identity(self):
    return self._cmd("*IDN?")

  def measure_voltage(self):
    return float(self._cmd("MEASure:VOLTage?"))

  def measure_current(self):
    return float(self._cmd("MEASure:CURRent?"))

  def set_voltage(self, voltage):
    return self._silent_cmd(f"VOLTage {voltage:.3f}")

  def set_current(self, current):
    return self._silent_cmd(f"CURRent {current:.3f}")

  def set_voltage_limit(self, voltage):
    return self._silent_cmd(f"VOLTage:LIMit {voltage:.3f}")

  def set_current_limit(self, current):
    return self._silent_cmd(f"CURRent:LIMit {current:.3f}")

  def get_output(self):
    ret = self._cmd(f"OUTPut?")
    if ret not in ["ON", "OFF"]:
      raise Exception(f"Unknown return for get output command: {ret}")
    return ret == "ON"

  def set_output(self, enabled):
    self._silent_cmd(f"OUTPut {'ON' if enabled else 'OFF'}")

if __name__ == "__main__":
  import sys
  port_name = sys.argv[1]

  # Use with context manager
  with OwonPSU(port_name) as opsu:
    print("Identity:", opsu.read_identity())
    print("Voltage:", opsu.measure_voltage())
    print("Current:", opsu.measure_current())
    opsu.set_voltage(20)
    opsu.set_current(2)
    opsu.set_voltage_limit(30)
    opsu.set_current_limit(3)
    print("Output enabled:", opsu.get_output())
    opsu.set_output(False)

  # Use without context manager
  opsu = OwonPSU(port_name)
  opsu.open()
  print("Identity:", opsu.read_identity())
  opsu.close()
