def main():

   word = "Jazz"
   guessed = []
   guessedword = list(len(word)*"_")
   wordaslist = list(word.lower())
   originalLives = 10
   lives = originalLives
   print("The word has " + str(len(word)) + " letters in it.")

   while True:

      if lives == 0:
         print("\nGame over.")
         break

      if guessedword == wordaslist:
         print("\nYou win, congratulations. The word was " + word)
         break

      print(" ".join(guessedword))
      print("Lives left: " + str(lives)+"\n") #the \n just adds another line
      guess = input("Guess a letter: ")

      if guess not in guessed:
         guessed.append(guess)
         if guess not in wordaslist:
            lives -=1
         else:
            for i in range(0,len(wordaslist)):
               if guess == wordaslist[i]:
                  guessedword[i] = guess
         
      else:
         print("You have already guessed that")
      
   guesses = int(len(word))+originalLives-lives
   return guesses
