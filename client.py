import socket
client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(("localhost",2020))
done=False
while not done:
    client.send(input("Message: ").encode('utf-8'))
    mesg=client.recv(1024).decode('utf-8')
    if mesg=="quit":
        done=True
    else:
        print(mesg)