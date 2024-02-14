import random
class Dealer:
    # Attribute
    def __init__(self) -> None:
        self.__hand: list[int] = []
        self.__score: int = 0
        self.__set_game()
        
    # Setter
    def __set_game(self) -> None:
        for i in range(0,2):
            card = self.give_card()
            self.__hand.append(card)
    
    def reset_game(self) -> None:
        self.__hand = []
        self.__score = 0
        self.__set_game()
        
    def add_into_hand(self, cards:list[int]):
        self.__hand = cards
        
    def set_score(self, score:int):
        self.__score = score
                
    # Getter
    def give_card(self) -> int:
        rand = str(random.randrange(0,12,1))
        return rand
    
    def get_score(self) -> int:
        self.__score = 0
        for number in self.__hand:
            self.__score += int(number)
        return self.__score
    
    def get_all_hand(self) -> list[int]:
        return self.__hand
    
    def get_score_directly(self) -> int:
        return self.__score