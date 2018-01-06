from scapy.all import *
ip1 = IP(src="10.0.1.57", dst ="10.0.1.47")
sy1 = TCP(sport =1024, dport=80, flags="F", seq=12345)
packet = ip1/sy1
p =sr1(packet)
p.show()

#if contains the RST/ACK flag, 
#which means that the port is closed
