import sys

from numpy import sort
sys.path.append('Wordle-Solver')

from search import *
from sortle import *

class Wordle:
    def __init__(self):
        self.word = "" # the word currently being solved for
        self.guessable_list = [] # all the guessable words minus the solution words
        self.solution_list = [] # all the words that are part of the solution list
        self.start_words = ["soare, asier, roast"]

    """ gives the word a score """
    def score(self, word):
        ''' '''
        return 0

    """ solves for the word using self.list """
    def solve(self, word):
        return None

    """ solves for each word in self.solution_list """
    def solve_list(self):
        return None

class WordleGame(Problem):
    """ The problem is to guess the goal word of length 5 from an initial blank state where nothing is known
    about what letters are in the goal word. A state is represented as a an array of length 7 with
    the first six elements being potentially filled with guesses and the last array being the goal word.
    In addition, there is an array of length 26 that states how many of a letter are in the word
    if the letters are guessed. An array of length 5 keeps track of the yellow and green letters that have
    been guessed. """

    def __init__(self, initial, goal=(1, 2, 3, 4, 5, 6, 7, 8, 0)):
        """ Define goal state and initialize a problem """
        super().__init__(initial, goal)

    def find_blank_square(self, state):
        """Return the index of the blank square in a given state"""

        return state.index(0)

    """ Chooses the next word to guess """
    def choose_next_word(self):
        return None

    def actions(self, state):
        """ The only action is to guess the next word.
        The strategy of how a word is choosen can be mixed up here or in the choose_next_word function. """

        return self.choose_next_word()

    def result(self, state, action):
        """ Given state and action, return a new state that is the result of the action.
        Action is assumed to be a valid action in the state """

        # blank is the index of the blank square
        blank = self.find_blank_square(state)
        new_state = list(state)

        delta = {'UP': -3, 'DOWN': 3, 'LEFT': -1, 'RIGHT': 1}
        neighbor = blank + delta[action]
        new_state[blank], new_state[neighbor] = new_state[neighbor], new_state[blank]

        return tuple(new_state)

    def goal_test(self, state):
        """ Given a state, return True if state is a goal state or False, otherwise """

        return state == self.goal


def main():
    # make a new Wordle class
    wordle = Wordle()
    # make a new Sortle class
    sortle = Sortle()
    # convert the new york times solution list to just the words 
    #sortle.convert_to_clean_solution_list('wordle_lists/nyt_wordle_solution_list.txt', 'wordle_lists/sources/new_york_times.txt', 2)
    # compare the new york times list with the one from medium
    #list1 = sortle.convert_to_clean_solution_list('wordle_lists/guessable_list_clean.txt', 'wordle_lists/guessable_list.txt', 2)
    #list2 = sortle.LoadList('wordle_lists/medium_wordle_solution_list.txt')
    #print(sortle.compare_lists(list1, list2))
    #sortle.CountFrequencies(list1)
    #list_guessable = sortle.guessable_words()
    #freq_table_guessable = sortle.CountFrequencies(list_guessable)
    #freq_table_1 = sortle.CountFrequencies(list1, 'data_visualization/guessable_list_freq.txt')

    guessable_list = sortle.LoadList('wordle_lists/nyt_wordle_guessable_list.txt')
    solution_list = sortle.LoadList('wordle_lists/nyt_wordle_solution_list.txt')
    full_list = sortle.LoadList('wordle_lists/nyt_full_list.txt')

    sortle.CountFrequencies(guessable_list, 'data_visualization/txt/guessable_list_freqs.txt')
    sortle.CountFrequencies(solution_list, 'data_visualization/txt/solution_list_freqs.txt')
    sortle.CountFrequencies(full_list, 'data_visualization/txt/full_list_freqs.txt')
    #sortle.unique_test()

if __name__ == '__main__':
    main()