from scapy.all import sniff
#This line imports the sniff function from Scapy's all module.
#The sniff function allows you to capture packets from a network interface.
#Scapy is a Python library used for packet manipulation, network analysis, and sniffing.
def packet_callback(packet):
#This line defines a function called packet_callback that takes one parameter packet.
#The packet parameter represents each individual network packet that is captured by Scapy.
# The packet_callback function will be called every time a packet is captured, and the packet will be passed to this function for processing.
    print(packet.summary())
#This line prints a summary of the packet using Scapy's built-in summary() method.
sniff(prn=packet_callback,count=10)
#This line tells Scapy to start sniffing network packets, and for each packet captured, it will call the packet_callback function to print the summary of the packet. It will stop after 10 packets.
