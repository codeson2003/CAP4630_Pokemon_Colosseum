import csv
import ast
import random
import os
import math
import numpy as np

class Pokemon:

    types = ["Normal", "Fire", "Water", "Electric", "Grass", "Others"]

    effectivenessMatrix = np.array([
        [1, 1, 1, 1, 1],
        [1, 0.5, 0.5, 1, 2],
        [1, 2, 0.5, 1, 0.5],
        [1, 1, 2, 0.5, 0.5],
        [1, 0.5, 2, 1, 0.5],
        [1, 1, 1, 1, 1],   
    ])

    def __init__(self):
        self.pokemon_data = {}
        self.moves_data = {}


    def load_pokemon(self, fileName):
        project_dir = os.path.dirname(os.path.abspath(__file__))
        pokemon_filename = os.path.join(project_dir,fileName)
        
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
                self.pokemon_data[row[0]] = {
                    "Type": row[1],
                    "HP": int(row[2]),
                    "current_health": int(row[2]),
                    "Attack": int(row[3]),
                    "Defense": int(row[4]),
                    "height": int(row[5]),
                    "weight": int(row[6]),
                    "Moves": ast.literal_eval(moves) # string to list
                }
                
        #for key in pokemon_moves:
            #print(key, "moves: ", pokemon_moves[key])
        
        

    def load_moves(self, fileName):
        project_dir = os.path.dirname(os.path.abspath(__file__))
        moves_data_filename = os.path.join(project_dir,fileName)
        moves_data = {}
        with open(moves_data_filename) as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            header = next(reader)
            for row in reader:
                move_name = row[0]
                self.moves_data[move_name] = {
                    "Type": row[1],
                    "Category": row[2],
                    "Contest": row[3],
                    "PP": int(row[4]),
                    "Power": int(row[5]),
                    "Accuracy": None if row[6] == "None" else int(row[6])
                }
                #for s in row:
                    #print(s + ",",end='')
                #print("\n")
                
    #Parameters: Pokemon A performs move M on Pokemon B
    def damage(self, M,A,B):
        power = self.moves_data[M]['Power']
        attack = self.pokemon_data[A]['Attack']
        defense = self.pokemon_data[B]['Defense']
        stab = 1.5 if self.pokemon_data[A]['Type'] == self.moves_data[M]['Type'] else 1

        attack_type = self.moves_data[M]['Type'] if self.moves_data[M]['Type'] in self.types else "Others"
        defence_type = self.pokemon_data[B]['Type']
        efficiency = self.effectivenessMatrix[self.types.index(attack_type), self.types.index(defence_type)]

        random_val = random.uniform(0.5,1.0)

        """print(f"""
        power:         {power}
        attack:        {attack}
        defense:       {defense}
        stab:          {stab}
        attack_type:   {attack_type}
        defence_type:  {defence_type}
        efficiency:    {efficiency}
        random_val:    {random_val}
        """)
        """

        return math.ceil(power * (attack/defense) * stab * efficiency * random_val)
    

    def menu(self, pokemon):
    # Ensure there is a "Used" list for this Pokemon.
        if "Used" not in self.pokemon_data[pokemon]:
            self.pokemon_data[pokemon]["Used"] = [False] * len(self.pokemon_data[pokemon]["Moves"])
        
        # Check if all moves are used; if so, reset them.
        if all(self.pokemon_data[pokemon]["Used"]):
            print("All moves have been used. Resetting move usage.\n")
            self.pokemon_data[pokemon]["Used"] = [False] * len(self.pokemon_data[pokemon]["Moves"])
        
        print(f"\nChoose the move for {pokemon}:")
        for i, move in enumerate(self.pokemon_data[pokemon]["Moves"], start=1):
            status = " (N/A)" if self.pokemon_data[pokemon]["Used"][i-1] else ""
            print(f"{i}. {move}{status}")
        print()
    
    def teamrocketattack(self, pokemon):
        return len(self.pokemon_data[pokemon]['Moves'])
    
    def getAttack(self, pokemon, attackNum):
        index = int(attackNum)

        if "Used" not in self.pokemon_data[pokemon]:
            self.pokemon_data[pokemon]["Used"] = [False] * len(self.pokemon_data[pokemon]["Moves"])

        self.pokemon_data[pokemon]["Used"][index] = True

        return self.pokemon_data[pokemon]["Moves"][index]
    
    def health(self, pokemon):
        return self.pokemon_data[pokemon]['current_health']
    
    def apply_damage(self, pokemon, damage):
        self.pokemon_data[pokemon]['current_health'] -= damage
        if self.pokemon_data[pokemon]['current_health'] < 0:
            self.pokemon_data[pokemon]['current_health'] = 0
        
        



    