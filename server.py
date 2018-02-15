import socket
import threading
import select

# def send(c):
#     inready,outputready,exceptrdy = select.select([],c,[])
#     for i in outputready:
#         i.send(msg)
#
# def receive(c):
#     while True:
#         inputready,outready,exceptrdy = select.select([c],[],[])
#         if inputready != []:
#             msg = c.recv(1024)
#             if not msg:
#                 break
#             print(str(msg, "utf8"))

class ClientThread(threading.Thread):
    def __init__(self, clientAddr, client_socket):
        threading.Thread.__init__(self)
        self.csocket = client_socket
        self.connections = []
    def run(self):
        print("Connection")
        self.connections.append(self.csocket)
        # threading.start_new_thread(receive, (self.csocket))
        self.c = []
        for i in self.connections:
            self.c.append(i)
        self.c.remove(self.csocket)
        # threading.start_new_thread(send, (self.c))
        while True:
            msg = self.csocket.recv(1024)
            if not msg:
                break
            print(str(msg, "utf8"))
        self.connections.remove(self.csocket)
        print("client disconnected")

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = ''
port = 5000
server_socket.bind((host, port))
while True:
    server_socket.listen(1)
    (client_socket, addr) = server_socket.accept()
    newthread = ClientThread(addr, client_socket)
    newthread.start()
