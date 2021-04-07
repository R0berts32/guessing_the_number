from random import randint
from art import logo



easy_level = 10
hard_level = 5 

#Making a guess
def guess_number(guess, answer, turns):
  if guess > answer:
    print("Too High!")
    return turns -1
  elif guess < answer:
    print("Too Low!")
    return turns -1
  else:
    print(f"You got the answer correct. The correct answer is {answer}")
  
#Check difficulty
def choose_level():
  answer = input("Please choose your level 'easy' or 'hard'\n ")
  if answer == 'easy':
    return easy_level
  else:
    return hard_level

def game():
  print("Welcome to Guessing The Number Game")
  print(logo)
  print("I'm thinking of a number between 1 and 100")
  answer = randint(1, 100)
  turns = choose_level()


  guess = 0

  while guess != answer:
    print(f"You have {turns} attempts to guess the number!")
    guess = int(input("Please make a guess: "))
    turns = guess_number(guess,answer,turns)
    if turns == 0:
      print("You have lost the game!")
    elif guess != answer:
      print("Please try again!")
game()