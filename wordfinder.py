"""Word Finder: finds random words from a dictionary."""

import random


class WordFinder:
	"""For finding random words from dictionary."""

    def __init__(self, path):
        dict_file = open(path)
        self.words = self.parse(dict_file)
        print(f"{len(self.words)} words read")

    def parse(self, dict_file):
        return [w.strip() for w in dict_file]

    def random(self):
        return random.choice(self.words)


class SpecialWordFinder(WordFinder):

	"""
	This is the Parse method which parse the dict_file 
	and list of words while skipping blanks/comments.
	"""

    def parse(self, dict_file):
        return [w.strip() for w in dict_file
                if w.strip() and not w.startswith("#")]
    

wordFinder = WordFinder("words.txt")
print(wordFinder.random())

specialwordfinder = SpecialWordFinder("words.txt")
print(specialwordfinder.random())