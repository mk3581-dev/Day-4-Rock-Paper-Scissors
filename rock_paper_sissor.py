import random
print("Welcome to Rock, Paper, Scissors!")
rock='''---'   ____)
              (_____)
              (_____)
              (____)
        ---.__(___)'''
paper='''    _______
        ---'   ____)____
                  ______)
                  _______)
                 _______)
        ---.__________)'''

scissors=''' _______
        ---'  ____)____
                  ______)
               __________)
              (____)
        ---.__(___)'''
choices = ["rock", "paper", "scissors"]
random_choice = random.choice(choices)
user_choice = input("Enter your choice (rock, paper, scissors): ").lower()
if user_choice not in choices:
    print("Invalid choice! Please choose rock, paper, or scissors.")
else:
    print(f"Computer chose: {random_choice}")
    if user_choice == random_choice:
        print("It's a tie!")
    elif (user_choice == "rock" and random_choice == "scissors"):
        print("You win!")
        print("your choice: rock")
        print(rock)
        print("computer choice:scissors")
        print(scissors)
    elif (user_choice == "paper" and random_choice == "rock"):
        print("You win!")
        print("your choice: paper")
        print(paper)
        print("computer choice: rock")
        print(rock)
    elif (user_choice == "scissors" and random_choice == "paper"):
        print("You win!")
        print("your choice: scissors")
        print(scissors)
        print("computer choice: paper")
        print(paper)

    else:

        print("Computer wins!")
        if user_choice == "rock":
            print("your choice: rock")
            print(rock)
            print(f"computer choice: {random_choice}")
            if random_choice == "paper":
                print(paper)
            else:
                print(scissors)
        elif user_choice == "paper":
            print("your choice: paper")
            print(paper)
            print(f"computer choice: {random_choice}")
            if random_choice == "scissors":
                print(scissors)
            else:
                print(rock)
        else:
            print("your choice: scissors")
            print(scissors)
            print(f"computer choice: {random_choice}")
            if random_choice == "rock":
                print(rock)
            else:
                print(paper)