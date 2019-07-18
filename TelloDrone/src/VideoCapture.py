import threading
import socket
import sys
import time
import cv2

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
            print(data.decode(encoding="utf-8"))
        except Exception:
            print ('\nExit . . .\n')
            break


print ('\r\n\r\nTello Python3 Demo.\r\n')

print ('Tello: command takeoff land flip forward back left right \r\n       up down cw ccw speed speed?\r\n')

print ('end -- quit demo.\r\n')


#recvThread create
recvThread = threading.Thread(target=recv)
recvThread.start()
msg = "command"
msg = msg.encode(encoding="utf-8")
sent = sock.sendto(msg, tello_address)
time.sleep (5)
msg = "battery?"
msg = msg.encode(encoding="utf-8")
sent = sock.sendto(msg, tello_address)
time.sleep (5)
msg = "streamon"
msg = msg.encode(encoding="utf-8")
sent = sock.sendto(msg, tello_address)
##cam = cv2.VideoCapture("http://192.168.10.1:8889")
cam = cv2.VideoCapture(0)
ret, img = cam.read()
while True:
    ret, img = cam.read()
    cv2.imshow('drone', img)
    if cv2.waitKey(1) == 27:
        break