import socket

for i in range(80,90):
    sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock.connect_ex(("192.168.0.1",i))
    if sock == 0:
        print("false")
    else:
        print("true")
        print(i)
    sock.close()
