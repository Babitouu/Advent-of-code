# --- Day 2: Gift Shop ---
# You get inside and take the elevator to its only other stop: the gift shop. "Thank you for visiting the North Pole!" gleefully exclaims a nearby sign. You aren't sure who is even allowed to visit the North Pole, but you know you can access the lobby through here, and from there you can access the rest of the North Pole base.
#
# As you make your way through the surprisingly extensive selection, one of the clerks recognizes you and asks for your help.
#
# As it turns out, one of the younger Elves was playing on a gift shop computer and managed to add a whole bunch of invalid product IDs to their gift shop database! Surely, it would be no trouble for you to identify the invalid product IDs for them, right?
#
# They've even checked most of the product ID ranges already; they only have a few product ID ranges (your puzzle input) that you'll need to check. For example:
#
# 11-22,95-115,998-1012,1188511880-1188511890,222220-222224,
# 1698522-1698528,446443-446449,38593856-38593862,565653-565659,
# 824824821-824824827,2121212118-2121212124
# (The ID ranges are wrapped here for legibility; in your input, they appear on a single long line.)
#
# The ranges are separated by commas (,); each range gives its first ID and last ID separated by a dash (-).
#
# Since the young Elf was just doing silly patterns, you can find the invalid IDs by looking for any ID which is made only of some sequence of digits repeated twice. So, 55 (5 twice), 6464 (64 twice), and 123123 (123 twice) would all be invalid IDs.
#
# None of the numbers have leading zeroes; 0101 isn't an ID at all. (101 is a valid ID that you would ignore.)
#
# Your job is to find all of the invalid IDs that appear in the given ranges. In the above example:
#
# 11-22 has two invalid IDs, 11 and 22.
# 95-115 has one invalid ID, 99.
# 998-1012 has one invalid ID, 1010.
# 1188511880-1188511890 has one invalid ID, 1188511885.
# 222220-222224 has one invalid ID, 222222.
# 1698522-1698528 contains no invalid IDs.
# 446443-446449 has one invalid ID, 446446.
# 38593856-38593862 has one invalid ID, 38593859.
# The rest of the ranges contain no invalid IDs.
# Adding up all the invalid IDs in this example produces 1227775554.
#
# What do you get if you add up all of the invalid IDs?
#comment faire ? 
# - diviser la grande liste de nombre en sous listes qui seront nos intervalles ex : 11-22, 95-115, 998-1012... le premier élément sera une liste seule [11-22]
# - vérifier les doubles dans chaque intervalle 11-22 a deux chiffres double 11 et 22, 95-115 a un chiffre double 99...

class Jour_2_Part1:
    def __init__(self):
        self.invalid_ids = []  # Liste pour stocker les IDs invalides
    def trouver_id_invalide(self, input_data):
        ranges = input_data.strip().split(',')  # Diviser les intervalles par des virgules
        for r in ranges:
            start, end = map(int, r.split('-'))  # Diviser chaque intervalle en début et fin
            for num in range(start, end + 1):
                str_num = str(num)
                length = len(str_num)
                if length % 2 == 0:  # Vérifier si le nombre de chiffres est pair
                    half = length // 2
                    if str_num[:half] == str_num[half:]:  # Vérifier si les deux moitiés sont identiques
                        self.invalid_ids.append(num)  # Ajouter l'ID invalide à la liste
        return sum(self.invalid_ids)  # Retourner la somme des IDs invalides
# préparer les données d'entrée
with open('Jour 2/input_jour2_part1.txt', 'r') as file:
    input_data = file.read()
jour2_part1 = Jour_2_Part1()
result = jour2_part1.trouver_id_invalide(input_data)
print("La somme des IDs invalides est :", result)

# Partie 2
class Jour_2_Part2:
    def __init__(self):
        self.invalid_ids = []  # Liste pour stocker les IDs invalides
        self.diviseur = [2, 3, 5, 7, 11, 13]
    def trouver_id_invalide(self, input_data):
        ranges = input_data.strip().split(',')  # Diviser les intervalles par des virgules
        for r in ranges:
            start, end = map(int, r.split('-'))  # Diviser chaque intervalle en début et fin
            for num in range(start, end + 1):
                str_num = str(num)
                length = len(str_num)
                for div in self.diviseur:
                    if length % div == 0:  # Vérifier si le nombre de chiffres est divisible par diviseur
                        part_length = length // div
                        parts = [str_num[i*part_length:(i+1)*part_length] for i in range(div)]
                        if all(part == parts[0] for part in parts):  # Vérifier si toutes les parties sont identiques
                            self.invalid_ids.append(num)  # Ajouter l'ID invalide à la liste
                            break  # Sortir de la boucle des diviseurs une fois qu'un match est trouvé
        return sum(self.invalid_ids)  # Retourner la somme des IDs invalides
# préparer les données d'entrée
with open('Jour 2/input_jour2_part2.txt', 'r') as file:
    input_data = file.read()
jour2_part2 = Jour_2_Part2()
result = jour2_part2.trouver_id_invalide(input_data)
print("La somme des IDs invalides est :", result)