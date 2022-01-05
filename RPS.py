def main():

    import random
    match = True
    print("\nWelcome to Rock, Paper, Scissors\n")
    pointsMe = 0
    pointsYou = 0

    while match == True:
        stupid = True
        valueInt = random.randrange(1,4)

        if valueInt == 1:
            valueStr = "Rock"
            
        elif valueInt == 2:
            valueStr = "PAPER"
            
        else:
            valueStr = "SCISSORS"
            
        while stupid == True:
           
            userStupidInput = input("Choose ether ROCK (1), PAPER (2), SCISSORS (3), Quit (4): ")
            

            if userStupidInput == str(1):
                stupid = False
                userValueStr = "Rock"
                
            elif userStupidInput == str(2):
                stupid = False
                userValueStr = "PAPER"
                
            elif userStupidInput == str(3):
                stupid = False
                userValueStr = "SCISSORS"

            elif userStupidInput == str(4):
                match = False
                stupid = False

            else:
                print("\nYou Idiot\n")

        if userStupidInput == str(4):
            print("weee")
            break
            
        else:
            userInput = int(userStupidInput)
            print ("\nMe: " + valueStr + " ,You: " + userValueStr)
            if valueInt == userInput:
                print ("\nOk, Again")
                
            else:
                if userInput == 2 and valueInt == 1:
                    print ("\nOne Point to YOU")
                    pointsYou = pointsYou + 1
                elif userInput == 3 and valueInt == 2:
                    print ("\nOne Point to YOU")
                    pointsYou = pointsYou + 1
                elif userInput == 1 and valueInt == 3:
                    print ("\nOne Point to YOU")
                    pointsYou = pointsYou + 1
                elif userInput == 1 and valueInt == 2:
                    print ("\nOne Point to ME")
                    pointsMe = pointsMe + 1
                elif userInput == 2 and valueInt == 3:
                    print ("\nOne Point to ME")
                    pointsMe = pointsMe + 1
                elif userInput == 3 and valueInt == 1:
                    print ("\nOne Point to ME")
                    pointsMe = pointsMe + 1
            
        print ("[Me: " + str(pointsMe) + " ,You: " + str(pointsYou) + "]\n")

    guesses = pointsYou-pointsMe
    return guesses
