import socket

# Configuration
LISTEN_IP = '0.0.0.0'
LISTEN_PORT = 5001
BUFFER_SIZE = 4096

def receive_packets():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((LISTEN_IP, LISTEN_PORT))
    
    print(f"Receiver listening on {LISTEN_IP}:{LISTEN_PORT}\n")
    
    try:
        msg_count = 0
        while True:
            data, addr = sock.recvfrom(BUFFER_SIZE)
            msg_count += 1
            payload = data.decode()
            src_ip, src_port = addr
            
            print(f"Message {msg_count} received from {src_ip}:{src_port}")
            print(f"Data: {payload}\n")
    
    except KeyboardInterrupt:
        print(f"\nReceiver stopped. Total messages: {msg_count}")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        sock.close()

if __name__ == "__main__":
    receive_packets()