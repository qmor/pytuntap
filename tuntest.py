# -*- coding: utf-8 -*-
from tuntap import TunTap
import threading
import socket

def thread(tun):
    print("thread start")
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
    sock.bind(("0.0.0.0", 5005))
    while True:
        data, addr = sock.recvfrom(2048)
        #print("UDP recv: %s" % data.hex())
        tun.write(data)
master = True
udpto = "192.168.137.2"
tunip = "192.168.255.1"
if master is False:
    udpto = "192.168.137.1"
    tunip = "192.168.255.2"

tun = TunTap(nic_type="Tun", nic_name="tun0")
tun.config(ip=tunip, mask="255.255.255.0")
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

thr = threading.Thread(target=thread, args=[tun], daemon=True)
thr.start()
while True:
    buf = tun.read()
    #print(buf.hex())
    sock.sendto(buf, (udpto, 5005))
    


