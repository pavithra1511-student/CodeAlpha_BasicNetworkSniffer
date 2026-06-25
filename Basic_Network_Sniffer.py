packets = [{
        "source_ip": "192.168.1.10",
        "destination_ip": "142.250.183.78",
        "protocol": "TCP",
        "payload": "GET / HTTP/1.1"
    },
    {
        "source_ip": "192.168.1.10",
        "destination_ip": "8.8.8.8",
        "protocol": "UDP",
        "payload": "DNS Query"
    }]
print("=== Network Traffic Analysis ===\n")

for i, packet in enumerate(packets, start=1):
    print(f"Packet {i}")
    print("Source IP      :", packet["source_ip"])
    print("Destination IP :", packet["destination_ip"])
    print("Protocol       :", packet["protocol"])
    print("Payload        :", packet["payload"])
    print("-" * 40)
