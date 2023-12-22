import unittest

class Flashcard:
    '''
    This class represents a flashcard with a term and its definition.

    Attributes:
        term (str): The term for the flashcard.
        definition (str): The definition for the flashcard.
    '''

    def __init__(self, term, definition):
        '''
        Initializes the Flashcard object with the given term and definition.

        Args:
            term (str): The term for the flashcard.
            definition (str): The definition for the flashcard.
        '''
        self.term = term
        self.definition = definition


class StudyQuestzGame:
    '''
    This class represents the StudyQuestz flashcard game, gamifying learning.

    Attributes:
        flashcards(list): List to hold flashcard objects for the game.
    '''

    def __init__(self):
        '''
        Initializes the StudyQuestzGame object with an empty list of flashcards.
        '''
        self.flashcards = []

    def add_flashcard(self, card, definition):
        '''
        Adds a new flashcard to the game.

        Args:
            card (str): The term for the flashcard.
            definition (str): The definition for the flashcard.
        '''
        flashcard = Flashcard(card, definition)
        self.flashcards.append(flashcard)

    def input_flashcard(self):
        '''
        Takes user input to create a new flashcard and adds it to the game.
        '''
        card = input("Enter the term: ")
        definition = input("Enter the definition: ")
        self.add_flashcard(card, definition)

    def play_game(self):
        '''
        Initiates the quiz and tracks user points.
        '''
        print("\nWelcome to StudyQuestz! Let's start the game.\n")
        self.input_flashcard()  # Add a flashcard for the user to study
        # Add the logic for the quiz and point tracking as needed


# Unit Test
#class TestStudyQuestzGame(unittest.TestCase):
    def test_add_flashcard(self):
        game = StudyQuestzGame()
        game.add_flashcard("Python", "A high-level programming language.")
        self.assertEqual(len(game.flashcards), 1)
        self.assertEqual(game.flashcards[0].term, "Python")
        self.assertEqual(game.flashcards[0].definition, "A high-level programming language.")

#if __name__ == "__main__":
    unittest.main()
