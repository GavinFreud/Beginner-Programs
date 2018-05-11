import random

words = ["Albatross", "Milkman", "Pennsylvania", "Tom", "Arthur"]

index = random.randint(0, len(words)-1)
#print(index)
word = words[index]
word_bool = [0] * len(word)
word_letters = ['0'] * len(word)
guesses = 5
tries = 1
#print(word)
while(1):
    print("You have ", guesses, " guesses left. Guess a letter or press . to guess the word")
    print("You have ", word_letters, " so far") 
    guess = input()
    if guess == ".":
        word_guess = input("Guess the word: ")
        if word_guess == word:
            print("Congratulations! You got the word in ", guesses, " tries!")
            quit()
        else:
            print("Incorrect!")
            guesses -= 1
    elif len(guess) != 1:
        print("Please only enter one letter or .")
        continue
    else:
        x = 0
        count = 0
        for char in word:
            if guess == char:
                if word_bool[x] == 1:
                   continue 
                word_bool[x] = 1
                count += 1
                word_letters[x] = char
            x += 1
        if count == 0:
            print("Not in the word or already guessed. Minus one guess")
            guesses -= 1
            tries += 1
    if guesses == 0:
        print("Out of guesses! Better luck next time!")
        quit()
    if ''.join(word_letters) == word:
        print("You win the game! Congrats!")
        quit()


