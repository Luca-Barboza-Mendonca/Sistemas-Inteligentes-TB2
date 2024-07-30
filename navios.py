import json
from genetic2022 import *
from matplotlib import pyplot as plt
import time

# Rodar gerarNavios.py para gerar um set aleatório de navios

navios = []

file = open('navios.json', 'r')

navios = json.load(file) # carregando os navios que foram gerados aleatóriamente

file.close()

n_itens = len(navios)
print(f"Nro de Navios: {n_itens}")
comprimento_max = 20 # comprimento máximo do cais, L

p_count = 100

p = population(p_count, n_itens)

epochs = 1500

t0 = time.time()

media = media_fitness(p, navios, comprimento_max)
best_f = best_fitness(p, navios, comprimento_max)
fitness_history = [[media[0]],[media[1]],[best_f[0]],[best_f[1]]]

for i in range(epochs):
    p = evolve(p, navios, comprimento_max)
    media = media_fitness(p, navios, comprimento_max)
    best_f = best_fitness(p, navios, comprimento_max)
    fitness_history[0].append(media[0])
    fitness_history[1].append(media[1])
    fitness_history[2].append(best_f[0])
    fitness_history[3].append(best_f[1])

t1 = time.time()

t2 = time.time()
best = run_bruteforce(navios, comprimento_max)
print(f"Força bruta: ")
print(best)
t3 = time.time()

print(f"Individuo AG: {str(sorted(p, key=lambda p:p[0])[-1])}, Valor: {str(fitness_history[2][-1])}")
print(f"Tempo AG: {t1 - t0}")
print(f"Tempo Força Bruta: {t3 - t2}")

fig = plt.figure()
ax = plt.axes()


ax.plot(fitness_history[0])
ax.plot(fitness_history[2])

ax.plot(fitness_history[1])
ax.plot(fitness_history[3])

ax.legend(["Fitness Media", "Melhor Fitness", " Comprimento Medio (x10)", "Comprimento do Melhor (x10)"])

ax.grid(True)
plt.show()