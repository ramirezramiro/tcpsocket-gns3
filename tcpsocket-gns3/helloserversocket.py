import socket

host = '192.168.122.71'
port = 50002                   # The same port as used by the server

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))

print 'starting connection to' '\n' 'host: ', host, '\n' 'port: ',  port

s.sendall(b'Hello, world')
data = s.recv(1024)
print 'sending data from UE to Server...'


print('Received msg from server:', repr(data))

