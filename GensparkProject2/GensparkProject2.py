import random

num_to_guess = random.randint(1, 101) # random number between 1 and 100

i = 1
while i < 11:
    attemptVal = int(input("Guess the number (between 1 and 100): ")) # prompt user input
    if attemptVal > num_to_guess: # if the number is less than the random number, then we tell them its too high
        print("Too high! Try again.")
    elif attemptVal < num_to_guess: # if their guess was too low, we tell them that
        print("Too low! Try again.")
    else: # if they get it right ,we tell em the number of guesses it took
        print(f"Congratulations! You guessed it in {i} attempts!")
        break
    i += 1
print("Game over! Better luck next time!")