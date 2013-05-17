#!/usr/bin/env python
from OSC import OSCClient, OSCServer, OSCMessage

x32address = ('192.168.1.200', 10023)
client = OSCClient()
#server = OSCServer()

client.connect((x32address))

msg = OSCMessage('/ch/01/mix/on')
msg.append(0)
client.send(msg)
