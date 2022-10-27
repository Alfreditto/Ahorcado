from random import *


def nuevo_string(palabraAdivinar, letra, palabraSecreta):
    palabra_nueva = ''
    for i, character in enumerate(palabraAdivinar):
        if character == letra:
            palabra_nueva += letra
        elif palabraSecreta[i] != '-':
            palabra_nueva += palabraSecreta[i]
        else:
            palabra_nueva += '-'
    return palabra_nueva


palabras_adivinar_lista = ("patata", "zanahoria", "boniato")
palabraAdivinar = choice(palabras_adivinar_lista)
# palabraSecreta = ''
vidas = 6
# for i in range(len(palabraAdivinar)):
palabraSecreta = len(palabraAdivinar) * '-'

while '-' in palabraSecreta and vidas > 0:
    print(palabraSecreta)
    print(f"Vidas restantes {vidas}")
    letra = input("Dime una letra: ").lower()
    if palabraAdivinar.find(letra) != -1:
        if letra in palabraSecreta:
            print("Letra repetida")
        else:
            palabraSecreta = nuevo_string(palabraAdivinar, letra, palabraSecreta)

    else:
        vidas -= 1

if '-' not in palabraSecreta and vidas > 0:
    print("Ganaste!")
else:
    print("Perdiste")
