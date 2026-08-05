# Owon SPE, SPM, and P4000 series PSU Python control library
This library works with the Owon SPE6103, SPE3103, SPM series, and P4000 series (P4603 and P4305) power supplies.
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

## SPM series multimeter

SPM models expose their built-in multimeter through the same connection. All
of its measurement functions are supported: AC/DC voltage, AC/DC current,
resistance, capacitance, diode, and continuity.

```python
with OwonPSU("/dev/ttyUSB0") as opsu:
  opsu.set_multimeter_function("VOLT:DC")
  print("Function:", opsu.get_multimeter_function())
  print("Measurement:", opsu.measure_multimeter())
```

Supported functions are `VOLT:DC`, `VOLT:AC`, `CURR:DC`, `CURR:AC`, `RES`,
`CAP`, `DIOD`, and `CONT`. Open or overloaded inputs return `inf`.

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
