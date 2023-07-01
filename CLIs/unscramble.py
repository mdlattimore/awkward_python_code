import itertools
import argparse
import sys
import time

"""
This is a CLI that takes a single positional string argument, creates a list of all possible permutations, and checks that list against a dictionary (an external text file containing a little over 300,000 words, each separated by a new line), printing the permutations that match words in the dictionary to the screen. 

The arguments must be bewteen 3 and 10 characters, inclusive. The lower limit is simply a matter of common sense. Unscrambling a two character string is hardly challenging. The upper limit is set out of concern for functionality. The program creates a list in memory of permutations of the argument and then checks each member of that list against a 300k+ word dictionary (also loaded into memory). The number of permutations increases exponentially with each added character to the argument. Mathematically the number of permutations equal factorial of the length of the argument (!len(argument)). While no formal speed testing has been conducted as of yet, trial and error on am M1 MacBook Air (16GB RAM) has shown that arguments in excess of 8 characters show a perceptible slowdown, arguments of 10 characters show a more  noticeable delay between hitting the 'return' button and display of the result. 11 character arguments yield a delay of several seconds. 12 character arguments won't process at all (either because of a memory error or time-out settings in the terminal). By way of illustration of the exponential growth of permutations, the number of permutations for 12 characters is 120 times that for 10 characters, placing an enormous burden on system resources.
"""

def load_words():
    with open('/Users/mark/py_dev/word_unscrambler/words_sorted_10_or_less.txt') as word_file:
        valid_words = set(word_file.read().split())
    return valid_words

# Set up CLI
start = time.perf_counter()
parser = argparse.ArgumentParser(
    prog="Word Unscrambler",
    description="Takes a string of letters and checks all possible permutations against a dictionary of words. \
        This app only unscrambles a single word at a time. \
        Word length must be between 3 and 10 letters, inclusive."
)
parser.add_argument("word", type=str, help="A string of letters with no spaces. Word length must be between 3 and 10 letters, inclusive.",)
args = parser.parse_args()
#----


if len(args.word) > 10 or len(args.word) < 3:
    print("Words must be between 3 and 10 letters.")
    sys.exit()

letter_list = [char for char in args.word]

word_lists = itertools.permutations(letter_list)

english_words = load_words()

possible_words = ["".join(word) for word in word_lists]

correct_answers = {word for word in possible_words if word in
                    english_words}

if not correct_answers:
    print()
    print("Sorry. No word found")
    print()
else:
    print()
    for answer in correct_answers:
        print(answer)
    print()
stop = time.perf_counter()
print(f"Total time: {stop - start}")