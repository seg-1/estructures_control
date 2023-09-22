"""
- Exercici 5

Crea un programa que donada una llista, et digui quants números coincideixen amb la seva posició.
Per exemple [3,4,2,0,2,3,6] el 2 i el 6 coincideixen.
"""

llista = [3,4,2,0,2,3,6]
j = 0

for i in llista:
    if j == i:
        print("El numero", i, "coincideix amb la seva posició en llista",j)

    j = j + 1

