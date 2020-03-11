"""Function to fetch words."""

import random

wordlist = "wordlist.txt"


def get_random_word(min_word_length):
    ### Gets a random word from the wordlist text file using no extra memory
    num_words_processed = 0
    current_word = None

    with open(wordlist, 'r') as f:
        for word in f:
            if '(' in word or ')' in word:
                continue
            word = word.strip().lower()
            if len(word) < min_word_length:
                continue
            num_words_processed += 1
            if random.randint(1, num_words_processed) == 1:
                current_word = word

    return current_word