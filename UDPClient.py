import json
import socket
import time

# UDP server address and port
server_address = ('localhost', 10000)

# Load the wheel_rotation_sensor_data.json and put it into variable
with open('./wheel_rotation_ sensor_data.json', 'r') as fileContent:
    sensor_data = json.load(fileContent)

# Create a UDP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

client_socket.settimeout(1)

for data in sensor_data:
    try:
    # Get the current time in seconds
        start_time = time.time()
       
    # Send and print the ping message to the server
        message = str( data['id']) + ' ' + data['date'] + ' ' + data['value']
        print("Ping message: " + message)
        client_socket.sendto(message.encode(), server_address)
    # Receive the pong message from the server
        pong_message, server = client_socket.recvfrom(1024)
        end_time = time.time()
    # Ping the server for each sensor data message and calculate RTT
        rtt = end_time - start_time
        print('Pong from {}: RTT = {:.4f} s'.format(server, rtt))
        
    except socket.timeout:
    # Time is out, assume packet was lost
        print('No reply from server')

# Close the socket
client_socket.close()