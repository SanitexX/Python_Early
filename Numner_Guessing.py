print('''

  ________                             ___________.__              _______               ___.                 
 /  _____/ __ __  ____   ______ ______ \__    ___/|  |__   ____    \      \  __ __  _____\_ |__   ___________ 
/   \  ___|  |  \/ __ \ /  ___//  ___/   |    |   |  |  \_/ __ \   /   |   \|  |  \/     \| __ \_/ __ \_  __ \
\    \_\  \  |  |  ___/ \___ \ \___ \    |    |   |   Y  \  ___/  /    |    \  |  /  Y Y  \ \_\ \  ___/|  | \/
 \______  /____/ \___  >____  >____  >   |____|   |___|  /\___  > \____|__  /____/|__|_|  /___  /\___  >__|   
        \/           \/     \/     \/                  \/     \/          \/            \/    \/     \/       
 ''')
import random

def game():
    number_list = list(range(1, 101))  # Updated range to include 100
    randomise = random.choice(number_list)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    
    # Ask for difficulty level
    difficulty = input("Choose a difficulty, Type 'easy' or 'hard': ").lower()

    # Set max_attempts based on difficulty
    if difficulty == "easy":
        max_attempts = 5
    elif difficulty == "hard":
        max_attempts = 10
    else: 
        print("Invalid Input!")
        return  # Use return to end the function instead of exit()

    attempts = 0

    while attempts < max_attempts:
        try: 
            user_guess = int(input("Enter your guess: "))
            attempts += 1

            if user_guess == randomise:
                print(f"Congratulations, you guessed the number in {attempts} attempts!")
                break
            elif user_guess > randomise:
                print("Too high!")
            else:
                print("Too low!")

            # Check if max attempts are reached
            if attempts == max_attempts:
                print(f"Sorry, you've used all {max_attempts} attempts! The correct number was {randomise}.")
        except ValueError:
            print("Please enter a valid integer.")

game()
