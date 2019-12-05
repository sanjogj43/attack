'''
import random

class Enemy:
    hp = 200

    def __init__(self, atkl, atkh):
        self.atkl = atkl
        self.atkh = atkh

    def getAtk(self):
        print(self.atkl)

    def getHp(self):
        print("HP is", self.hp)


enemy1 = Enemy(40, 50)
enemy1.getAtk()
enemy1.getHp()

enemy2 = Enemy(60, 80)
enemy2.getAtk()


playerhp = 260
enemyatkl = 60
enemyatkh = 80

while playerhp > 0:
    dmg = random.randrange(enemyatkl,enemyatkh)
    playerhp = playerhp - dmg

    if playerhp <=30:
        playerhp = 30

    print("Enemy strikes for ", dmg, " points of damage. Current HP is ", playerhp)
    if playerhp > 30:
        continue

    print("You have low health, you have been teleported to hospital.")
    break

'''
