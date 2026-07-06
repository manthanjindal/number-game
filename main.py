import random
import time

#lives and attempts
lives = 3
attempts = 0

#welcome message
print("Loading...")
time.sleep(1)
print(".")
time.sleep(1)
print("welcome to the python number guessing game")
time.sleep(1)
print("You'll have to guess a number within a range of your choice in less than 3 attempts!")
time.sleep(3)
print("lets start")

#enter range
time.sleep(1)
print("please enter the range")
start = int(input("Starting: "))
end = int(input("Ending: "))

#get computer's choice
print("The computer is picking a number...")
time.sleep(1)
print(".")
time.sleep(1)
print(".")
time.sleep(1)
print(".")
time.sleep(1)
print("the computer has chosen a number")
computer_choice = random.randint(start,end)

while attempts < 3:
    print(f"\nYou have {lives} lives remaining!")
    player_guess = input("Enter your guess: ")

    if player_guess.isdigit():
        if (start-1) < int(player_guess) < (end+1):
            if int(player_guess) == computer_choice:
                print(f"You won!! with {lives} lives remaining")
                break
            else:
                print("\nIncorrect Guess :(\n")
                lives -= 1
                attempts += 1
        else:
            print("Please enter a number within the range!")
    else:
        print("Please enter an integer only!")

if attempts == 3:
    print(f"\nGame Over! The number was {computer_choice}.")