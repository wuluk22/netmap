#!/usr/bin/env python

import scapy.all as scapy

def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]

    client_list = []
    for element in answered_list:
        client_dict = {"ip": element[1].psrc, "mac": element[1].hwsrc}
        client_list.append(client_dict)
    return client_list

def print_netmap(client_list):
    print("\nIP\t\t\tMAC address\n-----------------------------------")
    for element in client_list:
        print(element["ip"] + "\t\t" + element["mac"])

ip = raw_input("\nEnter IP to scan: ")
client_list = scan(ip)
print_netmap(client_list)