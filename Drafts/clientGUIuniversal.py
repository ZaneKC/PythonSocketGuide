from tkinter import *
import socket
from time import *

root = Tk()
root.title('Main Server Hub')
root.geometry("800x600")
frame1 = Frame(root)
frame1.pack()

#INITAL
def Reload():
    try:
        data = client_socket.recv(1024).decode()
        ACS.insert(END, data + '\n')
    except:
        print("No Message.")
def SendCom():
    try:
        global message
        message = ACR.get()
        client_socket.send(message.encode())
        sleep(.2)
        data = client_socket.recv(1024).decode()
        ACS.insert(END, data + '\n')
    except:
        print("Message not send.")
        
def NewTab():
    SEE.destroy()
    SEB.destroy()
    SET.destroy()
    SE.destroy()

def SEBcom():
    global client_socket
    global Ip
    Ip = str(SE.get())
    print(Ip)

    #connecting
    try:
        host = Ip
        port = 20007
        client_socket = socket.socket()
        client_socket.connect((host, port))
        client_socket.setblocking(False)

        NewTab()
        Open()
        
    #If Failed
    except:
        SEE.delete("1.0", END)
        SEE.insert(END, "Failed Connection.")
    
SEE = Text(root, width = 25, height = 2)
SEE.place(relx=.5, rely=.7,anchor= CENTER)

SEB = Button(root, width = 10, text="Connect", command=SEBcom)
SEB.place(relx=.7, rely=.5,anchor= CENTER)

SET = Label(root, text="What IP would you like to connect to?", font=('Times New Roman', 25, 'bold'))
SET.place(relx=.5, rely=.43,anchor= CENTER)

SE = Entry(root, width = 35)
SE.place(relx=.5, rely=.5,anchor= CENTER)

#SECOND TAB

def Open():
    global ACS
    global ACRL
    global ACR
    ACT = Label(root, text=("Active connection to: " + Ip))
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
    
root.mainloop()


#message = input(" -> ")
        #while message.lower().strip() != 'bye':
            #client_socket.send(message.encode())
            #data = client_socket.recv(1024).decode()
            
            #print('Received from server: '+ data)
                  
            #message = input(" -> ")
                  
        #client_socket.close()

def client_program():
    host = '192.168.1.105'
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
