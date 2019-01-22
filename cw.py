import random
def main ():

    def quest1():
    #Create a random number. Print the number.

        create_a_random_number = random.randint(0,1000)  #random number ranges from 0-1000
        print(create_a_random_number) #prints the number
    def quest2():
    #We will keep having this problem until EVERYONE gets it right without help
    #Create a function that has a loop that quits with ‘q’. If the user doesn't enter 'q', ask them to input another string.
        def escapeme(): #function that contains a loop
            escape =""
            while(True):
                if escape == 'q':
                    print("You escaped the loop") #message when user enters q
                    break
                else:
                    escape= input("Enter 'q' to exit the loop. Otherwise you never escape. ") #Tell user to enter q to break the loop
        escapeme()
    def quest3():
    #Create a function that will loop until the user enters '0'. Ask the user to enter a positive integer number.
    #Print 0 to that number and ask them again to enter a number until they enter '0'. Repeat.
        def press0toescape(): #function
            escape3=""
            pos_int=0
            while(escape3!=0):
                while(True):
                    if pos_int>0: #breaks this while loop once a positive integer is entered
                        break
                    else:
                        pos_int= int(input ("Please enter an positive integer."))
                for x in range(pos_int +1):  #for-loop
                    print(x)        #prints numbers from 0 to user input
                escape3= int(input("Would you like do this again? Enter '0' to exit. ")) #asks the user if they want to quit
                if escape3!=0:     #if they enter a non-zero number, it goes back to the for statement via the while-escape3 loop
                    pos_int = escape3

        press0toescape()
    def quest4():
    #Create a function that creates a random number. Ask the user to guess the random number.
    # Keep letting the user guess until they get it right, then quit.
    # If they don't get it right, tell them if their next guess has to be higher or lower.
        def rando():
            randomnum= random.randint(0,9)
            while(True):
                guess = int(input("Guess the random number. "))
                if (guess == randomnum):
                    print("Match")
                    break
                else:
                    if(guess>randomnum):
                        print("Go lower. ")
                    else:
                        print("Go higher. ")
        rando()


    #quest1()
    #quest2()
    quest3()
    #quest4()


if __name__ == '__main__':
    main()