# Lighting LEDs with Ultrasonic Sensor and Raspberry Pi
This project will allow you to measure the distance between your ultrasonic sensor and closest object in its range.
Then light a number of leds accordingly displaying a _visual feast_.

## Getting Started

### Requirements
- Raspberry Pi
- Breadboard
- 5 LEDs
- Jumper wires
- HC SR04 Ultrasonic Sensor
- 7 Resistors
- Raspbian (Python should be installed)

### Setting up the environment
  how to set up the environment

### Installing
  raspbian + python + terminal use (or ide, thonny)
  
### Code
For this project, the necessary modules are:
```python
import RPi.GPIO as GPIO
import time
```
RPi.GPIO is a module to control Raspberry Pi GPIO channels.
Meaning we can send signals (voltage) to the pins which will later turn the leds on.

Time module is being imported to get the instant time data to calculate the distance.
.
.
.
