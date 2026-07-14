class ArenaFighter:
    def __init__(self, name: str, stamina: int, focus: int) -> None:
        self.name = name
        self.__stamina = stamina
        self.__focus = focus
        self.focus_points = focus * 5   # 企劃討論之後的公式
        self.hp = stamina * 50          # 企劃討論之後的公式

    def use_power_strike(
        self, target: "ArenaFighter", focus_cost: int, raw_damage: int
    ) -> None:
        if self.focus_points < focus_cost:
            raise Exception(f"{self.name} 不能使出強烈一擊")
        self.focus_points -= focus_cost
        print(f"{self.name} 對 {target.name} 使出強烈一擊，造成 {raw_damage + self.__focus} 傷害")
        target.take_hit(raw_damage + self.__focus)

    def take_hit(self, raw_damage: int) -> None:
        final_damage = raw_damage - self.__stamina
        if final_damage < 0:
            final_damage = 0
        self.hp -= final_damage

    def can_continue(self) -> bool:
        return self.hp > 0

hero = ArenaFighter("勇者", 8, 6)
print(f"{hero.name} 登場，hp 是 {hero.hp}，強烈一擊點是 {hero.focus_points}")
dragon = ArenaFighter("紅龍", 12, 3)
print(f"{dragon.name} 登場，hp 是 {dragon.hp}，強烈一擊點數是 {dragon.focus_points}")

hero.use_power_strike(dragon, 10, 40)

print(f"{hero.name} 的 hp 是 {hero.hp}")
print(f"{dragon.name} 的 hp 是 {dragon.hp}")