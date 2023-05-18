import socket

# host = socket.gethostbyname(socket.gethostname())

HOST = "192.168.1.3"
PORT = 1010
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))

server.listen(5)

while True:
    communication_socket, address = server.accept()
    print(f"connected to {address}")
    message = communication_socket.recv(1024).decode()
    print(f"message from client is {message}")
    communication_socket.send("Your message has been received, Thank you!".encode())
    communication_socket.close()
    print(f"Comunication with {address} ended!")
    