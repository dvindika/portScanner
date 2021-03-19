#!/usr/bin/env python
import socket
import subprocess
import sys
from datetime import datetime

# Clear screen
subprocess.call('clear', shell=True)

# get input, hostname, start port and end port.
remoteServer = input("Enter a remote host to scan: ")
remoteServerStartPort = input("Enter start port: ")
remoteServerEndPort = input("Enter end port: ")


remoteServerIP  = socket.gethostbyname(remoteServer)


# print banner
print("-" * 55)
print("Please wait, Started scanning of host:  ", remoteServerIP)
print("-" * 55)

# scan start time
t1 = datetime.now()

#try, catch block with socket creation and close. Ports are converted to int
try:
    for port in range(int(remoteServerStartPort), int(remoteServerEndPort)):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(2)
        result = sock.connect_ex((remoteServerIP, port))
        if result == 0:
            print("Port {}: 	 Open".format(port))
        sock.close()

except KeyboardInterrupt:
    print("You stopped scan!")
    sys.exit()

except socket.gaierror:
    print("Hostname could not be resolved. Bye Bye")
    sys.exit()

except socket.error:
    print("Couldn't connect to server")
    sys.exit()

except socket.timeout:
    print("Socket timeout. Oooops")

# End time
t2 = datetime.now()

# Execution time
total =  t2 - t1

# Printing the information to screen
print("Scanning Completed in: {}".format(total))

#THE END
