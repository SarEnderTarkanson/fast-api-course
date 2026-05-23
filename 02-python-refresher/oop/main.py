from Enemy import *

enemy = Enemy()
enemy.type_of_enemy = 'zombie'


print(f'{enemy.type_of_enemy}'
      f' has {enemy.health_points} health points and '
      f'{enemy.attack_damage} attack damage')