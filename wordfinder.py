"""Word Finder: finds random words from a dictionary."""

import random

class WordFinder:
    """Find random words from a file.
    
    >>> wf = WordFinder("words.txt")
    3 words read
    
    >>> wf.random() in ["kale", "parsnips", "apple", "mango"]
    True

    >>> isinstance(wf.random(), str)
    True
    """

    """Initialize WordFinder with a list of words from a file"""

    def __init__(self, file_path="/home/meaallen/OOPython/words.txt"):
        self.words = self._read_file(file_path)
        print(f"{len(self.words)} words read")

    def _read_file(self, file_path):
        """Read the file and return a list of words"""
        with open(file_path, "r") as file:
            return [word.strip() for word in file.readlines()]
        
    def random(self):
        return random.choice(self.words)
    

    class SpecialWordFinder:
        """Special version of WordFinder that doesn't return blank lines or comments"""

        def _read_file(self, file_path):
            """Read file, filtering out blanks and comments"""
            words = super().read_file(file_path) # Call _read_file  method from the superclass
            return [word for word in words if word and not word.startswith("#")]