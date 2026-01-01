# --- Day 4: Printing Department ---
# You ride the escalator down to the printing department. They're clearly getting ready for Christmas; they have lots of large rolls of paper everywhere, and there's even a massive printer in the corner (to handle the really big print jobs).
# 
# Decorating here will be easy: they can make their own decorations. What you really need is a way to get further into the North Pole base while the elevators are offline.
# 
# "Actually, maybe we can help with that," one of the Elves replies when you ask for help. "We're pretty sure there's a cafeteria on the other side of the back wall. If we could break through the wall, you'd be able to keep moving. It's too bad all of our forklifts are so busy moving those big rolls of paper around."
# 
# If you can optimize the work the forklifts are doing, maybe they would have time to spare to break through the wall.
# 
# The rolls of paper (@) are arranged on a large grid; the Elves even have a helpful diagram (your puzzle input) indicating where everything is located.
# 
# For example:
# 
# ..@@.@@@@.
# @@@.@.@.@@
# @@@@@.@.@@
# @.@@@@..@.
# @@.@@@@.@@
# .@@@@@@@.@
# .@.@.@.@@@
# @.@@@.@@@@
# .@@@@@@@@.
# @.@.@@@.@.
# The forklifts can only access a roll of paper if there are fewer than four rolls of paper in the eight adjacent positions. If you can figure out which rolls of paper the forklifts can access, they'll spend less time looking and more time breaking down the wall to the cafeteria.
# 
# In this example, there are 13 rolls of paper that can be accessed by a forklift (marked with x):
# 
# ..xx.xx@x.
# x@@.@.@.@@
# @@@@@.x.@@
# @.@@@@..@.
# x@.@@@@.@x
# .@@@@@@@.@
# .@.@.@.@@@
# x.@@@.@@@@
# .@@@@@@@@.
# x.x.@@@.x.
# Consider your complete diagram of the paper roll locations. How many rolls of paper can be accessed by a forklift?

class Jour4:
    def __init__(self, input):
        self.input = input # on créé l'objet avec son input
    def resoudre_probleme(self): # partie 1
        resultat = 0
        for i in range(len(self.input)): # pour chaque ligne
            for j in range(len(self.input[i])): # pour chaque colonne
                if self.input[i][j] == '@': # si on trouve un rouleau de papier
                    compteur_adjacent = 0 # on initialise le compteur de rouleaux adjacents
                    for x in range(-1,2): # on regarde les 8 positions adjacentes
                        for y in range(-1,2): 
                            if (x != 0 or y != 0): # on n'inclut pas la position centrale
                                if 0 <= i+x < len(self.input) and 0 <= j+y < len(self.input[i]): # on vérifie qu'on ne sort pas des limites
                                    if self.input[i+x][j+y] == '@':
                                        compteur_adjacent += 1
                    if compteur_adjacent < 4:
                        resultat += 1
    # partie 2 (erronée)
    def boucle_de_base(self): 
        resultat = 0
        for i in range(len(self.input)): # pour chaque ligne
            for j in range(len(self.input[i])): # pour chaque colonne
                if self.input[i][j] == '@': # si on trouve un rouleau de papier
                    compteur_adjacent = 0 # on initialise le compteur de rouleaux adjacents
                    for x in range(-1,2): # on regarde les 8 positions adjacentes
                        for y in range(-1,2): 
                            if (x != 0 or y != 0): # on n'inclut pas la position centrale
                                if 0 <= i+x < len(self.input) and 0 <= j+y < len(self.input[i]): # on vérifie qu'on ne sort pas des limites
                                    if self.input[i+x][j+y] == '@':
                                        compteur_adjacent += 1
                    if compteur_adjacent < 4:
                        resultat += 1
                        self.input[i] = f"{self.input[i][:j]}x{self.input[i][j+1:]}" # on marque le rouleau comme accessible
        return resultat
    def resoudre_probleme_partie2(self):
        if self.boucle_de_base() == 0:
            return 0
        return self.boucle_de_base() + self.resoudre_probleme_partie2()
# préparation des données
with(open('Jour 4/input_jour4exemple.txt', 'r') as f):
    input_jour4 = Jour4(f.read().splitlines()) # sortie : ['..@@.@@@@.', '@@@.@.@.@@', '@@@@@.@.@@', '@.@@@@..@.', '@@.@@@@.@@', '.@@@@@@@.@', '.@.@.@.@@@', '@.@@@.@@@@', '.@@@@@@@@.', '@.@.@@@.@.']
print(input_jour4.resoudre_probleme_partie2())
# sortie attendue : 43
# sortie réelle : 9