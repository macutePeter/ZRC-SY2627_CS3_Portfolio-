class Hero:
    def __init__(self, name, hp):
        # Name and health
        self.name = name
        self.hp = hp

    def take_damage(self, amount):
        # Subtract `amount` from this hero's health
        self.hp -= amount



miku = Hero("Miku", 100)
Gumi = Hero("Gumi", 100)

miku.take_damage(39)

print(f"Miku's health: {miku.hp}.")    # Expected: 61
print(f"Gumi's health: {Gumi.hp}.")   # Expected: 100
