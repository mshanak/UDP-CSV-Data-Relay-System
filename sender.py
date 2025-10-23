import socket
import csv
import time
import sys

# Configuration
CSV_FILE = 'data.csv'
RELAY_IP = '127.0.0.1'
RELAY_PORT = 5000
INTERVAL = 1  # seconds

def send_csv_rows():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    try:
        with open(CSV_FILE, 'r') as f:
            reader = csv.reader(f)
            header = next(reader, None)
            
            if header:
                print(f"CSV Header: {','.join(header)}")
            
            row_count = 0
            for row in reader:
                if row:  # Skip empty rows
                    message = ','.join(row)
                    sock.sendto(message.encode(), (RELAY_IP, RELAY_PORT))
                    row_count += 1
                    print(f"Sent row {row_count}: {message}")
                    time.sleep(INTERVAL)
            
            print(f"\nFinished sending {row_count} rows")
    
    except FileNotFoundError:
        print(f"Error: CSV file '{CSV_FILE}' not found")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}")
    finally:
        sock.close()

if __name__ == "__main__":
    print(f"Starting UDP sender...")
    print(f"Target: {RELAY_IP}:{RELAY_PORT}")
    print(f"Interval: {INTERVAL}s\n")
    send_csv_rows()