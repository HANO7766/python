import random


def adivina_el_numero():
    # Genera un número aleatorio entre 1 y 100
    numero_secreto = random.randint(1, 100)
    intentos = 0

    print("¡Bienvenido al juego de adivinanzas!")
    print("He seleccionado un número entre 1 y 100. ¡Intenta adivinarlo!")

    while True:
        try:
            intento = int(input("Introduce tu número: "))
            intentos += 1

            if intento < numero_secreto:
                print("El número secreto es MAYOR.")
            elif intento > numero_secreto:
                print("El número secreto es MENOR.")
            else:
                print(f"¡Felicidades! Adivinaste el número en {intentos} intentos.")
                break
        except ValueError:
            print("Por favor, introduce un número válido.")



