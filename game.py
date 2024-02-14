from network.client import Client
from model.player import Player
from model.dealer import Dealer

import time

# Register Player
player_name = str(input("📜 Enter Player's Name: "))

player = Player()
player.set_name(player_name)
dealer = Dealer()

# Server Connecting
client_system = Client()
client_system.set_username(player.get_name())
client_system.connect()
print(f"\n💻 Server Say: {client_system.get_serv_msg()}")
time.sleep(2)
print("> Do you want to play <yes> or <no>")

is_play = False

while True:
    choice = str(input("type: ")).lower()
    if choice == "yes":
        client_system.action("start")
        print(f"\n🪙  Welcome '{player_name}' To The Black Jack Game 🪙\n")
        time.sleep(2)
        dealer_hand = client_system.get_serv_msg()
        print(f"🤵🏻 {dealer_hand}")
        print(f"'{player.get_name()}' Hand: {player.get_all_hand()}")
        is_play = True
        break
    elif choice == "no":
        client_system.disconnect()
        break
    
# Play game
while is_play:
    print("\n>🎯 type <hit> to add more card: ")
    print(">🪑 type <stay> if you full: ")
    print(">💨 type <exit> to exit game: ")
    msg = str(input("type something?: "))
    time.sleep(1)
    if msg == "exit":
        client_system.disconnect()
        is_play = False

    elif msg == "hit":
        client_system.action(msg)
        status_code = client_system.get_serv_msg().split(",")[0]
        card = client_system.get_serv_msg().split(",")[1]
        player.add_into_hand(card)
        player.calculate_score()
        print(f"💻 Server Say: <{status_code}>")
        time.sleep(1)
        print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
        print(f"🤵🏻 {dealer_hand}")
        print(f"\n'{player.get_name()}' Hand: {player.get_all_hand()}")
        print(f"'{player.get_name()}' Score: {player.get_score()}")

    elif msg == "stay":
        client_system.action(msg)
        player.calculate_score()
        status_code = client_system.get_serv_msg().split("_")[0]
        cards = client_system.get_serv_msg().split("_")[1]
        score = int(client_system.get_serv_msg().split("_")[2])
        dealer.add_into_hand(cards)
        dealer.set_score(score)
        print(f"💻 Server Say: <{status_code}>")
        time.sleep(1)
        print("=========================================================")
        print(f"\nDealer Hand: {dealer.get_all_hand()}")
        print(f"'{player.get_name()}' Hand: {player.get_all_hand()}\n")

        print(f"Dealer Score: {dealer.get_score_directly()}")
        print(f"'{player.get_name()}' Score: {player.get_score()}")

        if (
            ((player.get_score() > dealer.get_score_directly())
            and (player.get_score() <= 21))
            or (dealer.get_score_directly() >= 21)
        ):
            player.win()
            print(f"🎉 Congratulation '{player.get_name()}' You Win!!\n")
            client_system.action("Win")
        else:
            print(f"😭 Unlucky '{player.get_name()}' You Loss!!\n")
            client_system.action("Loss")
        print("=========================================================")
        client_system.disconnect()
        is_play = False
        
time.sleep(1)
print("\nTHANK YOU SEE YOU LATER...")
