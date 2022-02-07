import socket

host=input("nombre del host : ")
port=int(input("port : "))
sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.connect((host,port))
#sock.listen(1)
while True:
    so=sock.recv(1024)
    sock.send(so)
sock.close()
