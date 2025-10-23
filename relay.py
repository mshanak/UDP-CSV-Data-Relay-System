import socket

# Configuration
LISTEN_IP = '0.0.0.0'
LISTEN_PORT = 5000
RECEIVER_IP = '127.0.0.1'
RECEIVER_PORT = 5001
BUFFER_SIZE = 4096

def relay_packets():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((LISTEN_IP, LISTEN_PORT))
    
    print(f"Relay listening on {LISTEN_IP}:{LISTEN_PORT}")
    print(f"Forwarding to {RECEIVER_IP}:{RECEIVER_PORT}\n")
    
    try:
        while True:
            data, addr = sock.recvfrom(BUFFER_SIZE)
            payload = data.decode()
            src_ip, src_port = addr
            
            # Print received packet info
            print(f"--- Packet Received ---")
            print(f"Source IP: {src_ip}:{src_port}")
            print(f"Destination IP: {LISTEN_IP}:{LISTEN_PORT}")
            print(f"Payload: {payload}")
            print(f"--- Forwarding ---\n")
            
            # Forward to receiver
            sock.sendto(data, (RECEIVER_IP, RECEIVER_PORT))
    
    except KeyboardInterrupt:
        print("\nRelay stopped")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        sock.close()

if __name__ == "__main__":
    relay_packets()