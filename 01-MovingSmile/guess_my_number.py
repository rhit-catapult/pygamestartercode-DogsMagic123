import random

words = ['catapult', 'funishment', 'live', "laugh", "love", "dog", "car", "cat", "money", "happiness"]


def update_display_word(guess, display_word, unknown_word):
    result = ""
    for x in range(len(display_word)):
        # print(guess, display_word, unknown_word)
        if guess == unknown_word[x]:
            result += guess
        else:
            result += display_word[x]
    return result


unknown_word = random.choice(words)
display_word = "*" * len(unknown_word)

print(display_word)
guessed_letters = []
while True:
    guess = input('Guess a letter ')
    if guess in guessed_letters:
        print("you already guessed that")
        continue
    guessed_letters.append(guess)
    display_word = update_display_word(guess, display_word, unknown_word)

    print(f" Word so far : {display_word}")
    print(f"Guesses so far {guessed_letters}")

'''
pick a random word
created display word with the correct number of *
ask user to geuss a letter 
check if letter was already geussed
loop through the random word to see if its appears 
update the display word to show the letters

unknown_word = [random.choice(words)]

'''