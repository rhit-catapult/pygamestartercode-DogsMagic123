import random

num = random.randint(1,100)


count = 0
while True:
  count += 1
  user_num = int(input(" I'm thinking of a number from 1-100. Guess My Number "))
  print()
  if (user_num > num):
    print("Your number is too high guess lower" )
    print()
  elif (user_num < num):
    print("Your number is too low guess higher" )
    print()
    pass
  else:
    print (f"Congrats you won with {count} attemps")
    print()
    choice = input("play again? (y/n) ")
    num = random.randint(1,100)
    count = 0
    if choice == "n" :
      exit()


'''selct a number
start a counter from zero
create a loop that askes the user for a number
   add 1 to the counter
   ask the user to make a guess
   if the guess is too high, print "too high"
   if the guess is too low, print "too low"
   if the guess is correct, end code
   display guess counter'''
