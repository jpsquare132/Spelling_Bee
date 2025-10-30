# Worldle-Mini
🐝 Spelling Bee Game
📝 Overview
Spelling Bee is a command-line word puzzle game based on the popular format. Players are challenged to find as many words as possible using a limited set of seven letters. The primary goal is to maximize your score by finding long words and, most importantly, Pangrams!

## 🚀 How to Play
Setup

Enter Your Letters: The game first asks the user (or the game administrator) to input seven unique letters, separated by commas (e.g., a,b,c,d,e,f,g).

Choose the Required Letter: From those seven letters, you must designate one as the required letter. This letter must be present in every word you submit.

Start Guessing: Once the letters are set, you can begin entering valid words.

## Rules for Valid Words

For any word to be counted and scored, it must meet three conditions:

Length: The word must be at least 4 letters long.

Required Letter: The word must contain the required letter chosen during setup.

Available Letters: The word can only use the seven letters provided at the start of the game.

No Repeats: You cannot submit the same word twice.

## Scoring

Points are awarded based on the length of the word, with bonuses for finding a Pangram:

Word Length	Base Points
4 letters	1 point
5 letters	5 points
6 letters	6 points
7+ letters	7 points, plus 1 point for every letter beyond 7
Pangram Bonus: If a word successfully uses all seven of the available letters, it is considered a Pangram and receives an additional 7-point bonus on top of its base length score!

## Ending the Game

To stop entering words and see your final score, simply type END when prompted for your next word. The game will display your cumulative total score.

# 🛠️ Requirements
The game is written in Python and is structured across several modules for clean organization:

spelling_bee.py: The main execution file that handles user input, game flow, and scoring aggregation.

get_word.py: Manages user word entry and validates basic rules (length, required letter, letter usage, and if the word has been used).

score.py: Calculates the points for a valid word, checking for the Pangram condition.

pangram.py and valid_word.py: Helper functions used for specific rule checks.