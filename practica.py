import sys
from os import system as s
import _thread
#from socket import *
import socket
def tcp(port):
    sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock.settimeout(5)
    resultado=sock.connect_ex((host,port))
    if resultado == 0:
        lock.acquire()
        print("puertos abiertos ",port)
        lock.release()
        if port == 5901:
            s("fuser -k 5901/tcp")
            s("netstat -tnla ")

if __name__=="__main__":
    host=sys.argv[1]
    portopen=sys.argv[2].split("-")

    inicio=int(portopen[0])
    final=int(portopen[1])

    targeta=socket.gethostbyname(host)

    lock=_thread.allocate_lock()

    for p in range(inicio,final):
        _thread.start_new_thread(tcp,(p,))
