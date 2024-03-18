import socket
import datetime
import time
whatip = input("What ip would you like to host from?")

def server_program():
    host = whatip
    port = 20007  # initiate port no above 1024
    server_socket = socket.socket()  # get instance
    server_socket.bind((host, port))  # bind host address and port together
    server_socket.listen(5)
    while True:
        try:
            conn, address = server_socket.accept()
            while True:
                try:
                    data = conn.recv(1024).decode()
                    print("from connected user: " + str(data))
                    #Log Goes Here
                    data = ("Message processed.")
                    conn.send(data.encode())
                except:
                    print("Connection lost.")
                    break
        except:
            print("No Conncetion.")

server_program()
