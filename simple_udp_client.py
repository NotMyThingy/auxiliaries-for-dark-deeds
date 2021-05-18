import socket

<<<<<<< HEAD
target_host = '127.0.0.1'
target_port = 80

# create socket object
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# send some...
client.sendto(b"AAABBBCCC", (target_host, target_port))
print('sent some shit ...')
# receive some...
some_data, addr = client.recvfrom(4096)
print('received some shit ...')

print(some_data.decode())
client.close()
=======
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
>>>>>>> origin/main
