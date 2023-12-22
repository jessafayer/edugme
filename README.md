Import Statements:

import statements are used to bring in external modules that provide additional A functionality.


import random
import unittest


Class Definitions:

Class Def is a fundamental part of the structure code. Classes show data.


class Flashcard:
    #  class definition

class StudyQuestzGame:
    # class definition 


   Docstrings:

Docstrings are used to provide the necessary documentation for classes, functions, or modules. 

'''
This class represents a flashcard with a term and its correct paired definition.

Attributes:
    term (str): The term for the flashcard.
    definition (str): The definition for the flashcard.

   Class Methods

Methods within a class define's the behavior of the class. functions that can operate the class's data.

def __init__(self, term, definition):
    #constructor method 

def add_flashcard(self, term, definition):
    #  method to add a flashcard



User Input:

Functions  input() are used to interact with the user by taking the input. F
term = input("Enter term: ")


Control Flow:

Statements like if, or, while, and for control's the flow of the program. 
if shuffle_option == 'yes':
    self.create_quiz(shuffle=True)

    
  Unit test:
  
Unit tests verify that the code is working correctly. 

class TestStudyQuestzGame(unittest.TestCase):
    # unit test definition
Main Block:

The if __name__ == "__main__": block is used to check whether the  script is being run as the main program or if it is being imported as a module. 
if __name__ == "__main__":
    unittest.main()


    
