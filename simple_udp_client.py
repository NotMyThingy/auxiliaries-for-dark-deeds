import socket

RHOST = "127.0.0.1"
RPORT = 1337

# create a socket
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# send some data
# as UDP is connectionless, there's no connect call.
client.sendto(b"AAABBBCCC", (RHOST, RPORT))

# receive data
data, addr = client.recvfrom(4096)

print(data.decode)
client.close
