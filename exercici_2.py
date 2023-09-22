"""
- Exercici 2

Utilitzant el següent tutorial crea un programa que et pregunti dos números.
T’ha de mostrar un missatge dient si el primer és més gran, el segon és més gran o són iguals.
"""

n1 = int(input("Introdueix un numero: "))
n2 = int(input("Introdueix un numero: "))

if n1 > n2:
    print(n1, "es més gran que", n2)
else:
    print(n2, "es més gran que", n1)