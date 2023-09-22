"""
- Exercici 3

Crea un programa que et pregunti el teu nom, i et demani un número.
Si el número és 0, hauria de mostrar un missatge d’error.
En cas contrari, hauria de mostrar el nom repetit tants cops com indiqui el número.
Per exemple, “Joan Joan Joan”.
"""

nom = str(input("Introdueix el teu nom: "))
numero = int(input("Introdueix un numero: "))

if numero == 0:
    print("Error el numero 0 no es pot multiplicar!")
else:
    print(nom * numero)
