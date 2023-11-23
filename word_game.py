"""Compute a team's score for a (fictitious) word game.
In this game, two players independently find words in a matrix of letters.
Each player's words are added to a text file with one word per line. Duplicates
are removed from each player's list. For each word that appears on both players'
lists, the team's score increases by the number of letters in the word minus 2
(words less than three characters long are not worth any points).
"""

from argparse import ArgumentParser
import sys

class PlayerWords:
    """Shows the player's words and calculates the team's score.
    
    Attributes: 
        words(set): A set containing the unique words found by the player.
    """

    def __init__(self, filepath):
        """Initialize a PlayerWords object.

        Args:
            filepath: Path to a text file containing the player's words
            
        Side effects: 
            Reads the content of the file and initializes the attribute with unique words
        """
        self.words = set()
        with open(filepath, 'r') as file:
            for line in file:
                word = line.strip()
                self.words.add(word)
    
    def score(self, partner):
        """Calculate the team's score based on common words found by two players.

        Args:
            partner (PlayerWords): The partner's Playerwords object
        
        Returns:
            The team's score.
            
        Side effects: 
            None
        """
        common_words = self.words.intersection(partner.words)
        score = sum(len(word) - 2 for word in common_words if len(word) >= 3)
        return score
    
def main(player1_filepath, player2_filepath):
    """Calculate and print the team's score based on words found by two players.

    Args:
        player1_filepath: The path to a text file containing words found by player 1.
        player2_filepath: The path to a text file containing words found by player 2.
        
    Side effects: 
        Reads the content of the file and computes the team's score
    """
    player1 = PlayerWords(player1_filepath)
    player2 = PlayerWords(player2_filepath)
    team_score = player1.score(player2)
    print(f"Your team scored {team_score} points!")

if __name__ == "__main__":
    player1_filepath = "player1_words.txt"
    player2_filepath = "player2_words.txt"
    main(player1_filepath, player2_filepath)

def parse_args(arglist):
    """
    Parse command line arguments.

    Expect two mandatory arguments:
        - str: path to a text file containing words found by player 1.
        - str: path to a text file containing words found by player 2.

    Args:
        arglist (list of str): Arguments from the command line.

    Returns:
        namespace: The parsed arguments, as a namespace.
    """
    parser = ArgumentParser()
    parser.add_argument("wordfile1", help="file containing player 1's words")
    parser.add_argument("wordfile2", help="file containing player 2's words")
    return parser.parse_args(arglist)

if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    main(args.wordfile1, args.wordfile2)
