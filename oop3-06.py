# 封裝練習: 以悠遊卡為範例

class YoyoCard:
    def __init__(self, id, name, initial_balance):
        self.__id: str = id
        self.__name: str = name
        self.__balance: int = initial_balance
    def get_id(self) -> str:
        return self.__id
    def get_name(self) -> str:
        return self.__name
    def get_balance(self) -> int:
        return self.__balance
    def top_up(self, amount: int) -> None:
        if amount <= 0:
            raise ValueError("儲值金額必需大於零")
        self.__balance += amount
    def deduct(self, amount: int) -> None:
        if amount <= 0:
            raise ValueError("扣款金額必需大於零")
        if amount > self.__balance:
            raise ValueError("餘額不足")
        self.__balance -= amount

def try_deduct(title, money):
    print(f"{title}: {money}")
    try:
        card01.deduct(money)
    except ValueError as e:
        print("扣款失敗")
        print(e)
    else:
        print("扣款成功")
    finally:
        print(f"卡片餘額是: {card01.get_balance()}")

# 建立卡片實體
card01 = YoyoCard("s00001", "王小明", 1000)
# 取得卡片 id
print(f"卡片編號是: {card01.get_id()}")
# 取得卡片持有者
print(f"卡片持有者是: {card01.get_name()}")
# 取得卡片餘額
print(f"卡片餘額是: {card01.get_balance()}")
# 儲值
print("儲值金額: 500")
card01.top_up(500)
print(f"卡片餘額是: {card01.get_balance()}")
# 扣款
try_deduct("搭公車", 18)
try_deduct("搭高鐵", 130)
try_deduct("買 mac mini", 24900)
