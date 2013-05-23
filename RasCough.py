#!/usr/bin/env python

# this requires the RPi.GPIO and pyOSC libraries

from time import sleep
import threading
import RPi.GPIO as GPIO
from OSC import OSCClient, OSCServer, OSCMessage

# declare the GPIO pins we're using
LED1 = 2
LED2 = 3
button1 = 4
button2 = 22

# variables for the previous button inputs
previousInput1 = False
previousInput2 = False

# set up the GPIO
GPIO.setmote(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(LED1, GPIO.OUT)
GPIO.setup(LED2, GPIO.OUT)
GPIO.setup(button1, GPIO.IN)
GPIO.setup(button2, GPIO.IN)
# turning on the LEDs is like this:  GPIO.output(LED1, True)

# set up the OSC client (for sending) and server (for receiving)
x32address = ('192.168.1.200', 10023)
client = OSCClient()
client.connect((x32address))
# not sure about these next three lines, check the syntax
server = OSCServer(('localhost', 10023)
server.timeout = 0
run = True

# define the OSC addresses for the channels that we'll be controlling
pulpit = '/ch/01/mix/on'
lapel = '/ch/02/mix/on'

# add the message handlers for the channels we're controlling
server.addMsgHandler(pulpit, muteHandler1)
server.addMsgHandler(lapel, muteHandler2)

'''
#  check out this example of a threading OSC server https://code.google.com/p/osc-midi-bridge/wiki/OSC
# start the OSC server to receive messages from the X32
threadingServer = threading.Thread(target=server.serve_forever)
threadingServer.start()
'''

'''
# an infinite loop that checks if the button is pressed and if so toggles the mute channel
while True:
 input1 = GPIO.input(button1)
 if ((not previousInput1) and input1):
  #send an OSC message here to toggle the mute
  previousInput1 = input1
'''

'''
# sending an OSC mute
msg = OSCMessage('/ch/01/mix/on')
msg.append(0)
client.send(msg)
'''

# shut everything down
server.close()
threadingServer.join()
GPIO.cleanup()
