# Owon SPE and P4000 series PSU python control library
This library works with the Owon SPE6103, SPE3103, and P4000 series (P4603 and P4305) power supplies.
Kiprim devices "DC310S" and "DC605S" are also supported.

## Installation
The easiest way to install is straight from [the pypi project](https://pypi.org/project/owon-psu/) using pip:
```
pip install owon-psu
```

## Example Usage with context manager
```python
from owon_psu import OwonPSU

with OwonPSU("/dev/ttyUSB0") as opsu:
  print("Identity:", opsu.read_identity())
  print("Measured Voltage:", opsu.measure_voltage())
  print("Measured Current:", opsu.measure_current())

  print("Set Voltage:", opsu.get_voltage())
  print("Set Current:", opsu.get_current())

  print("Set Voltage Limit:", opsu.get_voltage_limit())
  print("Set Current Limit:", opsu.get_current_limit())

  opsu.set_voltage(20)
  opsu.set_current(2)
  opsu.set_voltage_limit(30)
  opsu.set_current_limit(3)

  print("Output enabled:", opsu.get_output())
  opsu.set_output(True)
```

## Example Usage without context manager
```python
from owon_psu import OwonPSU

opsu = OwonPSU("/dev/ttyUSB0")
opsu.open()
print("Identity:", opsu.read_identity())
print("Voltage:", opsu.measure_voltage())
print("Current:", opsu.measure_current())

print("Set Voltage:", opsu.get_voltage())
print("Set Current:", opsu.get_current())

print("Set Voltage Limit:", opsu.get_voltage_limit())
print("Set Current Limit:", opsu.get_current_limit())

opsu.set_voltage(20)
opsu.set_current(2)
opsu.set_voltage_limit(30)
opsu.set_current_limit(3)
print("Output enabled:", opsu.get_output())
opsu.set_output(True)
opsu.close()
```
