#
# Tello Python3 Control Demo
#
# http://www.ryzerobotics.com/
#
# 1/1/2018

import threading
import socket
import sys
import time



host = ''
port = 9000
locaddr = (host,port)


# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

tello_address = ('192.168.10.1', 8889)

sock.bind(locaddr)

def recv():
    count = 0

    while True:
        try:
            data, server = sock.recvfrom(1518)
            n = time.time()
            print ('n = ', n)
            print(data.decode(encoding="utf-8"))
        except Exception:
            print ('\nExit . . .\n')
            break

def fly_poly(sides):
    for s in range(sides):
        msg_f = "forward 150".encode(encoding="utf-8")
        sent = sock.sendto(msg_f, tello_address)
        time.sleep (5)
        #tello.Tello.rotate(round(360 / sides))
        rotate = (round (360/sides))
        msg_f = "ccw 120".encode(encoding="utf-8")
        sent = sock.sendto(msg_f, tello_address)
        time.sleep(5)

print ('\r\n\r\nTello Python3 Demo.\r\n')

print ('Tello: command takeoff land flip forward back left right \r\n       up down cw ccw speed speed?\r\n')

print ('end -- quit demo.\r\n')


#recvThread create
recvThread = threading.Thread(target=recv)
recvThread.start()

##t = time.time()
##msg_c = "command"
##sent = 0
##print ('Start ', t, '|', msg_c, '|', sent)
##msg_c = msg_c.encode(encoding="utf-8")
##sent = sock.sendto(msg_c, tello_address)
##print ('Start ', t, '|', msg_c, '|', sent)
##
##t = time.time()
##msg_b = "battery?"
##sent = 0
##print ('Start ', t, '|', msg_b, '|', sent)
##msg_b = msg_b.encode(encoding="utf-8")
##sent = sock.sendto(msg_b, tello_address)
##print ('Start ', t, '|', msg_b, '|', sent)
##time.sleep(1)
##
##t = time.time()
##msg_to = "takeoff"
##sent = 0
##print ('Start ', t, '|', msg_to, '|', sent)
##msg_to = msg_to.encode(encoding="utf-8")
##sent = sock.sendto(msg_to, tello_address)
##print ('Start ', t, '|', msg_to, '|', sent)
##time.sleep(5)
##
##t = time.time()
##msg_f = "forward 50"
##sent = 0
##print ('Start ', t, '|', msg_f, '|', sent)
##msg_f = msg_f.encode(encoding="utf-8")
##sent = sock.sendto(msg_f, tello_address)
##print ('Start ', t, '|', msg_f, '|', sent)
##time.sleep(5)
##
##t = time.time()
##msg_b = "back 50"
##sent = 0
##print ('Start ', t, '|', msg_b, '|', sent)
##msg_b = msg_b.encode(encoding="utf-8")
##sent = sock.sendto(msg_b, tello_address)
##print ('Start ', t, '|', msg_b, '|', sent)
##time.sleep(5)
##
##t = time.time()
##msg_l = "land"
##sent = 0
##print ('Start ', t, '|', msg_l, '|', sent)
##msg_l = msg_l.encode(encoding="utf-8")
##sent = sock.sendto(msg_l, tello_address)
##print ('Start ', t, '|', msg_l, '|', sent)
##time.sleep(1)

t = time.time()
msg_c = "command"
sent = 0
print ('Start ', t, '|', msg_c, '|', sent)
msg_c = msg_c.encode(encoding="utf-8")
sent = sock.sendto(msg_c, tello_address)
print ('Start ', t, '|', msg_c, '|', sent)

t = time.time()
msg_to = "takeoff"
sent = 0
print ('Start ', t, '|', msg_to, '|', sent)
msg_to = msg_to.encode(encoding="utf-8")
sent = sock.sendto(msg_to, tello_address)
print ('Start ', t, '|', msg_to, '|', sent)
time.sleep(5)

fly_poly(3)

t = time.time()
msg_l = "land"
sent = 0
print ('Start ', t, '|', msg_l, '|', sent)
msg_l = msg_l.encode(encoding="utf-8")
sent = sock.sendto(msg_l, tello_address)
print ('Start ', t, '|', msg_l, '|', sent)
time.sleep(1)


while True:

    try:
        msg = input("");
        print (msg)
##        msg = 'battery?'
##        print (msg)

        if not msg:
            break

        if 'end' in msg:
            print ('...')
            sock.close()
            break

        # Send data
        msg = msg.encode(encoding="utf-8")
        sent = sock.sendto(msg, tello_address)
    except KeyboardInterrupt:
        print ('\n . . .\n')
        sock.close()
        break




