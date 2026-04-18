## Ficha del Proyecto
Nombre: Michael Wilfrido Aguilar Andrade

Fecha: 18 de abril de 2026

Programa: Juego del Ahorcado  en Python.

Objetivo: Desarrollar un programa interactivo de consola que permita al usuario adivinar una palabra oculta seleccionada al azar de las palabras, gestionando niveles de dificultad y un sistema de intentos visual mediante arte ASCII o el ahorcado.
# Juego del Ahorcado

#Descripcion

Este juego es un clasico pasatiempo de adivinar la palabra. asi como se inicio principalmente el juego con,
 papel y lapiz  donde un  los jugadores o el jugador piensa una palabra y el otro juagador trata de adivinarla, la  letra por letra, antes de completar el dibujo de un hombre ahorcado generalmente tiene entre  6-10 fallos. Por cada letra incorrecta, se añade una parte del cuerpo a la horca. Gana si  adivina la palabra antes de que el dibujo se complete. esos es entro ladicional.
Lo que aqui hize fue llevarar el juago a lo digil programado en python. para que sea mas entretenido y ver como se formando el **ahorcado**


## Demo


[Demo](https://github.com/MichaelAguilar20/Mi-repositorio.git)
## Screenshots
![imagen alt](https://github.com/MichaelAguilar20/Mi-repositorio/blob/cae43f2ee867312a90d570cacfd57e54767f927b/ahorcado%20inicio.png)
![imagen alt](https://github.com/MichaelAguilar20/Mi-repositorio/blob/cae43f2ee867312a90d570cacfd57e54767f927b/ahorcado%20final.png)


# Explicación principales funcionalidades del código.

1. Selecion de Niveles de Dificultad
 * Al iniciar, el juego permite al usuario elegir entre tres niveles. Esta elección filtra la lista de palabras posibles utilizando estructuras condicionales, if/elif/else

 * Fácil: Palabras cortas.  
 * Medio: Palabras de intermedia.  
 * Difícil: Palabras largas y complejas.

2. Representación Visual Del Ahorcado.      

 * Utiliza una lista llamada IMAGENES_AHORCADO que contiene arte del Ahorcado.

 * Aqui el programa imprime el estado del "ahorcado" basándose en el índice de la lista que coincide con el número de intentos restantes.

 * Reverse: Se aplica .reverse() a la lista para alinear correctamente el orden de las imágenes con la cuenta regresiva de vidas.
 
3. Gestión de Estado del Juego.

* Este es el núcleo del juego utiliza un ciclo while intentos    >  0 para mantener la partida activa, controlando, y seguir jugando.

* Validación de letras: El programa guarda las letras ya ingresadas en la lista letras_usadas para evitar que el usuario pierda vidas por repetir una letra.

* RRenderizado: Se imprime el estado actual de la horca, la palabra con guiones bajos (_ _ _) y las letras que ya probaste.  

* Captura de entrada: Se solicita una letra con input().   

   * Validación:

   * Si la letra ya se usó, no penaliza pero avisa al jugador.

   * Si la letra está en palabra_oculta, recorre la palabra con   un for y actualiza la lista letras_reveladas.

   * Si falla, resta un intento (intentos -= 1).
* Condición de victoria: Si ya no quedan guiones bajos ("_" not in letras_reveladas), el jugador gana y el bucle se rompe con break.

4. Juego Terminado.
* El código utiliza una característica de Python poco común pero muy útil: el else en un bucle while.   

* Este else solo se ejecuta si el bucle terminó porque la condición de los "intentos > 0"  y se vuelve falsa, es decir, te quedaste sin vidas, se rompió con un break. Por eso, el mensaje de "Perdido".
5. Reiniciar el Juego.

* Al final, si el usuario presiona "s",  para juegar de nuevo  o si prciona "n" para salir del juego, el código llama a la función Juego_del_ahorcado() dentro de sí misma o salir.
Esto se conoce como reinicio y permite volver a empezar el juego desde cero sin cerrar el programa.  


* Módulos: random (para la selección aleatoria de la palabra).
## Tecnoloias

**Paython:** 

**Import random:** 
