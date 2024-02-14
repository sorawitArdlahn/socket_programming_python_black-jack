import socket

HEADER = 64
PORT = 5050
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)

class Client:
    # Attribute
    def __init__(self) -> None:
        self.__name = ''
        self.__serv_msg = ''
        self.__client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Setter
    def connect(self):
        self.__client.connect(ADDR)
        self.__serv_msg = self.__client.recv(2048).decode(FORMAT)
        self.__sendmsg(f"connected by {self.__name}")
        
    def action(self, action:str):
        self.__send_action(f"{self.__name} {action}")
    
    def disconnect(self):
        self.__sendmsg(f"{self.__name} !DISCONNECT")
        self.__sendmsg(DISCONNECT_MESSAGE)
        print("💻 Server Say: <!SERVER DISCONNECT>")
        
    def __sendmsg(self,message):
        message = message.encode(FORMAT)
        message_length = len(message)
        send_length = str(message_length).encode(FORMAT)
        send_length += b' ' * (HEADER - len(send_length))
        self.__client.send(send_length)
        self.__client.send(message)
        
    def __send_action(self,message):
        message = message.encode(FORMAT)
        message_length = len(message)
        send_length = str(message_length).encode(FORMAT)
        send_length += b' ' * (HEADER - len(send_length))
        self.__client.send(send_length)
        self.__client.send(message)
        self.__serv_msg = self.__client.recv(2048).decode(FORMAT)
        #print(self.__serv_msg)
        
    
    def set_username(self, name:str):
        self.__name = name
        
    def get_serv_msg(self):
        return self.__serv_msg
    