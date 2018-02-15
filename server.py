import socket
import threading
import select

def send(co):
    msg_old = ''
    while True:
        try:
            if msg_old != msg:
                print(co)
                co.send(msg)
                print("send")
                msg_old = msg
        except NameError:
            pass

def receive(c):
    while True:
        global msg
        msg = c.recv(1024)
        if not msg:
            break
        print(str(msg, "utf8"))
    print("client disconnected")

class ClientThread(threading.Thread):
    def __init__(self, clientAddr, client_socket):
        threading.Thread.__init__(self)
        self.csocket = client_socket
        print(self.csocket)
    def run(self):
        print("Connection")
        connections.append(self.csocket)
        print(connections)
        t1 = threading.Thread(target=receive, args=(self.csocket,))
        t1.start()
        t2 = threading.Thread(target=send, args=(self.csocket,))
        t2.start()

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = ''
port = 1337
server_socket.bind((host, port))
connections = []
while True:
    server_socket.listen(1)
    (client_socket, addr) = server_socket.accept()
    newthread = ClientThread(addr, client_socket)
    newthread.start()
