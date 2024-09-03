# Import the library with the modules for creating and managing the socket
import socket
# Import the library with the modules for thread creation and management
import threading

# Declare which IP and port the program should communicate to via the socket
ip = '0.0.0.0'
port = 9998

def main():
    # Create the socket object for the server
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Pass the parameters trmite by which the server listens on the network
    server.bind((ip, port))
    # Set the limit of connections made
    server.listen(5)
    print(f'[*] Listening on {ip}:{port}')

    while True:
    	# When a client connects, receive the client socket in the client variable and the remote connection details in the address variable
        client, address = server.accept()
        print(f'[*] Accepted connection from {address[0]}:{address[1]}')
        # Create a new thread object that points to handle_client function, and pass it the client socket object as an argument.
        client_handler = threading.Thread(target=handle_client, args=(client,))
        # Start the thread to handle the client connection, at which point the main server loop is ready to handle another incoming connection.
        client_handler.start()

def handle_client(client_socket):
    with client_socket as sock:
    	# Performs the recv() and then sends a simple message back to the client.
        request = sock.recv(1024)
        print(f'[*] Received: {request.decode("utf-8")}')
        sock.send(b'Hello client')

if __name__ == '__main__':
    main()
