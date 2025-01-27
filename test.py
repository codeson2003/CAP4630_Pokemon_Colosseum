#Project 1, Pokemon Game
#1/15/2025

import csv
import ast
import random
import os

project_dir = os.path.dirname(os.path.abspath(__file__))
pokemon_filename = os.path.join(project_dir,'pokemon-data.csv')
header = []
pokemon_moves = {}
with open(pokemon_filename) as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    header = next(reader)
    for row in reader:
        moves=''
        end_of_moves=False
        for s in row:
            if s[0]=='[':
                end_of_moves = True
                moves = s
            elif end_of_moves == True:
                moves += ','+s
                if s[-1] == ']':
                    end_of_moves = False
        #print(moves)
        pokemon_moves[row[0]] = ast.literal_eval(moves) # string to list
for key in pokemon_moves:
    print(key, "moves: ", pokemon_moves[key])

moves_data_filename = os.path.join(project_dir,'moves-data.csv')
with open(moves_data_filename) as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    header = next(reader)
    for row in reader:
        moves=''
        end_of_moves=False
        for s in row:
            print(s + ",",end='')
        print("\n")
        
print("Welcome to Pokemon Colosseum!")
playerName = input("Enter Player Name: ")
random_pokemon = random.sample(list(pokemon_moves.keys()), 3)
for key in random_pokemon:
    print(key + ' ', end='')

print()

remaining_pokemon = list(set(pokemon_moves.keys()) - set(random_pokemon))
opponent_pokemon = random.sample(remaining_pokemon, 3)

for key in opponent_pokemon:
    print(key + ' ', end='')

print()



