# Basic Network Sniffer 

Hey everyone! This is my first project for the CodeAlpha Cybersecurity Internship. It’s a simple yet effective packet sniffer built in Python using the `scapy` library. 

The main goal of this tool is to capture live network traffic, break down packet structures, and display key information like source/destination IPs, protocols, and payloads directly in the terminal[cite: 1].

---

### What It Does
* Captures live packets flowing through your network interface[cite: 1].
* Filters and identifies core protocols like **TCP**, **UDP**, and **ICMP**[cite: 1].
* Extracts and prints out source and destination IP addresses[cite: 1].
* Inspects transport layer payloads to see raw data snippets[cite: 1].

---

### Prerequisites
Before running the script, make sure you have the following installed on your machine:
1. **Python 3.x**
2. **Scapy library**: You can install it via pip:
   ```bash
   pip install scapy
3. Scapy requires Npcap to capture raw network packets. Make sure to check the box for "Install Npcap in WinPcap API-compatible Mode" during setup.

### How to run it
Because packet sniffing requires raw socket access, you need to run your terminal with administrator/root privileges.
1. Clone or download this repository.
2. Open your terminal (PowerShell or Command Prompt) as Administrator.
3. Navigate to the project folder:
Bash
cd "Basic Network Sniffer"
4. Run the script:
Bash
python sniffer.py
5. (Optional) To test it out, open a separate terminal window and run a ping test (e.g., ping google.com) to see live packets getting logged in real-time!

Built As Part Of
Internship: CodeAlpha Cybersecurity Internship[cite: 1]
Task: Task 1 - Basic Network Sniffer[cite: 1]
