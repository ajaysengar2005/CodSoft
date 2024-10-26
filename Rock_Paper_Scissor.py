import random
Rock = """
      ______
-----!   ___)
        (_____)
        (_____)
        (____)
------!(____)

"""
Paper = """
      ______
-----!   ___)____
         ________)_
         __________)
         _________)
------!________)

"""
Scissor = """
      ______
-----!   ___)____
         ________)_
         __________)
        (____)
------!(____)

"""
def play_game():
     
     user_score = 0
     computer_score = 0
     while True :
        print("Choose : ")
        print("0.Rock")
        print("1.Paper")
        print("2.Scissor\n")
       
        images = [Rock,Paper,Scissor]
        choices = ["Rock","Paper","Scissor"]
        user_choice = int(input("Enter Choice : "))
        if user_choice > 2 and user_choice < 0:
            print("Invalid Choice ")
        else:
            print(f"You Choose : {choices[user_choice]}")
            print(f"{images[user_choice]}")
            computer_choice = random.randint(0,2)
            print(f"Computer Choose : {choices[computer_choice]}")
            print(f"{images[computer_choice]}")

            print("\n")

            if user_choice == computer_choice :
                print("Match Tie ")
            elif user_choice == 0 and computer_choice == 2 :
                print("You Win")
                user_score += 1
            elif user_choice == 2 and computer_choice == 1 :
                print("You Win")
                user_score += 1
            elif user_choice == 1 and computer_choice == 0 :
                print("You Win")
                user_score += 1
            else : 
                print("Computer Win")
                computer_score += 1
            print("\n")
            print(f"Current Score :-\nYour Score : {user_score}\tComputer Score : {computer_score}")

            print("\n")
            print("Do You Want To Play Again \n1.Yes\n2.No ")
            play_again = int(input("Enter : "))
            print("\n")
            if play_again != 1 : 
                break

play_game()



    


 
