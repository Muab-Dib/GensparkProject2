import random

num_to_guess = random.randint(1, 100)

i = 1
while i < 11:
    attemptVal = int(input("Guess the number (between 1 and 100): "))
    if attemptVal > num_to_guess:
        print("Too high! Try again.")
    elif attemptVal < num_to_guess:
        print("Too low! Try again.")
    else:
        print(f"Congratulations! You guessed it in {i} attempts!")
        break
    i += 1
print("Game over! Better luck next time!")