import random

class WordFinder:
    """Word Finder: finds random words from a dictionary."""

# Find a file, read the file, and make an attribute of a list of the words
# prints out “[num-of-words-read] words read”
# method random() returns random word from the list of words we made in line 4
    def __init__(self):
        self.file = open("/usr/share/dict/words", "r")

        self.words_list = self.create_words_list()

        self.file.close()

        self.display_words()

    def create_words_list(self):

        words_list = []

        for word in self.file:
            words_list.append(word)

        return words_list

    def display_words(self):

        print(f"{len(self.words_list)} words read")


    def random(self):
        random_word = random.choice(self.words_list)
        return random_word[:-1:1]





