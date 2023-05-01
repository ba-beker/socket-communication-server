# Socket Communication Server
This project is a simple implementation of socket communication in Python. It consists of two files, server.py and client.py, which enable communication between a server and a client using TCP sockets.

Link to project: https://github.com/ba-beker/socket-communication-server

## How It's Made:
      Tech used: Python
      
The server.py file creates a socket object with IPv4 address family and TCP socket type. It then binds the socket to a specific IP address and port number, and listens for incoming connections from clients. When a client connects, the server accepts the connection, receives a message from the client, sends a response message back to the client, and closes the communication socket. This process repeats in an infinite loop to allow multiple clients to connect and communicate with the server.

The client.py file creates a socket object with IPv4 address family and TCP socket type, and connects to the server using the IP address and port number specified. It then sends a message to the server and receives a response message back from the server.

# Lessons Learned:

This project helped me to understand the basics of socket communication and how it can be implemented in Python. I learned how to create a server that listens for incoming connections and a client that can connect to the server and send/receive messages. I also learned about the importance of error handling and proper socket closure to prevent resource leaks and ensure reliable communication.
