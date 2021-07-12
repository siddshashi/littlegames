import random
import string
from words import words

def get_valid_word(words):
    word = random.choice(words)
    while "-" in word or " " in word:
        word = random.choice(words)
    return word.upper()

def hangman():
    word = get_valid_word(words)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()
    lives = 8

    while len(word_letters) > 0 and lives > 0 :
        print("you have used these letters: ", " ".join(used_letters))
        print("you have ", lives, " lives left")

        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('current word: ', ''.join(word_list))

        user_letter = input("guess a letter: ").upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives = lives - 1
                print("sorry, that letter isn't in the word")
        elif user_letter in used_letters:
            print("you already used this letter")
        else:
            print("that's not in the alphabet")
    if lives == 0:
        print('you lost, the word was ', word)
    else:
        print('you win! the word was ', word)


hangman()