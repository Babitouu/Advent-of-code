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
            indice_batterie_2max = 0 # indice de la deuxième batterie avec le voltage max
            for i in range(1,len(banks)): # on cherche la première batterie avec le plus grand voltage
                if int(banks[i]) > int(batterie_max) : # si on trouve une batterie avec un voltage plus grand
                    batterie_max = banks[i] # on met à jour la batterie max
                    indice_batterie_max = i # on met à jour l'indice de la batterie max pour éviter de la prendre deux fois
            batterie_2max = banks[0] if indice_batterie_max != 0 else banks[1] # on initialise la deuxième batterie max
            for j in range(1,len(banks)): 
                if j != indice_batterie_max and int(banks[j]) > int(batterie_2max): # si on trouve une batterie avec un voltage plus grand et que ce n'est pas la première batterie max
                    batterie_2max = banks[j]
                    indice_batterie_2max = j  # on met à jour l'indice de la deuxième batterie max
            if indice_batterie_max > indice_batterie_2max: # on s'assure que la première batterie max est avant la deuxième dans la liste pour former le bon nombre
                batterie_max, batterie_2max = batterie_2max, batterie_max
            volt_max += int(batterie_max + batterie_2max) # on ajoute le voltage des deux batteries (pas mathématiquement) max au voltage total
# j'ai un problème futur moi, le dernier exemple donné dans le texte (818181911112111) ne fonctionnera pas car il faut prendre 9 et 2 or ici on prendra 8 et 9 
        return volt_max
# On prépare les données
with open('Jour 3/input_jour3.txt', 'r') as f: 
    input_jour3 = Jour3(f.read().splitlines())
print(input_jour3.resoudre_probleme())
