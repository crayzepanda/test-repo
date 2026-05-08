import random

def number_aleatoire():
    return random.randint(1, 100)

def decimal_aleatoire():
    return random.uniform(0, 1)

print("Le nombre aléatoire généré est :", number_aleatoire())
print("Le nombre décimal aléatoire généré est :", decimal_aleatoire())