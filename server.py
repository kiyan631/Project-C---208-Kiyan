import socket
from threading import Thread
IP_ADRESS = '127.0.0.2'
PORT = 8079
SERVER = None
clients = {}

def acceptConnections():
    global SERVER
    global clients

    while True:
        client,addr = SERVER.accept()
        print(client,addr)


def setup():
    print("\n\t\t\t\t\t\t MUSICAL APP\n")


    global PORT
    global IP_ADRESS
    global SERVER

    SERVER = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    SERVER.bind((IP_ADRESS,PORT))
    SERVER.listen(100)

    print("\t\t\tSERVER IS WAITING FOR INCOMING CONNECTIONS...")
    print("\n")

    acceptConnections()

setup_thread = Thread(target=setup)
setup_thread.start()