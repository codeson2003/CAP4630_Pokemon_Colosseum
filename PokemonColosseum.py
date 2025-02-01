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
print(f"Coin toss goes to ----- Team {coin_toss_result} to start the attack!")

nextUp = coin_toss_result
user = user_pokemon.pop(0)
opponent = opponent_pokemon.pop(0)
remainingMoves = list()
while len(opponent_pokemon) != -1 or len(user_pokemon) != -1:

    #print(f"\n{user} health: {manager.health(user)}, {opponent} health: {manager.health(opponent)}\n")


    if nextUp == playerName:
        manager.menu(user)
        attack = int(input(f"Team {playerName}'s choice: "))-1

        while attack + 1 < 1 or attack + 1 > manager.teamrocketattack(user):
            print(f"Invalid input! Input must be in the range 1-{manager.teamrocketattack(user)}")
            attack = int(input(f"Team {playerName}'s choice: "))-1
        print()
        while remainingMoves.count(attack) > 0:
            print(f"You've already used that attack, pick again!")
            attack = int(input(f"Team {playerName}'s choice: "))-1
        remainingMoves.append(attack)
        damage = manager.damage(manager.getAttack(user, attack), user, opponent)
        print(f"{user} cast '{manager.getAttack(user,attack)}' to {opponent}")
        print(f"Damage to {opponent} is {damage} points.")
        manager.apply_damage(opponent, damage)
        
    elif nextUp == "Rocket":
        rocketAttack = random.randint(1, manager.teamrocketattack(opponent)) - 1
        print(f"\nTeam Rocket's {opponent} cast '{manager.getAttack(opponent,rocketAttack)}' to {user}")
        
        damage = manager.damage(manager.getAttack(opponent, rocketAttack), opponent, user)
        print(f"Damage to {user} is {damage} points.")
        manager.apply_damage(user, damage)
    
    
    if manager.health(user) <= 0:
        print(f"Now {opponent} has {manager.health(opponent)} HP, and {user} faints back to poke ball.")
        if len(user_pokemon) == 0:
            print(f"\nAll of Team {playerName}'s Pokemon fainted, and Team Rocket prevails!")
            break
        user = user_pokemon.pop(0)
        print(f"\nNext for Team {playerName}, {user} enters battle!")
        remainingMoves = list()

    elif manager.health(opponent) <= 0:
        print(f"Now {opponent} faints back to pokeball, and {user} has {manager.health(user)} HP.")
        if len(opponent_pokemon) == 0:
            print(f"\nAll of Team Rocket’s Pokemon fainted, and Team {playerName} prevails!")
            break
        opponent = opponent_pokemon.pop(0)
        print(f"\nNext for Team Rocket, {opponent} enters battle!")

    else:
        print(f"Now {opponent} has {manager.health(opponent)} HP, and {user} has {manager.health(user)} HP.")
    nextUp = playerName if nextUp == "Rocket" else "Rocket"



