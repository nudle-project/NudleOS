import random
def gamesources():
    print("Welcome to Guess the Number!")
    print("Options:")
    print("1. Play the game")
    print("2. Exit")
    choice = input("Enter your choice (1 or 2): ")
    if choice == '1':
        print("Enter a number between 1 and 100:")
        number = random.randint(1, 100)
        attempts = 0
        while True:
            guess = input("Your guess: ")
            attempts += 1
            if not guess.isdigit():
                print("Please enter a valid number.")
                continue
            guess = int(guess)
            if guess < number:
                print("Too low! Try again.")
            elif guess > number:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You've guessed the number {number} in {attempts} attempts.")
                break
    elif choice == '2':
        print("Exiting...")
        exit()
