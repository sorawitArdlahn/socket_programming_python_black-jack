class Player:
    # Attribute
    def __init__(self) -> None:
        self.__name: str = ""
        self.__hand: list[int] = []
        self.__score: int = 0
        self.__is_stay: bool = False
        self.__is_win: bool = False

    # Setter
    def set_name(self, name: str) -> None:
        self.__name = name

    def add_into_hand(self, card: str) -> None:
        self.__hand.append(card)

    def stay(self) -> None:
        self.__is_stay = True

    def win(self) -> None:
        self.__is_win = True
        
    def calculate_score(self) -> int:
        score = 0
        for number in self.__hand:
            score += int(number)
        self.__score = score
    # Getter
    def get_name(self) -> str:
        return self.__name

    def check_win(self) -> bool:
        return self.__is_win

    def check_stay(self) -> bool:
        self.calculate_score()
        return self.__is_stay

    def get_all_hand(self) -> list[int]:
        return self.__hand

    def get_score(self) -> int:
        return self.__score
