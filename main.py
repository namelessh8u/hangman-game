import random
from words import words_ru, words_eng
from display import display_hangman


def is_english():
    print('\n- If you want to play with the English words, type "eng".')
    print('- If you want to play with the Russian words, type "ru".')
    while True:
        lang = input()
        if lang == 'eng':
            return True
        elif lang == 'ru':
            return False
        else:
            print('Incorrect input. Type "eng" or "ru".')


def get_word():
    random_word = random.choice(words_list).lower
    return random_word()


def get_input(guessed_letters):
    print('Enter a letter or the whole word:')
    while True:
        user_input = input().lower()
        if user_input.isalpha():
            if user_input not in guessed_letters:
                return user_input
            print(f'You have already entered "{user_input}". Try another one.')
        else:
            print('Incorrect input.')


def play(word):
    word_completion = '_' * len(word)
    guessed = False
    guessed_letters = []
    tries = 0
    while (not guessed) and (tries < 5):
        print(display_hangman(tries))
        print(word_completion)
        user_guess = get_input(guessed_letters)
        guessed_letters.append(user_guess)
        if user_guess == word:
            guessed = True
        elif user_guess in word:
            print(f'Great! The letter "{user_guess}" is really in the word')
            word_completion, guessed = compare_words(user_guess, word, word_completion)
        else:
            print('Unfortunately, there is no such letter in the word.')
            tries += 1
    if guessed:
        print(f'Congratulations! Indeed, that was the "{word}" word.')
    else:
        print(display_hangman(tries))
        print(f'Sadly, you lost. That was the word "{word}".')


def compare_words(user_guess, word, word_completion):
    for i in range(len(word)):
        if user_guess == word[i]:
            word_completion = word_completion[:i] + user_guess.upper() + word_completion[i+1:]
    return word_completion, '_' not in word_completion


print(True if 'e' in 'abcd' else False)
print('Welcome to the Hangman Game!')
if is_english():
    words_list = words_eng
else:
    words_list = words_ru
while True:
    play(get_word())
    print('Would you like to play again??\ny/n?')
    if input() != 'y':
        break
print('Bye!')
