from scapy.all import ICMP, IP, TCP, UDP, sniff


def packet_callback(packet):
    # 1st-->Checking if the packet has an IP layer
  if packet.haslayer(IP):
    ip_layer = packet.getlayer(IP)
    src_ip = ip_layer.src
    dst_ip = ip_layer.dst

    # 2nd-->Identifying the protocol
    protocol = "OTHER"
    if packet.haslayer(TCP):
      protocol = "TCP"
    elif packet.haslayer(UDP):
      protocol = "UDP"
    elif packet.haslayer(ICMP):
      protocol = "ICMP"

    print(f"\n[+] Packet Captured:")
    print(f"    Source IP      : {src_ip}")
    print(f"    Destination IP : {dst_ip}")
    print(f"    Protocol       : {protocol}")

    # 3rd-->Extracting and displaying payload (if present)
    if packet.haslayer(TCP) or packet.haslayer(UDP):
      payload = bytes(packet.payload.payload)  # Transport layer payload
      if payload:
        print(f"    Payload (First 50 bytes): {payload[:50]!r}")
      else:
        print("    Payload        : [Empty/No Data]")
    print("-" * 50)


def main():
  print("[*] Starting Network Sniffer...")
  print("[*] Press Ctrl+C to stop capturing.\n")

  # 4th-->Starting sniffing network packets (store=False prevents memory leaks)
  sniff(prn=packet_callback, store=False)


if __name__ == "__main__":
  main()