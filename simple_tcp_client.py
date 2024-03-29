import socket

RHOST = "0.0.0.0"
RPORT = 9998

# create a socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect the client
client.connect((RHOST, RPORT))

# send data
client.send(b"GET / HTTP/1.1\r\nHost: google.com\r\n\r\n")

# receive data
response = client.recv(4096)

print(response.decode())
client.close
