
# 📘 Assignment: Hangman Game Challenge

## 🎯 Objective

Build a Hangman game in Python that practices string handling, loops, conditionals, and user interaction.

## 📝 Tasks

### 🛠️ Game Setup and Word Selection

#### Description
Create the initial Hangman game setup by choosing a secret word and preparing the game state.

#### Requirements
Completed program should:

- Randomly select a word from a predefined list
- Initialize the display state with underscores for each letter
- Track letters guessed by the player
- Set a maximum number of incorrect attempts

### 🛠️ Player Interaction and Guess Processing

#### Description
Implement the core game loop to accept guesses and update the game state accordingly.

#### Requirements
Completed program should:

- Prompt the player to guess a single letter each turn
- Reveal correct letters in the word display
- Show current progress in `_ _ _` format
- Track incorrect guesses and remaining attempts
- Prevent repeated guesses from affecting the game unfairly

### 🛠️ Endgame and Result Messages

#### Description
Finish the game with a clear win or lose outcome and display the result to the player.

#### Requirements
Completed program should:

- End when the player guesses the word or runs out of attempts
- Display a win message when the word is fully guessed
- Display a lose message and reveal the secret word if attempts are exhausted
- Provide feedback for each guess
