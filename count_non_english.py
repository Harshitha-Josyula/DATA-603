from mrjob.job import MRJob
from spellchecker import SpellChecker
import re

# Initialize SpellChecker (this uses a built-in English dictionary)
spell = SpellChecker()
WORD_RE = re.compile(r"\b\w+\b")

class NonEnglishWordCount(MRJob):

    def mapper(self, _, line):
        for word in WORD_RE.findall(line):
            word_lower = word.lower()
            # Check if the word is not in the English dictionary
            if word_lower not in spell:
                yield word_lower, 1

    def reducer(self, word, counts):
        yield word, sum(counts)

if __name__ == "__main__":
    NonEnglishWordCount.run()
