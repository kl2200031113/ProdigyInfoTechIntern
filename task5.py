from scapy.all import sniff, Ether, IP, TCP, UDP

def packet_callback(packet):
    if packet.haslayer(IP):
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        protocol = packet[IP].proto
        
        print(f"IP Packet: {src_ip} -> {dst_ip} Protocol: {protocol}")
        
        if packet.haslayer(TCP):
            src_port = packet[TCP].sport
            dst_port = packet[TCP].dport
            print(f"TCP Port: {src_port} -> {dst_port}")
            if packet.haslayer(Raw):
                print(f"Raw Data: {packet[Raw].load}")
        
        elif packet.haslayer(UDP):
            src_port = packet[UDP].sport
            dst_port = packet[UDP].dport
            print(f"UDP Port: {src_port} -> {dst_port}")
            if packet.haslayer(Raw):
                print(f"Raw Data: {packet[Raw].load}")
        
        print("-----------------------------------------------")

def main():
    print("Network Packet Analyzer")
    print("Press Ctrl+C to stop sniffing.")
    
    # Start sniffing packets on the default interface (adjust as needed)
    sniff(filter="ip", prn=packet_callback, store=0)

if name == "main":
    main()