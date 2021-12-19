import socket
from typing import Collection
server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(("localhost",2020))
server.listen()


client , addres=server.accept()
done=False
while not done:
    print(client.recv(1024).decode('utf-8'))
    if mesg=="quit":
        done=True
    else:
        print(mesg)
    client.send(input("Message: ").encode('utf-8'))
    
server.close()
client.close()
