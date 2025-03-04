import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
ip_address = ""
port = 5000
complete = (ip_address, port)

while True:
    message = input("Enter your message: ")
    encodedMessage = message.encode("ascii")
    s.sendto(encodedMessage, complete)