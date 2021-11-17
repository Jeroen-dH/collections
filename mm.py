# print(random.randint(3, 9))
import random
kleuren = ['oranje', 'blauw', 'groen', 'bruin']
global aantal
aantal = input("hoeveel m&m's wil je: ")


def zakie(aantal):
    zak = []
    for a in range(int(aantal)):
        zak.append(random.choice(kleuren))
    return zak
print(sorted(zakie(aantal)))