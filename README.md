# Hangman Game / Juego del Ahorcado

A Hangman game with a graphical interface developed in Python using Tkinter, created as a final project for **Code in Place** by Stanford University.

Un juego del Ahorcado con interfaz gráfica desarrollado en Python usando Tkinter, creado como proyecto final para **Code in Place** de la Universidad de Stanford.

---

## Description / Descripción

This project is a graphical implementation of the classic Hangman game. The player must guess the hidden word by clicking letters on a virtual keyboard. Each incorrect guess draws a part of the hangman. The game ends when the player guesses the word correctly or the hangman is complete.

Este proyecto es una implementación gráfica del clásico juego del Ahorcado. El jugador debe adivinar la palabra oculta haciendo clic en letras de un teclado virtual. Cada error dibuja una parte del ahorcado. El juego termina cuando el jugador adivina la palabra correctamente o el ahorcado está completo.

---

## Features / Características

-  Graphical interface with Tkinter / Interfaz gráfica con Tkinter
-  Virtual keyboard (A-Z buttons) / Teclado virtual (botones A-Z)
-  Visual hangman drawing on canvas / Dibujo visual del ahorcado en canvas
-  Restart button for new games / Botón para reiniciar partida
-  Input validation (no repeated letters) / Validación de entrada (sin letras repetidas)
  - Used letters display / Visualización de letras usadas

---

## Requirements / Requisitos

- Python 3.6 or higher / Python 3.6 o superior
- Tkinter (included with Python, no extra installation needed / incluido con Python, no requiere instalación extra)

---

## How to Run / Cómo ejecutar

1. Download or clone this repository / Descargá o cloná este repositorio
2. Open a terminal in the project folder / Abrí una terminal en la carpeta del proyecto
3. Run the following command / Ejecutá el siguiente comando:

```bash
python Flujo.py

How to Play / Cómo jugar
Click any letter on the virtual keyboard / Hacé clic en cualquier letra del teclado virtual

If the letter is correct, it appears in the word / Si la letra es correcta, aparece en la palabra

If it's wrong, a part of the hangman is drawn / Si es incorrecta, se dibuja una parte del ahorcado

Win by guessing all letters / Ganá adivinando todas las letras

Lose if the hangman is completed (6 mistakes) / Perdés si el ahorcado se completa (6 errores)

Acknowledgments / Agradecimientos
This project was created as part of Code in Place by Stanford University. Special thanks to my section leader and the entire Code in Place team for this amazing learning opportunity.

Este proyecto fue creado como parte de Code in Place de la Universidad de Stanford. Un agradecimiento especial a mi profesor guía y a todo el equipo de Code in Place por esta increíble oportunidad de aprendizaje.
