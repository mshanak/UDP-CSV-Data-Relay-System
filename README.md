# UDP CSV Data Relay System

A Python-based UDP communication system that demonstrates packet forwarding through a relay server. The system reads CSV data and transmits it row-by-row through a network of three components: sender, relay, and receiver.

## Overview

This project consists of three Python scripts that work together to demonstrate UDP packet transmission and relay:

- **sender.py**: Reads a CSV file and sends each row as a UDP packet at configurable intervals
- **relay.py**: Acts as a middleware that receives packets, logs information, and forwards them
- **receiver.py**: Final destination that receives and displays the forwarded packets

```
[sender.py] --UDP--> [relay.py] --UDP--> [receiver.py]
   (5000)              (5001)
```

## Features

- 📤 CSV file parsing and row-by-row transmission
- 🔄 Packet relay with detailed logging
- 📊 Source/destination IP tracking
- ⏱️ Configurable transmission intervals
- 🖥️ Simple command-line interface

## Requirements

- Python 3.6 or higher
- No external dependencies (uses only standard library)

## Installation

1. Clone or download this repository
2. Ensure Python 3 is installed on your system
3. No additional packages need to be installed

## File Structure

```
.
├── sender.py       # CSV reader and UDP sender
├── relay.py        # UDP packet relay with logging
├── receiver.py     # UDP packet receiver
├── data.csv        # Sample CSV file (you need to create this)
└── README.md       # This file
```

## Setup

### 1. Create a CSV File

Create a file named `data.csv` in the same directory as the scripts. Example:

```csv
name,age,city
Alice,30,Berlin
Bob,25,Munich
Charlie,35,Hamburg
David,28,Dresden
```

### 2. Configure Network Settings (Optional)

Each script has configuration variables at the top that you can modify:

**sender.py:**
```python
CSV_FILE = 'data.csv'      # CSV file to read
RELAY_IP = '127.0.0.1'     # Relay IP address
RELAY_PORT = 5000          # Relay port
INTERVAL = 1               # Seconds between packets
```

**relay.py:**
```python
LISTEN_IP = '0.0.0.0'      # Listen on all interfaces
LISTEN_PORT = 5000         # Port to receive on
RECEIVER_IP = '127.0.0.1'  # Receiver IP address
RECEIVER_PORT = 5001       # Receiver port
```

**receiver.py:**
```python
LISTEN_IP = '0.0.0.0'      # Listen on all interfaces
LISTEN_PORT = 5001         # Port to receive on
```

## Usage

### Running the System

Open **three separate terminal windows** and run the scripts in this order:

#### Terminal 1 - Start the Receiver
```bash
python receiver.py
```

Expected output:
```
Receiver listening on 0.0.0.0:5001
```

#### Terminal 2 - Start the Relay
```bash
python relay.py
```

Expected output:
```
Relay listening on 0.0.0.0:5000
Forwarding to 127.0.0.1:5001
```

#### Terminal 3 - Start the Sender
```bash
python sender.py
```

Expected output:
```
Starting UDP sender...
Target: 127.0.0.1:5000
Interval: 1s

CSV Header: name,age,city
Sent row 1: Alice,30,Berlin
Sent row 2: Bob,25,Munich
...
```

### Expected Behavior

**Relay Output:**
```
--- Packet Received ---
Source IP: 127.0.0.1:52341
Destination IP: 0.0.0.0:5000
Payload: Alice,30,Berlin
--- Forwarding ---
```

**Receiver Output:**
```
Message 1 received from 127.0.0.1:5000
Data: Alice,30,Berlin

Message 2 received from 127.0.0.1:5000
Data: Bob,25,Munich
```

### Stopping the System

Press `Ctrl+C` in each terminal window to stop the scripts gracefully.

## Configuration Examples

### Change Transmission Speed

To send data every 0.5 seconds instead of 1 second, modify `sender.py`:
```python
INTERVAL = 0.5
```

### Use Different CSV File

To use a different CSV file, modify `sender.py`:
```python
CSV_FILE = 'my_custom_data.csv'
```

### Run on Different Machines

To run the components on separate machines:

1. **Machine A (Sender)**: Set `RELAY_IP` to the IP of Machine B
2. **Machine B (Relay)**: Set `RECEIVER_IP` to the IP of Machine C
3. **Machine C (Receiver)**: No changes needed

Make sure firewall rules allow UDP traffic on the configured ports.

## Troubleshooting

### "CSV file not found" Error
- Ensure `data.csv` exists in the same directory as `sender.py`
- Check the `CSV_FILE` variable points to the correct file path

### No Data Received
- Verify all three scripts are running
- Check that ports 5000 and 5001 are not blocked by firewall
- Ensure the IP addresses in configuration match your network setup

### "Address already in use" Error
- Another process is using the port
- Stop the conflicting process or change the port number
- On Linux/Mac, find the process: `lsof -i :5000`
- On Windows, find the process: `netstat -ano | findstr :5000`



