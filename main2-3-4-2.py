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
    # robot.straight(1000)
    # time.sleep(1)

    if(len(ev3.buttons.pressed()) and ev3.buttons.pressed()[0] == Button.CENTER):
        ev3.light.on(Color.RED)
        continue
        # robot.stop()
    else:
        ev3.light.on(Color.GREEN)
        continue


    # detected_color = CSensor.color()
    # left_motor.run(150)
    # right_motor.run(150)

    # ev3.screen.clear()
    # ev3.screen.print("Number: " + str(detected_color))

    # if detected_color != Color.BLACK:
    #     # note = color_sounds["red"]
    #     count +=1



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
