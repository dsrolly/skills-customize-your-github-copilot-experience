
# 📘 Assignment: Games in Python

## 🎯 Objective

Build a Hangman word-guessing game using Python strings, loops, conditionals, random selection, and user input.

## 📝 Tasks

### 🛠️ Set Up the Word and Guess State

#### Description
Create a word list and randomly select one word for the player to guess. Display the word as a row of underscores with one underscore for each letter.

#### Requirements
Completed program should:

- Store at least five possible words in a predefined list.
- Randomly select a word from the list.
- Display the hidden word using underscores, such as `_ _ _ _`.
- Accept a single letter as input from the player.

### 🛠️ Check and Track Player Guesses

#### Description
Update the displayed word whenever the player guesses a correct letter and track incorrect guesses separately.

#### Requirements
Completed program should:

- Reveal every position of a correctly guessed letter.
- Keep all other letters hidden as underscores.
- Record incorrect letter guesses.
- Limit the player to a maximum of six incorrect guesses.
- Ignore repeated guesses or ask the player to guess again.

### 🛠️ Complete the Game Loop

#### Description
Repeat the guessing process until the player has revealed the word or used all incorrect guesses.

#### Requirements
Completed program should:

- Use a loop to continue the game until it ends.
- Display the current hidden word after each guess.
- Display a win message when every letter has been guessed.
- Display a lose message and the hidden word when the player runs out of attempts.
