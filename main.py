import random

#lives and attempts
lives = 3
attempts = 0

#enter range
print("please enter the range")
start = int(input("Starting: "))
end = int(input("Ending: "))

#get computer's choice
computer_choice = random.randint(start,end)

#get player's choice
while attempts<3:
    print(f"\nYou have {lives} lives remaining! ")
    player_guess = int(input("Enter your guess: "))
    if player_guess == computer_choice:
        print(f"You won!! with {lives} lives remaining")
        break
    else:
        print("Incorrect Guess:(\ntry again")
        lives -= 1
        attempts += 1
