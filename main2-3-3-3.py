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

# 2.2.4

# Create your objects here.
ev3 = EV3Brick()
left_motor = Motor(Port.B)
right_motor = Motor(Port.C)
speed = 150

robot = DriveBase(left_motor, right_motor, wheel_diameter=60, axle_track=105)

TSensor = TouchSensor(Port.S1)
UltraSensor = UltrasonicSensor(Port.S4)
CSensor = ColorSensor(Port.S3)

working = True

count = 0
# while True:
# robot.straight(20000)

while working:
    # left_motor.run(360)
    # right_motor.run(360)
    ev3.screen.clear()
    ev3.screen.print("Color: " + str(CSensor.color()))

    detected_color = CSensor.color()


    if detected_color == Color.RED:
        # note = color_sounds["red"]
        ev3.speaker.play_notes(["C4/4"])

    if detected_color == Color.GREEN:
        ev3.speaker.play_notes(["D4/4"])

    if detected_color == Color.BLUE:
        ev3.speaker.play_notes(["E4/4"])

    if detected_color == Color.YELLOW:
        ev3.speaker.play_notes(["F4/4"])


# robot.straight(1000)
# robot.stop()
# time.sleep(2)
# ev3.speaker.beep()
# robot.straight(-1000)
# time.sleep(2)




# Write your program here.
# ev3.speaker.beep()

# ev3.screen.print("Hello World!")
# wait(2000)
