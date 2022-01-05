def write():
    file = open("HighScores.txt","w")
    for i in range(10):
        file.write("This is line %d\n"%(i+1))
    file.close()

def read():
    file = open("HighScores.txt","r")
    contents = file.read()
    print(contents)
    file.close()

def append(text):
    file = open("HighScores.txt","a")
    file.write(text)
    file.close()


userInput = input("'w' to write to the file \n'r' to read from the file \n'a' to append \n Input:")
if userInput == 'w':
    write()
elif userInput == 'r':
    read()
elif userInput == 'a':
    text = input("enter some text to add to the file:\n")
    append(text)
