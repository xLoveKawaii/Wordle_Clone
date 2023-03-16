#wyrdl.py

WORD = "SNAKE"

for guess_num in range(1,7):
    guess = input(f"\nGuess {guess_num}: ").upper()
    if guess == WORD:
        print("Correct")

        break

#Classify each letter into :
#1. Correct letter in same position in secret word as guess

    correct_letters = { #Use zip() function: element by element comparisons of 2 sequences 
        letter for letter, correct in zip(guess, WORD) if letter == correct
    }

#2. Misplaced letter in secret word but different position
    #Set comprehension: Method used for creating sets in python usng elements from other iterables(lists, sets, or tuples)
    #make sure output cotains no duplicates {Use curly braces}

    misplaced_letters = set(guess) & set(WORD) - correct_letters

#3. Wrong letter that does not appear in secret word

    wrong_letters = set(guess) - set(WORD)

    #join() method joins all items in an iterable into one string
    
    print("Correct letters: ", ", ".join(sorted(correct_letters))) 
    print("Misplaced letters: ", ", ".join(sorted(misplaced_letters)))
    print("Wrong letters: ", ", ".join(sorted(wrong_letters)))
