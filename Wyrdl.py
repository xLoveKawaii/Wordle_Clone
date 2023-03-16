#wyrdl.py
for guess_num in range(1,7):
    guess = input(f"\nGuess {guess_num}: ").upper()
    if guess == "SNAKE":
        print("Correct")
        break #statement break out of loop early if user guesses the right word

#Does not require explicit 'else' statement
#Code will only continues if guesses are wrong

    print("Wrong")