import random

class WordFinder:
    """Word Finder: finds random words from a dictionary."""

# Find a file, read the file, and make an attribute of a list of the words
# prints out “[num-of-words-read] words read”
# method random() returns random word from the list of words we made in line 4
    def __init__(self):
        """
        Open file with words, call functions that create and clean word
        lists, calls function to display words.
        """

        # the only thing we want in the init is the word list

        # self.file = open("/usr/share/dict/words", "r")
        self.file = open("wordtestfile.txt", "r")

        self.words_list = self.create_words_list()

        self.file.close()

        self.display_words()


    def __repr__(self):
        """Displays properties of WordFinder instance."""
        print(f"This is the filtered word list: {self.words_list}")


    def create_words_list(self):
        """Goes through each line of file and appends line to a list."""
        words_list = []

        for word in self.file:
            words_list.append(word)

        return words_list


    def display_words(self):
        """Prints how many words are in unfiltered and filtered word lists."""
        print(f"There are {len(self.words_list)} words in filtered words list")


    def random(self):
        """Grabs a random word from words list and strips '\n'"""
        random_word = random.choice(self.words_list)
        return random_word[:-1:1]



class SpecialWordFinder(WordFinder):
    """
    Creates subclass of WordFinder to account for word files with
    empty lines or commented lines
    """

    def __init__(self):
        """
        Dunder init inherits WordFinder dunder init
        and creates a word list with only valid words
        """
        super().__init__()

        self.words_list = self.clean_words_list()

        super().random()


    def __repr__(self):
        """Displays properties of SpecialWordFinder instance."""
        print(f"This is the word list: {self.words_list}")


    def clean_words_list(self):
        """Filters initial word list to eliminate blank lines and comments."""
        clean_words = []

        for line in self.words_list:
            empty_test = line.strip()

            # If it's empty, this will catch it
            if bool(empty_test) and not line.startswith("#"):
                clean_words.append(line)

        print(clean_words)

        return clean_words
