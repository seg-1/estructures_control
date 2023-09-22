"""
- Exercici 4

Crea un programa que donada una llista qualsevol, et digui si és simètrica o no. Si ho és, que et digui quants elements té.
"""

llista = [1,2,2,1]
i = -1
check = str

for element in llista:
    print(element)
    print(llista[i])

    if element == llista[i]:
        check = "La llista es simtrica"
    else:
        check = "La llista no es simtrica"

    i = i - 1

print(check)
