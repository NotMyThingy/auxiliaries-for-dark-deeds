import socket

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
