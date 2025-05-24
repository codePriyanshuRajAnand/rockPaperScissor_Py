# rock paper scissor game
from random import randint

def get_choice():
    valid_choices = {
        1: "rock",
        0: "paper",
        2: "scissor"
    }
    choices = {}
    values_input = False
    try:
        while(not values_input):
            user_choice = int(input("Enter your choice: \n1 for Rock\n0 for Paper\n2 for Scissor\n"))
            if(user_choice==1 or user_choice==0 or user_choice==2):
                choices["user_choice"] = valid_choices[user_choice]
                choices["computer_choice"] = valid_choices[randint(0,2)]
                values_input = True
            else:
                print("Please enter a valid choice: (1 for Rock; 0 for Paper; 2 for Scissor)\n")
                values_input = False    
    except:
        print("Please enter a numeric value: (1 for Rock; 0 for Paper; 2 for Scissor)\n")
    
    return choices
    

def decide_winner(user, computer):
    if(user==computer):
        return f"It's a Draw...\nYou chose {user.title()} and Computer chose {computer.title()}"
    elif((user == "paper" and computer == "rock") or (user=="rock" and computer=="scissor") or (user=="scissor" and computer=="paper")):
        return f"Hurray!!! You Won...\nYou chose {user.title()} and Computer chose {computer.title()}"
    else:
        return f"Computer Won :(\nYou chose {user.title()} and Computer chose {computer.title()}"

def play():
    play = True
    while(play):
        choices = get_choice()
        user_choice = choices["user_choice"]
        computer_choice = choices["computer_choice"]

        res = decide_winner(user_choice, computer_choice)
        print(res)
        opt = input("Want to Play more??\nEnter y for yes n for no: ")
        if(opt != "y" and opt !="yes"):
            play = False

play()            

# print(f"Computer: {computer_choice.title()} and User: {user_choice.title()}")
