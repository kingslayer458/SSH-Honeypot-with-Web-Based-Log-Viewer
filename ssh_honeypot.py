import paramiko
import socket
import logging
from threading import Thread

# Set up logging
logging.basicConfig(filename='ssh_honeypot.log', level=logging.INFO, format='%(asctime)s - %(message)s')

# Honeypot configuration
HOST = '0.0.0.0'
PORT = 2222

def handle_connection(client_sock):
    try:
        transport = paramiko.Transport(client_sock)
        transport.add_server_key(paramiko.RSAKey.generate(2048))
        server = paramiko.ServerInterface()

        transport.start_server(server=server)

        while True:
            channel = transport.accept(1)
            if channel is None:
                break

            client_ip = client_sock.getpeername()[0]
            logging.info(f"Connection from {client_ip}")

            channel.send("Welcome to the SSH server.\r\n")
            while True:
                try:
                    command = channel.recv(1024).decode('utf-8').strip()
                    if not command:
                        break

                    logging.info(f"Command from {client_ip}: {command}")
                    channel.send(f"Command '{command}' executed.\r\n")
                except Exception as e:
                    logging.error(f"Error: {e}")
                    break

            channel.close()
    except Exception as e:
        logging.error(f"Error: {e}")
    finally:
        client_sock.close()

def start_honeypot():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind((HOST, PORT))
    sock.listen(100)

    logging.info(f"Honeypot started on {HOST}:{PORT}")

    while True:
        client_sock, addr = sock.accept()
        Thread(target=handle_connection, args=(client_sock,)).start()

if __name__ == "__main__":
    start_honeypot()