import random

def hangman():
    
    word_list = ['python', 'internship', 'satisfy', 'amazing', 'codealpha']
    
   
    word_to_guess = random.choice(word_list)
    
   
    guessed_word = ['_'] * len(word_to_guess)
    
    guessed_letters = []  
    attempts_left = 6  

    print("Welcome to Hangman!")
    print(f"The word has {len(word_to_guess)} letters.")
    print(" ".join(guessed_word))  
    
    
    while attempts_left > 0 and '_' in guessed_word:
        

        guess = input(f"\nYou have {attempts_left} attempts left. Guess a letter: ").lower()
        
        
        # if len(guess) != 1 or not guess.isalpha():
        #     print("Please enter a valid single letter.")
        #     continue

        
        if guess in guessed_letters:
            print("You've already judged that letter. Guess another one.")
            continue

        
        guessed_letters.append(guess)

        
        if guess in word_to_guess:
            print(f"Good guess! {guess} is in there.")
        
            for i in range(len(word_to_guess)):
                if word_to_guess[i] == guess:
                    guessed_word[i] = guess
        else:
            
            attempts_left -= 1
            print(f"Oops! {guess} is not in the word.")
        
        print(" ".join(guessed_word))
    
    if '_' not in guessed_word:
        print(f"\nCongratulations! You've guessed the right word: {word_to_guess}")
    else:
        print(f"\nSorry, you lost! The word was: {word_to_guess}")


hangman()
