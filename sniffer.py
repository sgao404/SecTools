# ifconfig eth0 promisc

import socket
import struct
import binascii

s = socket.socket(socket.PF_PACKET, socket.SOCK_RAW, socket.
ntohs(0x0800))
# 0x0800 code defines the protocol ETH_P_IP

while True:
    pkt = s.recvfrom(2048)
    ethhead = pkt[0][0:14] #14 bytes long and at first
    eth = struct.unpack("!6s6s2s",ethhead)
    # ! shows network bytes, and 6s shows 6 bytes

    print "--------Ethernet Frame--------"
    print "desination mac",binascii.hexlify(eth[0])
    print "Source mac",binascii.hexlify(eth[1])
    binascii.hexlify(eth[2])

    ipheader = pkt[0][14:34] # ip header after ethernet

    #ip_hdr = struct.unpack("!12s4s4s",ipheader)
    ip_hdr = struct.unpack("!8sB3s4s4s",ipheader)
    print "-----------IP------------------"
    print "TTL :", ip_hdr[1]
    print "Source IP", socket.inet_ntoa(ip_hdr[3])
    print "Destination IP", socket.inet_ntoa(ip_hdr[4])


    tcpheader = pkt[0][34:54] # 3rd is tcp header

    #tcp_hdr = struct.unpack("!HH16s",tcpheader)
    tcp_hdr = struct.unpack("!HH9ss6s",tcpheader)
    print "Source Port ", tcp_hdr[0]
    print "Destination port ", tcp_hdr[1]
    print "Flag ",binascii.hexlify(tcp_hdr[3])# 4th part
