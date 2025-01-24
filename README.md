# PACKET-SNIFFER
# Simple Network Packet Sniffer

This is a simple packet sniffer project developed in Python using the Scapy library. The program captures and analyzes network packets, displaying key details like source and destination IP addresses, protocols, and ports.

## Features
- Captures packets from a specified network interface.
- Displays packet details in a summary format.
- Lightweight and simple to use for basic network packet analysis.

## Prerequisites

Before running this project, make sure you have the following:

- **Python 3.x**: [Download Python](https://www.python.org/downloads/)
- **Scapy Library**: Scapy is used for packet capture and analysis. You can install it via pip:
  ```bash
  pip install scapy
  ```

## How to Use

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/packet-sniffer.git
   ```

2. **Navigate to the project folder**:
   ```bash
   cd packet-sniffer
   ```

3. **Run the script**:
   - Open the project folder in your terminal or PyCharm.
   - Run the Python file to start sniffing:
     ```bash
     python packet_sniffer.py
     ```
   - The program will prompt you to enter the network interface (e.g., `eth0` for Ethernet or `wlan0` for Wi-Fi).
   - It will display summaries of the captured packets.

## Example Output

Here’s what the output might look like when the program captures packets:
Ether / IP / TCP 172.64.155.209:https > 192.168.1.9:44075 PA / Raw
Ether / IP / TCP 172.64.155.209:https > 192.168.1.9:44075 PA / Raw
Ether / IP / TCP 172.64.155.209:https > 192.168.1.9:44075 PA / Raw
Ether / IP / TCP 192.168.1.9:44075 > 172.64.155.209:https A
Ether / IP / TCP 192.168.1.9:44075 > 172.64.155.209:https PA / Raw
Ether / IP / TCP 172.64.155.209:https > 192.168.1.9:44075 A
Ether / IP / TCP 192.168.1.9:43633 > 20.198.119.84:https PA / Raw
Ether / IP / TCP 20.198.119.84:https > 192.168.1.9:43633 PA / Raw
Ether / IP / TCP 192.168.1.9:43633 > 20.198.119.84:https A
Ether / IP / TCP 192.168.1.9:43859 > 20.198.119.84:https A / Raw

 
 🎉 We welcome contributions.


