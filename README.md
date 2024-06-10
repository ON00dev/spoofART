### Network Analysis and Testing Tool with Scapy

This nifty tool uses the Scapy interactive library to tackle all sorts of network shenanigans, making security analysis and testing a breeze. Perfect for security pros, network wizards, cyber sleuths, and curious students, it boasts features like ping, packet capture, sending sneaky TCP SYN packets, traceroute, DNS queries, and even a cheeky example of a SYN Flood attack. Happy hacking!

### Features

- **Ping (ping_target)**: Checks connectivity with a specified target by sending ICMP packets.
- **Packet Capture (sniff_packets)**: Captures and displays a specified number of network packets.
- **Send TCP SYN Packet (send_tcp_syn)**: Sends a single TCP SYN packet to a specified target and port.
- **SYN Flood Attack (syn_flood)**: Educational example of a SYN Flood attack using random source IP addresses.
- **Traceroute (traceroute_target)**: Traces the route that packets take to reach a target.
- **DNS Query (dns_query)**: Performs a DNS query for a specified domain.

### Usage

1. Clone the repository:
    ```bash
    git clone https://github.com/ON00dev/spoofART.git
    cd spoofART
    ```

2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Run the main script:
    ```bash
    python script.py
    ```

4. Follow the instructions in the interactive menu to select and execute the desired network operations.

### Security and Ethical Considerations

- **Permission**: Perform network tests only with explicit permission and in controlled environments.
- **Legality**: Conducting denial-of-service (DoS) attacks or any form of intrusion without permission is illegal and can result in severe legal penalties.
- **Ethics**: Use your cybersecurity knowledge ethically to protect and improve network infrastructure without causing harm or disruptions.

---

This tool is a valuable addition to the toolkit of any network security professional or student, providing a practical and safe learning environment to explore network operations and cybersecurity.
