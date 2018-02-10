import socket, sys
from thread import *
from time import sleep

if len(sys.argv) != 3:
    print "Correct usage: IP address, port number (default 999)"
    exit()

HOST = str(sys.argv[1])
PORT = int(sys.argv[2])

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

def se(s):
    while True:
        s.send(raw_input())
def re(s):
    while 1:
        r = s.recv(1024)
        if r != 'No messages':
            print r
        sleep(0.05)
start_new_thread(se ,(s,))
start_new_thread(re ,(s,))
while 1:
    pass
