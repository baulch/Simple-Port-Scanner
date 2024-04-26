#!/bin/python3
'''
Title: Simple port scanner
Author: Tybau/Tom
Date: 26/04/2024
Description: Used to scan open ports on a system, created for educational purposes only
'''

import sys
import socket
from datetime import datetime as dt

#Define our target
if len(sys.argv) == 2:
        target = socket.gethostbyname(sys.argv[1]) # Translate hostname to IPV4
else:
        print("Invalid amount of arguments")
        print("Syntax: python3 ps.py <ip>")

#Adding a banner
print("-" * 50)
print(f'scanning target: {target}')
print(f'Time started: {str(dt.now())}')
try:
        for port in range(50, 85): #ports in range of 50 to 85
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #a variable s to gather ipv4 and port
                socket.setdefaulttimeout(1)
                result = s.connect_ex((target,port)) # a tuple, target and port. s.connect_ex is an error indicator, i.e. returns 0 if open or 1 if closed
                if result == 0:
                        print(f'port: {port} is open')
                s.close()
except KeyboardInterrupt:
        print('\nExiting Program.')
        sys.exit()
except socket.gaierror:
        print('Hostname could not be resolved')
        sys.exit()
except socket.error:
        print('could not connect ot server')
        sys.exit()
