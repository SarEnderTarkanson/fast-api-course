from Enemy import *
from Zombie import *
from Ogre import *

def battle(e: Enemy):
    e.talk()
    e.attack()

zombie = Zombie(health_points=10, attack_damage=1)
ogre = Ogre(20,3)

battle(zombie)
battle(ogre)