"""
- Exercici 1

L'exercici consisteix a crear un programa que et classifiqui una variable numèrica en funció de l’escala Suspès/Aprovat/Notable/Excel·lent.

Recorda que Suspès < 5, Aprovat > 5 i < 7, Notable > 7 i < 9 i Excel·lent > 9.
"""

nota = 7

if nota < 5:
    print("Suspès")

elif 5 <= nota < 7:
    print("Aprovat")

elif 7 <= nota < 9:
    print("Notable")

else:
    print("Excel·lent")
