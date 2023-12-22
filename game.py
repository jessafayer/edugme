import random
import unittest

class Flashcard:
    '''
    This class represents a flashcard with a term and its correct paired definition.

    Attributes:
        term (str): The term for the flashcard.
        definition (str): The definition for the flashcard.
    '''

    def __init__(self, term, definition):
        '''
        Initializes the Flashcard object with the given term and its correct definition.

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
        points (int): User's points in the game collected by correct to wrong results.
    '''

    def __init__(self):
        '''
        Initializes the StudyQuestzGame object with an empty list of flashcards and zero points.
        '''
        self.flashcards = []
        self.points = 0

    def add_flashcard(self, term, definition):
        '''
        Adds a new flashcard to the game.

        Args:
            term (str): The term for the flashcard.
            definition (str): The definition for the flashcard.
        '''
        flashcard = Flashcard(term, definition)
        self.flashcards.append(flashcard)

    def input_flashcard(self):
        '''
        Takes user input to create a new flashcard and adds it to the game's study set.
        '''
        term = input("Enter the term: ")
        definition = input("Enter the definition: ")
        self.add_flashcard(term, definition)

    def create_quiz(self, shuffle=False):
        '''
        Create a personalized quiz by shuffling flashcards if specified.

        Args:
            shuffle (bool): To randomize order in the pattern flashcards are presented by using function shuffle.
        '''
        if shuffle:
            random.shuffle(self.flashcards)

    def get_yes_no_input(self, prompt):
        '''
        Get valid yes/no input from the user.

        Args:
            prompt (str): The prompt message is displayed.
        '''
        while True:
            response = input(prompt).lower()
            if response in ('yes', 'no'):
                return response
            print("Please enter 'yes' or 'no' as your response.")

    def get_user_input(self):
        '''
        Function to handle user input for adding flashcards.
        '''
        while True:
            try:
                difficulty = int(input("Enter the level of difficulty (1 for easy, 2 for medium, 3 for hard): "))
                if difficulty in [1, 2, 3]:
                    break
                else:
                    print("Invalid difficulty level. Please enter 1, 2, or 3.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    def display_results(self):
        '''
        Function to display quiz results.
        '''
        print(f"\nQuiz completed! You scored {self.points} points.")

    def handle_retry(self):
        '''
        Function to handle the retry option.
        '''
        retry_option = self.get_yes_no_input("Do you want to retry the quiz? (yes/no): ")
        if retry_option == 'yes':
            self.points = 0
            self.play_game()

    def play_game(self):
        '''
        Initiates the quiz and tracks user points.
        '''
        print("\nWelcome to StudyQuestz! Accomplish learning in game form, Let's kick off the quest.\n")

        # Allow the user to input their own flashcards they wish to master
        while True:
            add_more = self.get_yes_no_input("Do you want to add a flashcard? (yes/no): ")
            if add_more != 'yes':
                break
            self.input_flashcard()

        # Shuffle flashcards at random
        shuffle_option = self.get_yes_no_input("Do you want to shuffle the flashcards before the quiz? (yes/no): ")
        self.create_quiz(shuffle=shuffle_option == 'yes')

        # Quiz: Assessment for testing users' knowledge on each flashcard
        for flashcard in self.flashcards:
            print(f"\nQuestion: What is the definition of '{flashcard.term}'?")
            user_answer = input("Your answer: ")
            if user_answer.lower() == flashcard.definition.lower():
                print("Correct!")
                self.points += flashcard.difficulty  # Adjust points based on the level of difficulty
            else:
                print(f"Wrong! The correct definition is: {flashcard.definition}")

        # Display user's points
        self.display_results()

        # Ask if the user wants to retry the quiz for a better score
        self.handle_retry()


# Unit Test
class TestStudyQuestzGame(unittest.TestCase):
    def test_add_flashcard(self):
        game = StudyQuestzGame()
        game.add_flashcard("Happy", "Emotion or Feeling showing pleasure or contentment of joy.")

        # Ensure the flashcard is added
        self.assertEqual(len(game.flashcards), 1)

        # Ensure the flashcard term is correct
        self.assertEqual(game.flashcards[0].term, "Happy")

        # Ensure the flashcard definition is not directly exposed in the test
        self.assertTrue(game.flashcards[0].definition)


if __name__ == "__main__":
    unittest.main()

