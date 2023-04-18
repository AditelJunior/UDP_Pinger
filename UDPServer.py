import socket

# UDP server address and port
server_address = ('localhost', 10000)

# Create a UDP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to the server address and port
server_socket.bind(server_address)

while True:
    # Receive the ping message from the client
    ping_message, client_address = server_socket.recvfrom(1024)

    # Send the pong message back to the client
    server_socket.sendto(ping_message, client_address)