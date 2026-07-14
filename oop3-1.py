# 公開與與私有化

class PartyMember:
    def __init__(self, name, hp, mp):
        # __ 兩條底線的屬性, 在 python 中是私有化的寫法
        self.__hp = hp
        self.__mp = mp
        self.name = name

    def get_hp(self):
        return self.__hp
    def get_damage(self, damage: int):
        self.__hp -= damage


hero = PartyMember("勇者", 100, 100)
print(hero.name)
# print(hero.__hp) # 私有化的屬性不能直接取用
print(hero.get_hp())

hero.get_damage(1)
print(hero.get_hp())