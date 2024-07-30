from random import randint
import json

min_ln = 1
max_ln = 5
min_m = 5
max_m = 20

n = input("Número de navios: ")

navios = []

for i in range(0, int(n)):
    navios.append((randint(min_ln, max_ln),randint(min_m, max_m)))

with open('navios.json', 'w') as file:
    json.dump(navios, file)

print(navios)