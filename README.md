# Factoral

## Overview

Factorle is a Wordle-like number game where players guess the factors of a semi-prime number. The challenge lies in determining the correct pair of factors, with feedback provided on the accuracy of each digit's placement. The game features multiple rounds of guessing, error handling for incorrect input, and a best score tracker.

## Gameplay

### Objective
Guess the correct pair of factors for a randomly chosen semi-prime number.

### Feedback
- **Green**: Digit is correct and in the correct position.
- **Yellow**: Digit is correct but in the wrong position.
- **Gray**: Digit is not present in the factor.

### Rules
- The smaller factor comes first, followed by the larger factor.
- The number of digits in the factors will be displayed at the start of the game.
- Players can attempt as many guesses as needed until the correct pair is found.
- If a wrong number of digits is entered for either factor, an error message will prompt the player to try again.

## How to Play

1. **Start the Game:**
   - Run the `Factoral.py` script to start the game.

2. **Understand the Challenge:**
   - The game will display a semi-prime number and the number of digits in each factor.

3. **Make a Guess:**
   - Input your guess as two space-separated numbers (e.g., `12 34`).
   - Ensure that the smaller number comes first.

4. **Get Feedback:**
   - The game will provide feedback on each digit of your guess to help guide your next attempt.

5. **Win the Game:**
   - The game ends when you correctly guess both factors.
   - Your number of attempts will be displayed.

6. **Best Score:**
   - If your number of attempts is better than the previous best score, it will be recorded in a text file.

## Example

- **Semi-Prime Number:** 143
- **Digits in Factors:** Smaller (2 digits), Larger (2 digits)
- **Your Guess:** 18 31
- **Feedback:**
  - Factor 1: Green, Gray
  - Factor 2: Yellow, Yellow

## Requirements

- Python 3.x

## Installation

1. Clone or download the repository.
2. Ensure you have Python 3 installed on your machine.

## Running the Game

To start the game, use the following command:

```bash
python Factoral.py
