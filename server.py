import socket
import threading
from model.dealer import Dealer

HEADER = 64
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "!DISCONNECT"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")
    conn.send(b'Hello, client! This is a message from the server.')
    #conn.send(f"Dealer Hand: {dealer.get_all_hand()[0]} [HIDE]".encode(FORMAT))

    is_connected = True
    while is_connected:
        message_length = conn.recv(HEADER).decode(FORMAT)
        if message_length:
            message_length = int(message_length)
            message = conn.recv(message_length).decode(FORMAT)
            if message == DISCONNECT_MESSAGE:
                is_connected = False
                print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 2}")
                if (threading.active_count() - 2) == 0:
                    dealer.reset_game()
            else:
                print(f"[{addr}] {message}")
                action = (str(message).split())[1]
                if action == "hit":
                    conn.send(f"OK,{dealer.give_card()}".encode(FORMAT))
                elif action == "stay":
                    print(f"Dealer Hand: {dealer.get_all_hand()}, Dealer Score: {dealer.get_score()}")
                    conn.send(f"OK_{dealer.get_all_hand()}_{dealer.get_score()}".encode(FORMAT))
                elif action == "Win" or action == "Loss":
                    conn.send("Game Over".encode(FORMAT))
                elif action == "start":
                    conn.send(f"Dealer Hand: {dealer.get_all_hand()[0]} [HIDE]".encode(FORMAT))
                # conn.send("Message received".encode(FORMAT))


def start():
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")

dealer = Dealer()
print("[STARTING] server is starting...")
start()
