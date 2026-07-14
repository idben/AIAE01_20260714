# 公開與與私有化

class PartyMember:
    def __init__(self, name, hp, mp):
        # __ 兩條底線的屬性, 在 python 中是私有化的寫法
        self.__hp = hp
        self.__mp = mp
        self.name = name

    def get_hp(self):
        return self.__hp


hero = PartyMember("勇者", 100, 100)
print(hero.name)
print(hero.get_hp())