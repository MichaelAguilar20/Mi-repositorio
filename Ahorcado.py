import random
def Juego_del_ahorcado(): 
    IMAGENES_AHORCADO = ['''
      +---+
      |   |
          |
          |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
          |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
     /    |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
     / \  |
          |
    =========''']
    
    IMAGENES_AHORCADO.reverse()
    
    
    print("Selecciona un nivel de dificulta1d: ")
    print("1. Fácil ")
    print("2. Medio ")
    print("3. Difícil ")
    
    opcion = input("Elige: ")
    
    if opcion == "1":
        palabras = ["gato", "agua", "hola", "sol", "casa"]
    elif opcion == "2":
        palabras = ["ecuador", "aventura", "mandarina", "pintura"]
    elif opcion == "3":
        palabras = ["bienvenido", "electrodomestico", "espectaculo", "hipopotamo"]
    else: 
        print("Opción no válida, usando lista por defecto.")
        palabras = ["gato", "agua", "hola", "sol", "casa", "bienvenido", 
                    "electrodomestico", "espectaculo", "hipopotamo",
                    "ecuador", "aventura", "mandarina", "pintura"
                    ]
        
    
    palabra_oculta = random.choice(palabras)
    letras_reveladas = ["_"] * len(palabra_oculta)
    intentos = 6
    
    letras_usadas = []
    print("Bienvenido al juego de Ahorcado")
    while intentos > 0:
        
        print(IMAGENES_AHORCADO[intentos])
        print(f"\nPalabra: {' '.join(letras_reveladas)}")
        print(f"Letras usadas: {', '.join(letras_usadas)}")
        print(f"Vidas restantes: {intentos}")
        letra = input("Escribe una letra: ")
        if letra in letras_usadas:
            print("Intenta con otra.")
            continue
        letras_usadas.append(letra)
        if letra in palabra_oculta:
            print("es correcta.")
            for i in range(len(palabra_oculta)):
                if palabra_oculta[i] == letra:
                    letras_reveladas[i] = letra
        else:
            print(f"No,es la letra '{letra}' no está.")
            intentos -=1
           
        if "_" not in letras_reveladas:
            print(f"\nAdivino la palabra: {palabra_oculta}")
            break
    else:
        print(IMAGENES_AHORCADO[0])
        print("perdido")
        print(f"La palabra es: {palabra_oculta}")
        print("Jugar de nuevo")
    reiniciar = input("\n(s/n): ")

    if reiniciar.lower() == "s":
        Juego_del_ahorcado()
Juego_del_ahorcado()
