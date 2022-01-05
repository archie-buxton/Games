def main():

   import random
   replay = True
   highScore = 100

   while replay == True:
      
      guesses = 1
      number = random.randint(1,10)
      print ("The number is between 1-10")
      user_input=int(input("Please choose a number between 1 and 10: "))
      
      while user_input != number:

         if user_input > number:
            guesses +=1
            user_input=int(input("Too big, choose a smaller number: "))

         else:
            guesses +=1
            user_input=int(input("Too small, choose a bigger number: "))

      if guesses < highScore:
            highScore = guesses
      
      print ("Congratulations, it took you " + str(guesses) + " guess(es)")
      
      playAgain=input("Would you like to play again (True or False?) ")

      while playAgain != "True" and playAgain != "False":
         playAgain=input("Please type True or False: ")
         
      if playAgain == "True":
         replay = True

      elif playAgain == "False":
         replay = False
         
   print("awwww, see you next time. Your high score was " + str(highScore))

   return guesses
