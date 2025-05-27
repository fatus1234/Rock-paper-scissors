import random

user = 0
computer = 0
options = ["ROCK","PAPER","SCISSORS"]

found = False
count = 0
print("--------WELCOME TO OUR LITTLE GAME--------")
print("ARE YOU READY: TYPE YES TO START OR Q TO QUIT")
print("YOU HAVE THREE CHANCES."
    " THE SIDE WITH MORE SCORE WINS")
question = input("ANSWER: ").lower()
while question != "q":
    game = random.choice(options)
   
    count +=1
    
    if question == "q":
        break
    
    elif question == "yes" or question == "yh" or question == "yeah":


        # print("CHOOSE THE NUMBER TO PLAY")
        options = ["ROCK","PAPER","SCISSORS"]
        for idx,v in enumerate(options,1):
            print(idx,  v)
        user_input = input("Enter option: ").upper()
        if user_input in options:
            found = True
            if user_input == game:
                print("IT IS A TIE")
                
                user += 0
                print(f"Computer score: {computer}"
                      f"\nUser score: {user}")
                
            elif user_input == "SCISSORS" and game == "PAPER":
                print("USER WINS")
                user +=1
                print(f"Computer score: {computer}"
                      f"\nUser score: {user}")
                
            elif user_input == "SCISSORS" and game == "ROCK":
                print("COMPUTER WINS")
                computer +=1
                print(f"Computer score: {computer}"
                      f"\nUser score: {user}")
                
            elif user_input == "ROCK" and game == "PAPER":
                print("COMPUTER WINS")
                computer +=1
                print(f"Computer score: {computer}"
                      f"\nUser score: {user}")
                
            elif user_input == "ROCK" and game == "SCISSORS":
                print("USER WINS")
                user +=1
                print(f"Computer score: {computer}"
                      f"\nUser score: {user}")
                
            elif user_input == "PAPER" and game == "SCISSORS":
                print("COMPUTER WINS")
                computer +=1
                print(f"Computer score: {computer}"
                      f"\nUser score: {user}")
                
            elif user_input == "PAPER" and game == "ROCK":
                print("USER WINS")
                user +=1
                print(f"Computer score: {computer}"
                      f"\nUser score: {user}")
            # print("okay")



    if user_input not in options:
        print("NOT FOUND")
        print("SINCE IT IS NOT FOUND THERE'S NO SCORE")
        print(f"Computer score: {computer}"     
              f"\nUser score: {user}")
    if count == 3:
        if computer > user:
            print("Computer wins")
        else:
            print("Computer wins")
        print("EXHAUSTED ALL OPTOINS")
        print("THANK YOU!")

        
    redeem = input("Should we play again? ").lower()
    if redeem == "yes" or redeem == "yeah":
            user = 0
            computer = 0
            count = 0
            question == "yes"
    if count == 3:
            break
    else:
            break
