import socket
import threading
import sys
def send():
    msg = input(" > ")
    while msg != "exit":
        client_socket.send(bytes(msg, "utf8"))
        msg = input(" > ")

def receive():
    while True:
        ans = client_socket.recv(1024)
        if not ans:
            break
        print(str(ans, "utf8"))

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 1337
client_socket.connect((host,port))
threading.Thread(target=send).start()
threading.Thread(target=receive).start()
