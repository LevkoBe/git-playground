import words_fetcher
import random


def congratulate_user(congratulation_word):
    print("=============================")
    print(f"= Congratulations! You {congratulation_word}! =")
    print("=============================")
    print(f"Your words are: {guesses}")


def is_game_over():
    return guessed == WORDS_TO_WIN or errors == ERRORS_TO_LOSE


def guess_is_valid(candidate):
    for letter in candidate:
        count = word.count(letter)
        if count < candidate.count(letter):
            print(f"You can use letter {letter} only {count} time(s)")
            return False
    return True


guessed = 0
errors = 0

guesses = []

WORDS_TO_WIN = 5
ERRORS_TO_LOSE = 3

words = words_fetcher.fetch_words(min_letters=9, max_letters=9)
full_list = words_fetcher.fetch_words(min_letters=3, max_letters=9)
word = words[random.randrange(0, len(words))]

print(f"Can you make up {WORDS_TO_WIN} words from letters in word provided by me?")
print(f"Your word is '{word}'")


while not is_game_over():
    guess = input("Your next take: ")

    if not guess_is_valid(guess):
        continue

    if guess in guesses:
        errors += 1
        print(f"This word is already used! You have {ERRORS_TO_LOSE - errors} lives more")
    elif guess in full_list:
        guessed += 1
        guesses.append(guess)
        if guessed == WORDS_TO_WIN:
            congratulate_user("won")
            exit()
        print(f"That's right! {WORDS_TO_WIN - guessed} to go")
    else:
        errors += 1
        print(f"Oops :( No such word, you have {ERRORS_TO_LOSE - errors} lives more")
    if guesses:
        if len(guesses) == 1:
            print(f"Remember, you have used a word {str(guesses)[1:-1]}")
        elif len(guesses) > 1:
            print(f"Remember, you have used such words: {str(guesses)[1:-1]}")
congratulate_user("lose")
