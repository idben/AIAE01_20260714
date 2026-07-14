# 用撲克牌的例子做抽象化的練習
import random

# 替代型別
# type Card = tuple[str, str]
Card = tuple[str, str]

class Deck:
    SUITS: list[str] = ["黑桃", "紅心", "方塊", "梅花"]
    RANKS: list[str] = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

    def __init__(self):
        self.__cards: list[Card] = []
        self.create_deck()

    def create_deck(self) -> None:
        self.__cards = []
        for suit in self.SUITS:
            for rank in self.RANKS:
                self.__cards.append((suit, rank))
    
    def shuffle_deck(self) -> None:
        random.shuffle(self.__cards)
    
    def deal_card(self) -> Card | None:
        if len(self.__cards) == 0:
            return None
        return self.__cards.pop()
    
    def get_cards_num(self) -> int:
        return len(self.__cards)


# 建立牌局
deck01 = Deck()
# 洗牌
deck01.shuffle_deck()
# 發一張牌
# index = 1
# card01 = deck01.deal_card()
# print(card01)
# print(deck01.get_cards_num())
# print(f"發第 {index} 張牌，花色是 {card01}，剩下 {deck01.get_cards_num()} 張牌")

for _, index in enumerate(range(10), 1):
    card01 = deck01.deal_card()
    print(f"發第 {index} 張牌，花色是 {card01}，剩下 {deck01.get_cards_num()} 張牌")

# index = 2
# card01 = deck01.deal_card()
# print(f"發第 {index} 張牌，花色是 {card01}，剩下 {deck01.get_cards_num()} 張牌")

# index = 3
# card01 = deck01.deal_card()
# print(f"發第 {index} 張牌，花色是 {card01}，剩下 {deck01.get_cards_num()} 張牌")