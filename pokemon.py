class pokemon:
    def __init__ (self, name, hp, m1, m2):
        self.name = name
        self.hp = hp
        self.m1 = m1
        self.m2 = m2

class move:
    def __init__(self, name, dmg):
        self.name = name
        self.dmg = dmg

splash = move("Splash", 0)
scratch = move("Scratch", 5)
dp = move("Dragon Pulse", 50)
aw = move("Ancient Power", 60)

magikarp = pokemon("Magikarp", 10, splash, scratch)
rayquaza = pokemon("Rayquaza", 200, dp, aw)

chance = 0
while (magikarp.hp > 0 and rayquaza.hp > 0):
    question = "Do you want to use 1." + rayquaza.m1.name + " or 2." + rayquaza.m2.name
    m = int(input(question))
    if (m == 1):
        magikarp.hp = magikarp.hp - rayquaza.m1.dmg
    else:
        magikarp.hp = magikarp.hp - rayquaza.m2.dmg

print("Magikarp has fainted")

# print(magikarp.m1.name)
# print(magikarp.m2.dmg)