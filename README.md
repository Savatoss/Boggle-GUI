Overview
Our Boggle program runs according to the classic Boggle game rules. The game features an intuitive clock (implemented without external libraries like time) and a user-friendly graphical interface built with Tkinter. All the necessary buttons and labels are provided in clear, readable sizes and fonts.

Features
Clock/Timer:
An intuitive timer that counts down without relying on external libraries.

Dynamic Game Board:
The game board is generated with buttons that represent the letters. The layout ensures all buttons are visible and easy to interact with.

Control Buttons:

Start: Begins the game and activates the timer.
Check: Validates the selected word. If the word is correct, it is added to a listbox that displays all valid words (with the most recent word appearing at the top).
Remove: Acts like a backspace key to remove the last selected letter.
Quit: Exits the program.
Custom Icon:
Replaces the default Tkinter icon with a custom Boggle icon for a more polished look.

Game Over Prompt:
When time expires, a message box prompts the user to decide whether to play again or exit the game.
