# UDP Pinger

Autor: Adilet Aitmatov;

Student id: 12230114;

## UDP Server
After start, the server waits for client connection, as soon as client connects, the server receives a ping message from client and then sends a pong message to the client. 
## UDP Client
- After start, the client starts execution of program described below:
- - Client connects to the server;
- - Saves current time;
- - Sends a ping message to the server. Ping message will contain information such as “id”, “value” and “date” from the objects of wheel_rotation_sensor_data.json;
- - Receives the pong message from the server;
- - Saves current time and calculates RTT;
- Client has a function that informs the user if a packet is lost. In this program I assume that the packet is lost after 1 sec wait.


## Usage
First of all you need to start server:
```python
python3 UDPServer.py
```
If command above doesn't work try this command:
```python
python UDPServer.py
```
Next you should start client:
```python
python3 UDPClient.py
```
If command above doesn't work try this command:
```python
python UDPClient.py
```