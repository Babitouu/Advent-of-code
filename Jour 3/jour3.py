#You descend a short staircase, enter the surprisingly vast lobby, and are quickly cleared by the security checkpoint. When you get to the main elevators, however, you discover that each one has a red light above it: they're all offline.

#"Sorry about that," an Elf apologizes as she tinkers with a nearby control panel. "Some kind of electrical surge seems to have fried them. I'll try to get them online soon."

#You explain your need to get further underground. "Well, you could at least take the escalator down to the printing department, not that you'd get much further than that without the elevators working. That is, you could if the escalator weren't also offline."

#"But, don't worry! It's not fried; it just needs power. Maybe you can get it running while I keep working on the elevators."

#There are batteries nearby that can supply emergency power to the escalator for just such an occasion. The batteries are each labeled with their joltage rating, a value from 1 to 9. You make a note of their joltage ratings (your puzzle input). For example:

#987654321111111
#811111111111119
#234234234234278
#818181911112111
#The batteries are arranged into banks; each line of digits in your input corresponds to a single bank of batteries. Within each bank, you need to turn on exactly two batteries; the joltage that the bank produces is equal to the number formed by the digits on the batteries you've turned on. For example, if you have a bank like 12345 and you turn on batteries 2 and 4, the bank would produce 24 jolts. (You cannot rearrange batteries.)

#You'll need to find the largest possible joltage each bank can produce. In the above example:

#In 987654321111111, you can make the largest joltage possible, 98, by turning on the first two batteries.
#In 811111111111119, you can make the largest joltage possible by turning on the batteries labeled 8 and 9, producing 89 jolts.
#In 234234234234278, you can make 78 by turning on the last two batteries (marked 7 and 8).
#In 818181911112111, the largest joltage you can produce is 92.
#The total output joltage is the sum of the maximum joltage from each bank, so in this example, the total output joltage is 98 + 89 + 78 + 92 = 357.

#There are many batteries in front of you. Find the maximum joltage possible from each bank; what is the total output joltage?
class Jour3:
    def __init__(self, input):
        self.input = input # on créé l'objet avec son input
    def resoudre_probleme(self):
        volt_max = 0 # initialisation du voltage max
        for banks in self.input: # pour chaque banque de batteries
            batterie_max = banks[0]
            
            indice_batterie_max = 0 # indice de la batterie avec le voltage max nécessaire pour chercher la deuxième batterie correctement
            
            for i in range(1,len(banks)-1): # on cherche la première batterie avec le plus grand voltage jusqu'à l'avant dernière batterie
                
                if int(banks[i]) > int(batterie_max) : # si on trouve une batterie avec un voltage plus grand
                    batterie_max = banks[i] # on met à jour la batterie max
                    indice_batterie_max = i # on met à jour l'indice de la batterie max pour éviter de la prendre deux fois
            
            batterie_2max = banks[indice_batterie_max+1] # on initialise la deuxième batterie max
            
            for j in range(indice_batterie_max+2,len(banks)): 
                
                if int(banks[j]) > int(batterie_2max): # si on trouve une batterie avec un voltage plus grand
                    batterie_2max = banks[j] # on met à jour la deuxième batterie max
            
            volt_max += int(batterie_max + batterie_2max) # on ajoute le voltage des deux batteries (pas mathématiquement) max au voltage total
        return volt_max
# On prépare les données
#with open('Jour 3/input_jour3.txt', 'r') as f: 
    #input_jour3 = Jour3(f.read().splitlines())
#print(input_jour3.resoudre_probleme())

class Jour3_part2:
    def __init__(self, input):
        self.input = input # on créé l'objet avec son input
    
    def resoudre_probleme(self): # partie 1
        volt_max = 0 # initialisation du voltage max
        
        for banks in self.input:
            batterie_max = banks[0]
            nombre_batteries_restantes = 12
            indice_ancienne_batterie_max = 1
            volt_bank_max = ''
            while nombre_batteries_restantes > 0: # on cherche 12 batteries
                
                for j in range(indice_ancienne_batterie_max, len(banks)-nombre_batteries_restantes): # on commence à chercher après la dernière batterie prise et on s'arrête avant pour garder de la place pour les autres batteries
                
                    if int(banks[j]) >= int(batterie_max): 
                        batterie_max = banks[j]
                
                nombre_batteries_restantes -= 1
                indice_ancienne_batterie_max = banks.index(batterie_max) + 1
                volt_bank_max += batterie_max # on ajoute la batterie max au voltage de la banque (pas mathématiquement)
                batterie_max = banks[indice_ancienne_batterie_max] # on réinitialise la batterie max pour la prochaine recherche
            volt_max += int(volt_bank_max) # on ajoute le voltage de la banque au voltage total
        return volt_max
# partie 2 (erronée)
    def resoudre_probleme2(self):
        volt_max = 0
        for banks in self.input:
            volt_bank_max = ''
            nombre_batteries_restantes = 12
            batterie_max = banks[0]
            indice_ancienne_batterie_max = 0
            while nombre_batteries_restantes > 0:
                for i in range(indice_ancienne_batterie_max,len(banks)-nombre_batteries_restantes):

                    if int(banks[i]) > int(batterie_max):
                        batterie_max = banks[i]

                nombre_batteries_restantes -= 1
                indice_ancienne_batterie_max = banks.index(batterie_max) + 1
                volt_bank_max += batterie_max
            volt_max += int(volt_bank_max)
        return volt_max
# On prépare les données
with open('Jour 3/input_jour3part2.txt', 'r') as f: 
    input_jour3 = Jour3_part2(f.read().splitlines())
print(input_jour3.resoudre_probleme2())