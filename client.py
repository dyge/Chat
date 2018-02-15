import socket
import threading

# def send():
#     msg = input(" > ")
#     while msg != "exit":
#         client_socket.send(bytes(msg, "utf8"))
#         msg = input(" > ")
#
# def receive():
#     while True:
#         ans = client_socket.recv(1024)
#         if not ans:
#             break
#         print(str(ans, "utf8"))

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 5000
client_socket.connect((host,port))
msg = input(" > ")
while msg != "exit":
    client_socket.send(bytes(msg, "utf8"))
    msg = input(" > ")
# thread_send = threading.Thread(target=send)
# thread_send.start()
# thread_receive = threading.Thread(target=receive)
# thread_receive.start()
client_socket.close()
