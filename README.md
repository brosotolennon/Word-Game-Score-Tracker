**Project Title:** Word Game Score Tracker

**Overview**

The Word Game Score Tracker is a Python-based solution designed to simulate a competitive word game between two players. In this engaging game, participants independently search for words within a matrix of letters and compile their findings into text files. The program then efficiently removes duplicates from each player's list and calculates the team's score based on common words found by both players. The scoring system awards points only to words that are at least three letters long, with each word's score determined by the number of letters minus 2. The project provides a versatile and customizable framework, allowing users to adapt the game scenario to various word challenges. The PlayerWords class encapsulates the functionality of reading words from a file and computing scores, while the main() function orchestrates the overall process, making it user-friendly and accessible.


**Usage**

Ensure to download the following example files:
- player1_words.txt
- player2_words.txt

Run the program by executing the word_game.py script in the terminal, providing the paths to the text files containing words for player 1 and player 2 as command-line arguments. For example:
- python3 word_game.py player1_words.txt player2_words.txt
