# Boggle Game

Our Boggle program runs according to the Boggle game rules. It features an intuitive clock—implemented without relying on external libraries such as `time`—that enhances the user experience. We have also created all the necessary buttons and labels to play the game with clear, readable sizes and fonts. 

The application includes:
- A **Start** button to begin the game.
- A **Quit** button to exit the program.
- A **Remove** button that acts like the backspace key on the keyboard.
- A **Check** button to validate the chosen word.

We replaced the default Tkinter icon with a custom Boggle icon for a more polished look. When a user chooses a word and clicks the **Check** button, if the word is correct, it is added to a listbox displaying the chosen words—with the latest picked word always on top. When time runs out, a message box prompts the user to decide whether to play again or exit.

## Features

- **Intuitive Timer:**  
  A clock that runs without any external libraries, providing a smooth countdown experience.

- **User-Friendly Interface:**  
  Clear and readable buttons and labels with well-chosen sizes and fonts.

- **Game Controls:**  
  - **Start Button:** Initiates the game and the timer.
  - **Quit Button:** Exits the program.
  - **Remove Button:** Functions as a backspace to remove the last letter selected.
  - **Check Button:** Validates the formed word and updates the word list.

- **Custom Icon:**  
  Replaces the default Tkinter icon with a Boggle-specific icon.

- **Dynamic Word List:**  
  Correctly guessed words are displayed in a listbox with the most recent word at the top.

- **Game Over Prompt:**  
  When the timer ends, a prompt asks whether the user wants to play again.

## Usage

1. **Clone the Repository:**

   ```bash
   git clone <repository_url>
