#!/usr/bin/env python
# coding = utf-8

import sys,os
import socket
import sendmail

path = sys.path[0]
#print(path)
localIP = socket.gethostbyname(socket.gethostname())

filename = path+"/latestip.txt"

# if file does not exist, create it!
if not os.path.exists(filename):
	open(filename,'a').close()

#read ip address
with open(filename,'r') as f:
	latestip = f.read()

if localIP != latestip:
	with open(filename,'w') as f:
		f.write(localIP)
	sendmail.sendMail("Newest IP: {0}".format(localIP), "Pi IP changed")
