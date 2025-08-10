"""
This class takes care of reading in lists from text files and counting frequencies of letters from
the english alphabet for the words.
"""
from decimal import Decimal


class Sortle:
    def __init__(self):
        self.list = [] # the word list that the Sortle class does all it's operations on
        self.length = 5 # length of the words for Wordle the standard is 5
        self.alphabet = {
            "a" : 0, "b" : 1, "c" : 2, "d" : 3, "e" : 4, "f" : 5, "g" : 6, "h" : 7, "i" : 8, "j" : 9, 
            "k" : 10, "l" : 11, "m" : 12, "n" : 13, "o" : 14, "p" : 15, "q" : 16, "r" : 17, 
            "s" : 18, "t" : 19, "u" : 20, "v" : 21, "w" : 22, "x" : 23, "y" : 24, "z" : 25
        }

    def unique_test(self):
        word = "apple"
        unique_dict = []
        for z in range(26):
            unique_dict.append(0)
        for i in range(len(word)):
                ch = word[i]
                if (ch.isalpha()):
                    index = self.alphabet[ch] # get the index of the letter so that the count is appropriately updated
                    
                    if (unique_dict[index] == 0): # only add the letter if it is unique in the word
                        print("unique letter: " + ch)
                        unique_dict[index] = 1 # add to dict

    """ returns the frequency of each letter in the english alphabet for the given list
        1. first list -> word letter frequency(wlf): counts unique letters in each word
        2. second list -> general letter frequency(glf): counts all letters in each word
        3. next self.length=5 lists -> spot letter frequency(slf): counts how much of a letter are in each spot in the word """
    def CountFrequencies(self, word_list, writeTo):
        l = [] # a list to hold all the frequency tabulations
        for i in range(self.length + 2):
            a = []
            for j in range(26): # counts of 0 for each letter in the alphabet for each frequency
                a.append(0)
            l.append(a)
        # the first list will be the letter frequencies across all words
        # the rest of the lists will be the letter frequencies for each letter spot in the word
        # ex: _ _ _ _ _ alphabet frequencies for each spot if the word is 5 letters long
        num_unique = 0 # this is for the first list
        for word in word_list:
            # populate unique dict to only count unique letters
            unique_dict = []
            for z in range(26):
                unique_dict.append(0)
            for i in range(len(word)):
                ch = word[i]
                if (ch.isalpha()):
                    index = self.alphabet[ch] # get the index of the letter so that the count is appropriately updated
                    
                    if (unique_dict[index] == 0): # only add the letter if it is unique in the word
                        l[0][index] += 1.0
                        unique_dict[index] = 1 # add to dict
                        num_unique += 1.0

                    l[1][index] += 1.0 # update the first list with all the letter frequencies

                    # has to be i+2 otherwise it overwrites the first,second lists with frequencies for letters in all the words
                    l[i+2][index] += 1.0 # update just the list for which spot the letter is in

        # loop through all the lists and divide each element by the number of words in the list to get the frequency of the letter
        print("word list length: " + str(len(word_list)))
        print("total letters length: " + str(len(word_list) * self.length))
        for i in range(len(l)):
            for j in range(len(a)):
                if (i == 0):
                    l[0][j] /= len(word_list) # we only want to divide by the number of unique letters in each word
                    #print("num unique: " + str(num_unique))
                else:
                    l[i][j] /= (len(word_list) * self.length) # length of list times number of letters in word

        self.WriteFrequencyList(l, writeTo)
        return l

    """ loads a list from the txt file into self.list if it's in the format of
        word
        word
        word
        ... and so on """
    def LoadList(self, txtfile):
        list = []
        with open(txtfile) as f:
            for line in f:
                list.append(line.lower())
        self.list = sorted(list)
        return self.list

    """ writes the frequency list to the text file """
    def WriteFrequencyList(self, list, txtfile):
        with open(txtfile, "w") as w:
            spot = 1
            for i in range(len(list)):
                if (i == 0):
                    w.write("Unique letter frequecnies for entire word (wlf)\n")
                elif (i == 1):
                    w.write("General letter frequencies for entire word(glf)\n")
                else:
                    w.write("Letter frequencies for spot "+ str(spot) + " out of " + str(self.length) + " in the words (slf)\n")
                    spot += 1
                lcurr = list[i]
                indexcurr = 0
                for k in self.alphabet:
                    # round to 5 decimal places
                    w.write(str(Decimal(lcurr[indexcurr]).quantize(Decimal("1e-5"))) + "\n")
                    indexcurr += 1
                w.write("\n")
            w.close()

    """ writes the list from self.list to the file writeTo """
    def write_from_self(self, writeTo):
        with open(writeTo, 'w') as w:
            self.list = sorted(self.list)
            for word in self.list:
                w.write(word)

    """ gets the list from the medium website and strips it of everything but the solution word list
    for site put 1 if the medium website or put 2 if from the source code off New York Times Wordle """
    def convert_to_clean_solution_list(self, writeTo, openFile, site):

        list = []
        # open a file to write the cleaned up word list to
        with open(writeTo, 'w') as w:

            # open the file with the uncleaned up version of the world solution list
            with open(openFile) as f:
                if (site == 1): # if word list taken from Medium website
                    for line in f:

                        # split each line by spaces
                        split_string = line.split(' ')

                        # get the last entry which is the word we want
                        word = split_string[len(split_string-1)]

                        # get rid of the new lines
                        if (word[:-2] == '\n'):
                            word = word[:-2]
                        
                        # only append the word if its of length 5
                        if (len(word) == 5):
                            list.append(word.lower())

                elif (site == 2): # if word list taken from New York Times source code
                    word = ""
                    while True:
                        # reading a single character from the file
                        ch = f.read(1)

                        if not ch:
                            # end of file
                            break
                        else:
                            # check if character is alphabet discard if not
                            if (ch.isalpha()):
                                word += ch
                            else:
                                # only append the word to the list if of length 5
                                if len(word) == 5:
                                    list.append(word.lower() + "\n")
                                    word = ""
                
                else: # if writing a word list from self.list to a file
                    for word in self.list:
                        list.append(word)

                # sort the list
                list = sorted(list)
                # write to the file
                for word in list:
                    w.write(word)

                f.close() # close the file we're reading from
            w.close() # close the file we're writing to
        return list

    """ This function grabs all the 5 letter words from the Scrabble list """
    def guessable_words(self):
        list = []
        # open a file to write the cleaned up word list to
        with open("wordle_lists/5_letter_guessable_words.txt", 'w') as w:

            # open the file with the uncleaned up version of the world solution list
            with open("wordle_lists/scrabble_list_of_words.txt") as f:
                firstLine = f.readline() # get rid of first line as its not words
                counter = 0
                for line in f:
                    # get the last entry which is the word we want
                    word = line

                    # get rid of the new lines
                    if (word[:-2] == '\n'):
                        word = word[:-2]
                    
                    # only append the word if its of length 5
                    if (len(word) == 6):
                        list.append(word.lower())
                        counter += 1
                
                # sort the list
                #list = sorted(list)
                print("sorted list of count: " + str(counter))
                # write to the file
                for word in list:
                    w.write(word)

                f.close() # close the file we're reading from
            w.close() # close the file we're writing to
        return list

    """ returns if lists are identical or not """
    def compare_lists(self, list1, list2):
        if len(list1) != len(list2):
            print('Lists not of equal size!')
            print('list1 is size -> ' + str(len(list1)))
            print('list2 is size -> ' + str(len(list2)))
            #return False
        else:
            print('Lists are both size -> ' + str(len(list1)))
        
        for i in range(len(list1)):
            # get the items from both lists
            word1 = list1[i]
            word2 = list2[i]

            # get rid of the newlines from them if there are any
            if (word1[:-2] == '\n'):
                word1 = word1[:-2]
            if (word2[:-2] == '\n'):
                word2 = word2[:-2]
            
            # compare the two items
            if (word1 != word2):
                print('items at ' + str(i) + " are not the same!")
                print('list1 item is -> ' + list1[i])
                print('list2 item is -> ' + list2[i])
                return False
        
        print('Lists are identical!')
        return True