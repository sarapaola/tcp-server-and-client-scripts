#  Import the library with the modules for creating and managing the socket
import socket

# Declare which IP and port the program should communicate to via the socket
target_host = "0.0.0.0"
target_port = 9998

# You create the socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# AF_INET = socket uses IPv4 or hostname
# SOCK_STREAM = socket uses TCP protocol

# Connection is made with the server
client.connect((target_host,target_port))

# Submit the desired datai
client.send(b"Hello server")

# Receive the response from the server
response = client.recv(4096)

# Response received is printed on the terminal
print(response.decode())

# Close the socket and communication
client.close()
