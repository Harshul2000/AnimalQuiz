def check_guess(guess, answer):
    global score
    still_guessing = True
    attempt = 0
    while still_guessing and attempt < 3:
        if guess.lower() == answer.lower():
            print("Correct Answer")
            score = score + 1
            still_guessing = False
        else:
            if attempt < 2:
                guess = input("Sorry Wrong Answer, try again")
            attempt = attempt + 1
    if attempt == 3:
        print("The Correct answer is ",answer )
    
score = 0
print("Guess the Animal")
guess1 = input("Which is the largest member of the cat family? ")
check_guess(guess1, "tiger")
guess2 = input("Which is the smallest bird? ")
check_guess(guess2, "Humming bird")
guess3 = input("Which is the largest non flying bird? ")
check_guess(guess3, "Ostrich")
print("Your Score is "+ str(score))