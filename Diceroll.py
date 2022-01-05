def main():

    import random
    guesses = 1
    rolled_num = random.randint(1,6)
    print("The number is between 0-6")

    user_input=int(input("Enter number here: "))

    while user_input != rolled_num:
        if user_input < 1:
            user_input = int(input("Too small: "))
        
        elif user_input > 6:
            user_input = int(input("Too Big: "))

        else:
            user_input = int(input("Wrong: "))

        guesses = guesses +1

    if guesses == 1:
        print("Correct, it took you " + str(guesses) + " guess")

    else:
        print("Correct, it took you " + str(guesses) + " guesses")

    return guesses
