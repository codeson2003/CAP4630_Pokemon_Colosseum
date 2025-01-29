import csv
import ast
import random
import os

class Pokemon:

    def __init__(self):
        self.pokemon_data = {}
        self.moves_data = {}


    def load_pokemon(self, fileName):
        project_dir = os.path.dirname(os.path.abspath(__file__))
        pokemon_filename = os.path.join(project_dir,fileName)
        header = []
        pokemon_data = {}
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
                pokemon_data[row[0]] = ast.literal_eval(moves) # string to list
        #for key in pokemon_moves:
            #print(key, "moves: ", pokemon_moves[key])
        return pokemon_data   

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
                
            
    def damage(self, M,A,B):
        power = self.moves_data[M]['Power']
        random_val = random.uniform(0.5,1.0)
        return power * random_val
    
    def menu(self, pokemon):
        print(f"\nChoose the move for {pokemon}:")
        for i,move in enumerate(self.pokemon_data[pokemon], start=1):
            print(f"{i}. {move}")
        print()
    
    def teamrocketattack(self, pokemon):
        return len(self.pokemon_data[pokemon])
    
        



    