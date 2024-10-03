#importing MapReduce job to find the word count.
from mrjob.job import MRJob
from spellchecker import SpellChecker
import re

# Using spellchecker to identify english and non-english words.
spell = SpellChecker()
WORD_RE = re.compile(r"\b\w+\b")

class NonEnglishWordCount(MRJob):

    def mapper(self, _, line):
        for word in WORD_RE.findall(line):
            word_lower = word.lower()
            # Check if the word is a non-English word
            if word_lower not in spell:
                yield word_lower, 1

    def reducer(self, word, counts):
        yield word, sum(counts)

if __name__ == "__main__":
    NonEnglishWordCount.run()
