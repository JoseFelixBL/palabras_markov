"""Palabras de Markov"""

"""Viene de https://www.youtube.com/watch?v=8ext9G7xspg&t=9109s
    - Leer un texto
    - Crear un grafo donde:
        - cada nodo son palabras
        - cada palabra tiene una lista de palabras siguientes
        con la frecuencia en que son 'siguientes' según el texto
    - Luego se selecciona una palabra y se navega el grafo
    aleatoriamente según el peso de cada palabra siguiente.
"""


import random
texto = "I am, subscribed to Y-Cubed and I am 123 loving678 it."
texto = "I am, subscribed to Y Cubed and I am 123 loving678 it."
# Quitar los separadores: , . : ; ...
separadores = ".:,;¡¿!?()[]{}ªº0123456789-_"

palabras = {}
anterior = ""
# Las palabras compuestas separadas por "-" quedan unidas...
for pal in texto.split():
    if not pal.isalpha():
        for char in separadores:
            nueva_pal = pal.replace(char, "")
            pal = nueva_pal
            if pal.isalpha() or pal == "":
                break
    if pal == "":
        continue

    if pal not in palabras:
        palabras[pal] = {}

    if anterior == "":
        anterior = pal
        continue

    if pal not in palabras[anterior]:
        palabras[anterior][pal] = 0
    palabras[anterior][pal] += 1

    anterior = pal

print(palabras)

# Elegir una palabra y seguir el grafo
print("Palabras disponibles")
for pal in palabras:
    print(pal, end=" ")
print()
inicio = input("Escriba la palabra por la que comenzar: ")

print(inicio, end=" ")
pal = inicio
while True:
    peso_total = 0
    pal_sig = {}
    for siguiente, peso in palabras[pal].items():
        peso_total += peso
        pal_sig[peso_total] = siguiente
    if peso_total == 0:
        break

    peso_sig = random.randint(1, peso_total)
    for peso in sorted(pal_sig.keys()):
        if peso_sig <= peso:
            pal = pal_sig[peso]
            print(pal_sig[peso], end=" ")
            break

print()
