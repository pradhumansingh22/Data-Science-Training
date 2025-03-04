import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
ip_address = ""
port = 6969

complete = (ip_address, port)
s.bind(complete)

while True:
   msg =  s.recvfrom(1024)
   decodedMsg = msg[0].decode("ascii")
   print(decodedMsg)