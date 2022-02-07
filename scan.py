import socket
import sys

b="""
        comando del scaner
    python scan.py ip rango de puertos 
    ----------------------------------
    -`                    
                  .o+`              
                 `ooo/              
                `+oooo:             
               `+oooooo:                
               -+oooooo+:                
             `/:-:++oooo+:               
            `/++++/+++++++:              
           `/++++++++++++++:             
          `/+++ooooooooooooo/`           
         ./ooosssso++osssssso+`     
        .oossssso-````/ossssss+`
       -osssssso.      :ssssssso.
      :osssssss/        osssso+++.
     /ossssssss/        +ssssooo/-
   `/ossssso+/:-       -:/+osssso+-
  `+sso+:-`                 `.-/+oso:
 `++:.                          `-/+/
 .`                                 `/
            xela-stone-666
"""
print(b)

host=input("Nombre del host : ")
port=int(input("rango de puerto : "))
port_end=int(input("rango de puerto : "))
ports=[]
for i in range(port,port_end):
    sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock.settimeout(10)
    lista=sock.connect_ex((host,i))
    if lista == 0:
        ports.append(i)
#print(lista_de-puertos)
for s in ports:
    print(f"estos son los puertos abiertos {s}")

