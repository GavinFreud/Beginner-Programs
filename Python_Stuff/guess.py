import random

choice1 = int(input("Minimum number (again, only input an integer please)? "))
choice = int(input("What is the maximum number you want me to choose (only input an integer plz)? "))
#choice1 = int(input("Minimum number (again, only input an integer please)? "))
final_num = random.randint(choice1, choice)

guess = choice + 1
guessnum = 0

while guess != final_num:
  guess = int(input("What's your guess? "))
  if guess < final_num:
    print("Too Low!")
    guessnum += 1
  elif guess > final_num:
    print("Too High!")
    guessnum += 1
  else:
    guessnum += 1
    print("Congrats! You got the number within " + str(guessnum) + " tries!")
