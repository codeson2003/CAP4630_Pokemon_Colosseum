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
manager.load_pokemon('pokemon-data.csv')
manager.load_moves('moves-data.csv')

opponent_pokemon = random.sample(list(manager.pokemon_moves.keys()), 3)
print("Team Rocket enters with ", end='')
for i,key in enumerate(opponent_pokemon):
    if i == 2:
        print(key + '.\n')
    else:
        print(key + ', ', end='')


remaining_pokemon = list(set(manager.pokemon_moves.keys()) - set(opponent_pokemon))
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

while len(opponent_pokemon) != 0 and len(user_pokemon) != 0:

    if coin_toss_result == "Rocket":
        print("YEET")
    elif coin_toss_result == playerName:
        print("yeet")
    print(manager.damage("Karate Chop", "A", "B"))
    opponent_pokemon.pop(0)

    coin_toss_result = "irrelevant"

    
    

print("end")


