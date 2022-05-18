import socket

host = ''
port = 50002     # Arbitrary non-privileged port

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))

print 'running listensocket.py' '\n' 'host: localhost', '\n' 'port: ', port

s.listen(5)

conn, addr = s.accept()
print('Connected by', addr)

while True:
    try:
        data = conn.recv(1024)
        if not data: break

        print "UE Says: "+data

#        print "Client Says: "+data
        conn.sendall("Server Says:hi")

    except socket.error:
        print "Error Occured."
        break

conn.close()

