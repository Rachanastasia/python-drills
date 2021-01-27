import random
import string
from words import words


def hangman():
    word = random.choice(words).upper()
    print(word)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()

    while len(word_letters) > 0:
        # letters used
        print('You have used these letters: ', ' '.join(used_letters))

        # display current word with correct letters and spaces
        word_list = [
            letter if letter in used_letters else '-' for letter in word
        ]
        print('Current word: ', ' '.join(word_list))

        user_letter = input('Guess a letter: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)

        elif user_letter in used_letters:
            print('You have already used that letter.')

        else:
            print("Invalid charater.")


hangman()

user_input = input('Try something: ').upper()
print(user_input)
