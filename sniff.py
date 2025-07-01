from scapy.all import sniff, IP, TCP, UDP, ICMP

# Callback function to process each packet
def process_packet(packet):
    # Check if packet has IP layer
    if IP in packet:
        ip_layer = packet[IP]
        src_ip = ip_layer.src
        dst_ip = ip_layer.dst
        proto = ip_layer.proto

        # Detect protocol type
        protocol = ''
        if proto == 6:
            protocol = 'TCP'
        elif proto == 17:
            protocol = 'UDP'
        elif proto == 1:
            protocol = 'ICMP'
        else:
            protocol = str(proto)

        print(f"\n--- Packet Captured ---")
        print(f"Source IP      : {src_ip}")
        print(f"Destination IP : {dst_ip}")
        print(f"Protocol       : {protocol}")

        # Display payload if exists
        payload = bytes(packet.payload.payload)
        if payload:
            print(f"Payload        : {payload[:50]}...")  # Limit to 50 bytes for readability

# Start sniffing
def main():
    print("Starting packet sniffer... Press CTRL+C to stop.")
    try:
        # iface can be specified as iface="eth0" or "Wi-Fi" depending on your machine
        sniff(filter="ip", prn=process_packet, store=False)
    except KeyboardInterrupt:
        print("\nSniffer stopped by user.")

if __name__ == "__main__":
    main()
