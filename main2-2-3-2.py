#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
import time


# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.

# 2.2.3.2

# Create your objects here.
ev3 = EV3Brick()
left_motor = Motor(Port.B)
right_motor = Motor(Port.C)

left_motor.run(300)
right_motor.run(200)
time.sleep(2.5)
left_motor.run(50)
time.sleep(3.5)
left_motor.run(200)
right_motor.run(300)
time.sleep(2.5)
left_motor.run(50)
time.sleep(1.5)
left_motor.run(300)
right_motor.run(300)
time.sleep(3)
right_motor.run(50)
time.sleep(2.2)
left_motor.run(300)
right_motor.run(300)
time.sleep(2)
right_motor.run(50)
time.sleep(2.2)
left_motor.run(300)
right_motor.run(300)
time.sleep(1)

# time.sleep(1.3)




# Write your program here.
ev3.speaker.beep()

# ev3.screen.print("Hello World!")
# wait(2000)
