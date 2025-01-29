#Project 1, Pokemon Game
#1/15/2025

from Pokemon import Pokemon

import csv
import ast
import random
import os

print("\nWelcome to Pokemon Colosseum!\n")
playerName = input("Enter Player Name: ")
print()

manager = Pokemon()
manager.pokemon_data = manager.load_pokemon('pokemon-data.csv')
manager.move_data = manager.load_moves('moves-data.csv')

opponent_pokemon = random.sample(list(manager.pokemon_data.keys()), 3)
print("Team Rocket enters with ", end='')
for i,key in enumerate(opponent_pokemon):
    if i == 2:
        print(key + '.\n')
    else:
        print(key + ', ', end='')


remaining_pokemon = list(set(manager.pokemon_data.keys()) - set(opponent_pokemon))
user_pokemon = random.sample(remaining_pokemon, 3)

print(f"Team {playerName} enters with ", end='')
for i,key in enumerate(user_pokemon):
    if i == 2:
        print(key + '.\n')
    else:
        print(key + ', ', end='')

#1 is heads, 2 is tails
coin_toss = random.randint(1,2)
coin_toss_result = "Rocket" if coin_toss == 2 else playerName
print("Let the battle begin!")
print(f"Coin toss goes to ----- Team {coin_toss_result} to start the attack!\n")

nextUp = coin_toss_result
i = 1
while len(opponent_pokemon) != 0 and len(user_pokemon) != 0:
    user = user_pokemon[0]
    opponent = opponent_pokemon[0]

    if nextUp == playerName:
        manager.menu(user)
        attack = input(f"Team {playerName}'s choice: ")
        print()
    elif nextUp == "Rocket":
        rocketAttack = random.randint(1, manager.teamrocketattack(opponent))
        print(f"Team Rocket's {opponent} cast {rocketAttack} to {user}")

    
    print(manager.damage("Karate Chop", "A", "B"))
    
    nextUp = playerName if nextUp == "Rocket" else "Rocket"
    
    i+=1
    if i == 10:
        break

    
    

print("end")


