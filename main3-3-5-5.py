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


color_to_binary = {
    "BLACK": '00000',
    "WHITE": '00001',
    "RED": '00010',
    "YELLOW": '00011',
    "GREEN": '00100',
    "BLUE": '00101'
}



robot = DriveBase(left_motor, right_motor, wheel_diameter=60, axle_track=105)

TSensor = TouchSensor(Port.S1)
UltraSensor = UltrasonicSensor(Port.S4)
CSensor = ColorSensor(Port.S3)

MQTT_ClientID = 'mybot'
MQTT_Broker = '172.20.10.3'
MQTT_Topic_Status = 'Lego/Status'

def mqtt_callback(topic, msg):
    # Convert the message to a string and display it on the EV3 screen
    decodedText = 'None'
    ev3.screen.clear()
    ev3.screen.print("{}".format(msg.decode()))
    wholeList = msg.decode().split(',')
    for color_str in wholeList:
        color_name = color_str.split('.')[-1]
        if color_name == "BLACK":
            continue
        binary = color_to_binary[color_name]
        decimal = int(binary, 2)
        ascii_char = chr(decimal)
        decodedText += ascii_char

    print(decodedText)


client = MQTTClient(MQTT_ClientID, MQTT_Broker, 1883)

working = True

text = 'Hello, World.'

colorsDetected = []

numberOfLoops = 0

count = 0
# while True:
# robot.straight(20000)

# listen
client.set_callback(mqtt_callback)
while working:
    numberOfLoops = numberOfLoops + 1
    detected_color = CSensor.color()
    client.connect()
    client.publish(MQTT_Topic_Status, 'Started')
    colorsDetected.append(str(detected_color))
    time.sleep(0.5)

    if numberOfLoops == 10:
        client.subscribe(MQTT_Topic_Status)
        time.sleep(1)
        chaine = ",".join(colorsDetected)
        client.publish(MQTT_Topic_Status, chaine)
    client.wait_msg()
    client.check_msg()
    if numberOfLoops >= 10:
        working = False
    # ev3.screen.set_callback(listen)
    # if topic == MQTT_Topic_Status.encode():
    #     ev3.screen.print(str(msg.decode()))
    # ev3.screen.print('Hello World')

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
