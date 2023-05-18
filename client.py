import socket

HOST = "192.168.1.3"
PORT = 1010

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect((HOST, PORT))

socket.send("Hello World".encode())
print(socket.recv(1024).decode())