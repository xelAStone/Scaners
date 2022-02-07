import socket
from socket import *
import _thread

print("Esta es una herramienta de scaneo de puertos")

def conexion():
    sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock.settimeout(10)
    ip=sock.connect_ex((host,port))
    if ip == 0:
        lock.acquire()
        print("puerto abierto ")
        lock.relase()
if __name__=="__main__":
    host=input("Direccion del host : ")
    host=gethostbyname(host)
    lock=_thread.allocate_lock()

    for i in range(22,8000):
        _thread.start_new_thread(conexion,(i,))
