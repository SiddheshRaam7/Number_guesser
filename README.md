# Number Guessing Game

A Python-based command-line game where players compete to guess a hidden number between 1 and 100. The game tracks your attempts and saves high scores to a local leaderboard.

## Features
* **Three Difficulty Modes:** Choose your challenge level, ranging from unlimited guesses to a strict 10-attempt limit.
* **Persistent Leaderboard:** Scores are saved to a `leaderboard.txt` file and sorted so you can see the most efficient guessers.
* **Feedback:** The game tells you if your guess is too high or too low and prevents you from wasting turns on duplicate guesses.
* **Clean Exit:** Type `Q` at any time to forfeit and reveal the secret number.

---

## How to Run It

1. **Download the Files:** Ensure both the Python script and any associated files are in the same folder, and make sure that the name of the leaderboard.txt is exactly this (not leaderboard.txt (1), etc.).
2. **Run the Game:** Execute the `Final_project` Python file in your terminal or IDE:
   ```bash
   python Final_project.py
