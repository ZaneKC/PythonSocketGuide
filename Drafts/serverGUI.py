from tkinter import *
import socket

root = Tk()
root.title('Main Server Hub')
root.geometry("750x600")
#frame1 = Frame(root, width = 750, height = 600)
#frame1.pack()
frame1 = Frame(root)
frame1.place(x=0,y=0)
#INITAL
def Reload():
    try:
        data = conn.recv(1024).decode(utf-8)
        ACS.insert(END, data = '\n')
    except:
        print("No message, or no connection.")
def ConCheck():
    global conn
    try:
        conn, address = server_socket.accept()
        print("Connection from: " + str(address))
    except:
        print("No incoming connection.")
def SendCom():
    try:
        global message
        message = ACR.get()
        message = str(message)
        conn.send(message.encode())
    except:
        print("Message not sent.")
def Open():
    global ACS
    global ACRL
    global ACR
    ACT = Label(root, text=("Active server: " + Ip))
    ACT.place(x=0, y=0)

    ACR = Entry(root, width = 25)
    ACR.place(relx=.25, rely=.3,anchor= CENTER)

    ACRB = Button(root, width = 15, height = 2, text="Send", bg='light grey', command=SendCom)
    ACRB.place(relx=.25, rely=.55, anchor= CENTER)

    ACS = Text(root, width = 25, height = 15)
    ACS.place(relx=.7, rely=.3,anchor= CENTER)

    ACST = Label(root, text="Receiving", font=('Times New Roman', 10, 'bold'))
    ACST.place(relx=.7, rely=.07,anchor= CENTER)

    ACRL = Button(root, width = 15, height = 2, text="Reload", bg='light grey', command=Reload)
    ACRL.place(relx=.7, rely=.55, anchor= CENTER)

    CONB = Button(root, width = 15, height = 2, text="Check for connection.", bg='light grey', command=ConCheck)
    CONB.place(relx=.45, rely=.55, anchor= CENTER)
    
def NewTab():
    SEE.destroy()
    SEB.destroy()
    SET.destroy()
    SE.destroy()
    
def Start():
    try:
        global server_socket
        global Ip
        Ip = str(SE.get())
        host = Ip
        port = 20007
        server_socket = socket.socket()
        server_socket.bind((host, port))
        server_socket.listen(2)
        server_socket.setblocking(False)

        NewTab()
        Open()
    except:
        SEE.delete("1.0", END)
        SEE.insert(END, "Failed Host, Invalid IP.")
#FIRSTTAB
SEE = Text(root, width = 25, height = 2)
SEE.place(relx=.5, rely=.7,anchor= CENTER)

SEB = Button(root, width = 10, text="Start", command=Start)
SEB.place(relx=.7, rely=.5,anchor= CENTER)

SET = Label(root, text="What IP would you like to host from?", font=('Times New Roman', 25, 'bold'))
SET.place(relx=.5, rely=.43,anchor= CENTER)

SE = Entry(root, width = 35)
SE.place(relx=.5, rely=.5,anchor= CENTER)

root.mainloop()



def server_program():
    host = '192.168.1.103'
    port = 20007  # initiate port no above 1024
    server_socket = socket.socket()  # get instance
    server_socket.bind((host, port))  # bind host address and port together
    server_socket.listen(10)
    conn, address = server_socket.accept()  # accept new connection
    print("Connection from: " + str(address))
    while True:
        data = conn.recv(1024).decode()
        if not data:
            break
        print("from connected user: " + str(data))
        data = input(' -> ')
        conn.send(data.encode())
        
if __name__ == '__main__':
    server_program()
