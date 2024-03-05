#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
from umqtt.robust import MQTTClient
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

MQTT_ClientID = 'mybot'
MQTT_Broker = '192.168.8.215'
MQTT_Topic_Status = 'Lego/Status'
client = MQTTClient(MQTT_ClientID, MQTT_Broker, 1883)

working = True

count = 0
# while True:
# robot.straight(20000)

def listen(topic,msg):
    if topic == MQTT_Topic_Status.encode():
        ev3.screen.print(str(msg.decode()))

# listen

while True:
    client.connect()
    time.sleep(1)
    client.publish(MQTT_Topic_Status, 'Started')
    ev3.screen.clear()
    ev3.screen.print('Started')
    ev3.screen.set_callback(listen)
    client.subscribe(MQTT_Topic_Status)
    time.sleep(1)
    client.publish(MQTT_Topic_Status, 'Hello World')
    ev3.screen.print('Hello World')

# while working:
#     left_motor.run(360)
#     right_motor.run(360)
#     if UltraSensor.distance() < 300:
#         left_motor.stop()
#         right_motor.stop()
#         client.publish(MQTT_Topic_Status, 'I just stopped!')
#         client.check_msg()
#         time.sleep(1)


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
