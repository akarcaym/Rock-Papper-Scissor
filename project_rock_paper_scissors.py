#Yasin Yağız Gülten 041501037
#Melis Akarçay 041501015

from random import randint

print("***********************\n")
print("1) Human (Player1) \n2) Random Player (Player2) \n3) Rule-Based Player(Player3) \n4) Statistical-Rule Learner (Player4) \n5) Statistical-Decider (Player5)\n")
print("***********************")
u_choice = int(input("Choose your decision to play: "))

if(u_choice == 1):          #Player1

    user1_count = 0
    user2_count = 0

    print("For user 1: \n Enter choice \n 0. Rock \n 1. Paper \n 2. Scissor \n")
    print("For user 2: \n Enter choice \n 0. Rock \n 1. Paper \n 2. Scissor \n")

    while user1_count < 3 and user2_count < 3:
        user1_choice = int(input("User1 turn: "))
        user2_choice = int(input("User2 turn: "))

        if(user1_choice or user2_choice > 2):
            while(user1_choice > 2 or user2_choice > 2):
                print("Invalid number. Try again.")
                if(user1_choice > 2):
                    user1_choice = int(input("User1 turn: "))
                if(user2_choice > 2):
                    user2_choice = int(input("User2 turn: "))


        if (user1_choice == user2_choice):
            print("Tie!\n")

        elif (user1_choice == 0):
            if(user2_choice == 1):
                print("User1: Rock   User2: Paper")
                print("User2 win\n" )
                user2_count = (user2_count + 1)

            elif(user2_choice == 2):
                print("User1: Rock   User2: Scissor")
                print("User1 win\n")
                user1_count = (user1_count + 1)

        elif (user1_choice == 1 ):
            if(user2_choice == 0):
                print("User1: Paper   User2: Rock")
                print("User1 win")
                user1_count = (user1_count + 1)

            elif(user2_choice == 2):
                print("User1: Paper   User2: Scissor")
                print("User2 win\n")
                user2_count = (user2_count + 1)

        elif (user1_choice == 2):
            if(user2_choice == 0):
                print("User1: Scissor   User2: Rock")
                print("User2 win\n")
                user2_count = (user2_count + 1)

            elif(user2_choice == 1):
                print("User1: Scissor   User2: Paper")
                print("User1 win\n")
                user1_count = (user1_count + 1)

        print("User1 points: ", user1_count)
        print("User2 points: ", user2_count)
        print("\n")


elif(u_choice == 2):                #Player2
    computer_count = 0
    user_count = 0

    print("Enter choice \n 0. Rock \n 1. Paper \n 2. Scissor \n")

    while user_count < 3 and computer_count < 3:
        user_choice = int(input("User turn: "))

        if (user_choice > 2):
            while (user_choice > 2):
                print("Invalid number. Try again.")
                user_choice = int(input("User turn: "))

        computer_choice = randint(0, 1000)
        if (computer_choice >= 0 and computer_choice < 333):
            computer_choice = 1
        elif (computer_choice >= 333 and computer_choice < 666):
            computer_choice = 2
        elif (computer_choice >= 666 and computer_choice <= 1000):
            computer_choice = 0

        if (user_choice == computer_choice):
            print("Tie!\n")

        elif (user_choice == 0):
            if (computer_choice == 1):
                print("User: Rock   Computer: Paper")
                print("Computer win\n")
                computer_count = (computer_count + 1)

            elif (computer_choice == 2):
                print("User: Rock   Computer: Scissor")
                print("User win\n")
                user_count = (user_count + 1)

        elif (user_choice == 1):
            if (computer_choice == 0):
                print("User: Paper   Computer: Rock")
                print("User win")
                user_count = (user_count + 1)

            elif (computer_choice == 2):
                print("User: Paper   Computer: Scissor")
                print("Computer win\n")
                computer_count = (computer_count + 1)

        elif (user_choice == 2):
            if (computer_choice == 0):
                print("User: Scissor   Computer: Rock")
                print("Computer win\n")
                computer_count = (computer_count + 1)

            elif (computer_choice == 1):
                print("User: Scissor   Computer: Paper")
                print("User win\n")
                user_count = (user_count + 1)

        print("User points: ", user_count)
        print("Computer points: ", computer_count)
        print("\n")

elif(u_choice == 3):                #Player3
    detect = False
    user_count = 0
    computer_count = 0
    first_user_count = 0  # to compare user count. To user wins or lose
    first_computer_count = 0 # to compare computer count. To computer wins or lose
    print("Enter choice \n 0. Rock \n 1. Paper \n 2. Scissor \n")

    while user_count < 3 and computer_count < 3:
        user_choice = int(input("User turn: "))

        if (user_choice > 2):
            while (user_choice > 2):
                print("Invalid number. Try again.")
                user_choice = int(input("User turn: "))

        first_computer_count = computer_count
        first_user_count = user_count

        if(detect == False):
            computer_choice = randint(0, 1000)
            if (computer_choice >= 0 and computer_choice < 333):
                computer_choice = 1
            elif (computer_choice >= 333 and computer_choice < 666):
                computer_choice = 2
            elif (computer_choice >= 666 and computer_choice <= 1000):
                computer_choice = 0

        if (user_choice == computer_choice):
            print("Tie!\n")

        elif (user_choice == 0):
            if (computer_choice == 1):
                print("User: Rock   Computer: Paper")
                print("Computer win\n")
                computer_count = (computer_count + 1)

            elif (computer_choice == 2):
                print("User: Rock   Computer: Scissor")
                print("User win\n")
                user_count = (user_count + 1)

        elif (user_choice == 1):
            if (computer_choice == 0):
                print("User: Paper   Computer: Rock")
                print("User win")
                user_count = (user_count + 1)

            elif (computer_choice == 2):
                print("User: Paper   Computer: Scissor")
                print("Computer win\n")
                computer_count = (computer_count + 1)

        elif (user_choice == 2):
            if (computer_choice == 0):
                print("User: Scissor   Computer: Rock")
                print("Computer win\n")
                computer_count = (computer_count + 1)

            elif (computer_choice == 1):
                print("User: Scissor   Computer: Paper")
                print("User win\n")
                user_count = (user_count + 1)

        print("User points: ", user_count)
        print("Computer points: ", computer_count)
        print("\n")

        if (first_user_count != user_count):  # If user wins
            if (user_choice == 0):
                computer_choice = 1
            elif (user_choice == 1):
                computer_choice = 2
            elif (user_choice == 2):
                computer_choice = 0

            detect = True

        if (first_computer_count != computer_count):  # If computer wins
            if (computer_choice == 0):
                computer_choice = 2
            elif (computer_choice == 1):
                computer_choice = 0
            elif (computer_choice == 2):
                computer_choice = 1

            detect = True


elif(u_choice == 4):                            #player4
    detect = False
    user_count = 0
    computer_count = 0
    first_user_count = 0  # to compare user count. To user wins or lose
    first_computer_count = 0  # to compare computer count. To computer wins or lose
    arr_user_choices = []

    print("Enter choice \n 0. Rock \n 1. Paper \n 2. Scissor \n")

    while user_count < 10 and computer_count < 10:
        rock_numbers = 0
        paper_numbers = 0
        scissors_numbers = 0
        user_choice = int(input("User turn: "))

        if (user_choice > 2):
            while (user_choice > 2):
                print("Invalid number. Try again.")
                user_choice = int(input("User turn: "))

        arr_user_choices.append(user_choice)

        for i in range(len(arr_user_choices)):
            if arr_user_choices[i] == 0:
                rock_numbers = rock_numbers + 1
            elif arr_user_choices[i] == 1:
                paper_numbers = paper_numbers + 1
            elif arr_user_choices[i] == 2:
                scissors_numbers = scissors_numbers + 1

        """for j in range(len(arr_user_choices)):
            print(arr_user_choices[j])"""

        prob_rock = rock_numbers / len(arr_user_choices)
        prob_paper = paper_numbers / len(arr_user_choices)
        prob_scissors = scissors_numbers / len(arr_user_choices)

        print("Rock prob:", prob_rock)
        print("Paper prob:", prob_paper)
        print("Scissors prob:", prob_scissors)

        first_computer_count = computer_count
        first_user_count = user_count

        if (detect == False):
            computer_choice = randint(0, 1000)
            if (computer_choice >= 0 and computer_choice < 333):
                computer_choice = 1
            elif (computer_choice >= 333 and computer_choice < 666):
                computer_choice = 2
            elif (computer_choice >= 666 and computer_choice <= 1000):
                computer_choice = 0

        if (user_choice == computer_choice):
            print("Tie!\n")

        elif (user_choice == 0):
            if (computer_choice == 1):
                print("User: Rock   Computer: Paper")
                print("Computer win\n")
                computer_count = (computer_count + 1)

            elif (computer_choice == 2):
                print("User: Rock   Computer: Scissor")
                print("User win\n")
                user_count = (user_count + 1)

        elif (user_choice == 1):
            if (computer_choice == 0):
                print("User: Paper   Computer: Rock")
                print("User win")
                user_count = (user_count + 1)

            elif (computer_choice == 2):
                print("User: Paper   Computer: Scissor")
                print("Computer win\n")
                computer_count = (computer_count + 1)

        elif (user_choice == 2):
            if (computer_choice == 0):
                print("User: Scissor   Computer: Rock")
                print("Computer win\n")
                computer_count = (computer_count + 1)

            elif (computer_choice == 1):
                print("User: Scissor   Computer: Paper")
                print("User win\n")
                user_count = (user_count + 1)

        print("User points: ", user_count)
        print("Computer points: ", computer_count)
        print("\n")

        if(prob_rock > prob_paper and prob_rock > prob_scissors):
            computer_choice = 1
            detect = True
        elif(prob_paper > prob_rock and prob_paper > prob_scissors):
            computer_choice = 2
            detect = True
        elif(prob_scissors > prob_rock and prob_scissors > prob_paper):
            computer_choice = 0
            detect = True

        elif(prob_rock == prob_paper and prob_rock == prob_scissors):       #Three probs same
            detect = False

        elif(prob_rock == prob_paper and prob_rock > prob_scissors):        #Rock = paper > scissors
            computer_choice = randint(0, 1000)
            if (computer_choice >= 0 and computer_choice < 500):
                computer_choice = 1
            elif (computer_choice >= 500 and computer_choice < 1000):
                computer_choice = 2
            detect = True

        elif(prob_rock == prob_scissors and prob_rock > prob_paper):        #Rock = scissors > paper
            computer_choice = randint(0, 1000)
            if (computer_choice >= 0 and computer_choice < 500):
                computer_choice = 0
            elif (computer_choice >= 500 and computer_choice < 1000):
                computer_choice = 1
            detect = True

        elif(prob_paper == prob_scissors and prob_paper > prob_rock):       #Paper = scissors > rock
            computer_choice = randint(0, 1000)
            if (computer_choice >= 0 and computer_choice < 500):
                computer_choice = 0
            elif (computer_choice >= 500 and computer_choice < 1000):
                computer_choice = 2
            detect = True

elif(u_choice == 5):
    detect = False
    user_count = 0
    computer_count = 0
    first_user_count = 0  # to compare user count. To user wins or lose
    first_computer_count = 0  # to compare computer count. To computer wins or lose
    arr_user_choices = []

    print("Enter choice \n 0. Rock \n 1. Paper \n 2. Scissor \n")

    while user_count < 10 and computer_count < 10:
        rock_numbers = 0
        paper_numbers = 0
        scissors_numbers = 0
        user_choice = int(input("User turn: "))

        if (user_choice > 2):
            while (user_choice > 2):
                print("Invalid number. Try again.")
                user_choice = int(input("User turn: "))

        arr_user_choices.append(user_choice)

        for i in range(len(arr_user_choices)):
            if arr_user_choices[i] == 0:
                rock_numbers = rock_numbers + 1
            elif arr_user_choices[i] == 1:
                paper_numbers = paper_numbers + 1
            elif arr_user_choices[i] == 2:
                scissors_numbers = scissors_numbers + 1

        prob_rock = rock_numbers / len(arr_user_choices)
        prob_paper = paper_numbers / len(arr_user_choices)
        prob_scissors = scissors_numbers / len(arr_user_choices)

        print("Rock prob:", prob_rock)
        print("Paper prob:", prob_paper)
        print("Scissors prob:", prob_scissors)

        if (detect == False):
            computer_choice = randint(0, 1000)
            if (computer_choice >= 0 and computer_choice < 333):
                computer_choice = 1
            elif (computer_choice >= 333 and computer_choice < 666):
                computer_choice = 2
            elif (computer_choice >= 666 and computer_choice <= 1000):
                computer_choice = 0

        if (user_choice == computer_choice):
            print("Tie!\n")

        elif (user_choice == 0):
            if (computer_choice == 1):
                print("User: Rock   Computer: Paper")
                print("Computer win\n")
                computer_count = (computer_count + 1)

            elif (computer_choice == 2):
                print("User: Rock   Computer: Scissor")
                print("User win\n")
                user_count = (user_count + 1)

        elif (user_choice == 1):
            if (computer_choice == 0):
                print("User: Paper   Computer: Rock")
                print("User win")
                user_count = (user_count + 1)

            elif (computer_choice == 2):
                print("User: Paper   Computer: Scissor")
                print("Computer win\n")
                computer_count = (computer_count + 1)

        elif (user_choice == 2):
            if (computer_choice == 0):
                print("User: Scissor   Computer: Rock")
                print("Computer win\n")
                computer_count = (computer_count + 1)

            elif (computer_choice == 1):
                print("User: Scissor   Computer: Paper")
                print("User win\n")
                user_count = (user_count + 1)

        print("User points: ", user_count)
        print("Computer points: ", computer_count)
        #print("\n")

        computer_choice = randint(0, 1000)
        if (computer_choice >= 0 and computer_choice < (prob_rock * 1000)):
            computer_choice = 1
            detect = True
        elif (computer_choice >= (prob_rock * 1000) and computer_choice < (prob_paper * 1000 + prob_rock * 1000)):
            computer_choice = 2
            detect = True
        elif (computer_choice >= (prob_paper * 1000 + prob_rock * 1000) and computer_choice <= 1000):
            computer_choice = 0
            detect = True

        print("\n")
