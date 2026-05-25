from Enemy import *

zombie = Enemy(type_of_enemy="Zombie", health_points=10, attack_damage=1)
zombie.type_of_enemy = "Ogre"

print(zombie.attack())