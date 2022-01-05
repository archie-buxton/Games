import Diceroll
import HigherOrLower
import Hangman
import RPS

def write(textFile,guesses):
    file = open(textFile, "w")
    file.write(guesses)
    file.close()

def read(textFile):
    file = open(textFile, "r")
    contents = file.read()
    print(textFile + " is " + contents)
    file.close()
    return int(contents)

def append(text,textFile):
    file = open(textFile, "a")
    file.write(text)
    file.close()

def menu():
    print("\n********MENU*********")
    print("1: Dice Roll")
    print("2: Higher Or Lower")
    print("3: Hang Man")
    print("4: Rock, Paper, Scissors")
    print("5: My High Scores")
    print("6: Quit\n")
    choice = input("Enter your choice: ")

    #identifies the users choice then plays that game
    if choice == "1":
        print("\n***Dice Roll***\n")

        textFile = "DicerollHighScores.txt" # {this section is the High score feture, please add "return guesses" at the bottom of the game
        info = read(textFile)
        guesses = Diceroll.main()
        if info > guesses:
            write(textFile,str(guesses))
        menu()
        
    elif choice == "2":
        print("\n***Higher Or Lower***\n")

        textFile = "HigherOrLowerHighScores.txt"
        info = read(textFile)
        guesses = HigherOrLower.main()
        if info > guesses:
            write(textFile,str(guesses))
            
        menu()
        
    elif choice == "3":
        print ("\n================****================");
        print ("|__| /¯\  |\ | |¯¯   |¯\/¯| /¯\ |\ |");
        print ("|  |/¯¯¯\ | \| |__|  |    |/¯¯¯\| \|");
        print ("================****================");
        textFile = "HangmanHighScores.txt" # {this section is the High score feture, please add "return guesses" at the bottom of the game
        info = read(textFile)
        guesses = Hangman.main()
        if info > guesses:
            write(textFile,str(guesses))
        menu()

    elif choice == "4":
        print("\n***Rock, Paper, Scissors***\n")

        textFile = "RPSHighScores.txt"
        info = read(textFile)
        guesses = RPS.main()
        if info < guesses:
            write(textFile,str(guesses))
            
        menu()
        
    elif choice == "5":
        print("\n***My High Scores***\n")

        textFile = "DicerollHighScores.txt"
        info = read(textFile)
        textFile = "HigherOrLowerHighScores.txt"
        info = read(textFile)
        textFile = "HangmanHighScores.txt"
        info = read(textFile)
        textFile = "RPS.txt"
        info = read(textFile)
        
        menu()
        
    elif choice == "6":
        print("Thanks For Playing!!!")
        quit()
    else:
        print("\n***Invalid Choice Try Again***")
        menu()

menu()
