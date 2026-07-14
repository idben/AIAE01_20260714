# 複數 class 的一起使用
class Item:
    def __init__(self, name, amount, price):
        self.name = name
        self.amount = amount
        self.price = price

class Cart:
    def __init__(self, name):
        self.name = name
        self.cart: list[Item] = []
    def add_cart(self, item: Item):
        self.cart.append(item)
    def get_total(self):
        total_money = 0
        for item in self.cart:
            total_money += item.price * item.amount
        return total_money

cart01 = Cart("小明")
cart01.add_cart(Item("mbp", 1, 48000))
print(cart01.get_total())