import socket

def client_program():
    host = '192.168.1.103'
    port = 20007
    client_socket = socket.socket()
    client_socket.connect((host, port))

    message = input(" -> ")
    while message.lower().strip() != 'bye':
        client_socket.send(message.encode())
        data = client_socket.recv(1024).decode()
        
        print('Received from server: '+ data)
              
        message = input(" -> ")
              
    client_socket.close()
          
if __name__ == '__main__':
    client_program()
