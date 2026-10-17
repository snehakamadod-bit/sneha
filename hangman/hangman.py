import random

# List of five predefined words
words = ["python", "apple", "computer", "school", "internet"]

# Choose one random word
secret_word = random.choice(words)

guessed_letters = []
incorrect_guesses = 0
max_incorrect_guesses = 6

print("Welcome to Hangman!")
print("Guess the word one letter at a time.")

while incorrect_guesses < max_incorrect_guesses:
    # Show guessed letters and hidden letters
    display_word = ""

    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)
    print("Incorrect guesses left:", max_incorrect_guesses - incorrect_guesses)

    # Check if the user has guessed every letter
    if "_" not in display_word:
        print("Congratulations! You guessed the word:", secret_word)
        break

    guess = input("Enter one letter: ").lower().strip()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one letter.")
    elif guess in guessed_letters:
        print("You already guessed that letter.")
    else:
        guessed_letters.append(guess)

        if guess in secret_word:
            print("Correct guess!")
        else:
            incorrect_guesses += 1
            print("Wrong guess!")

# Show a losing message if six wrong guesses were made
if incorrect_guesses == max_incorrect_guesses:
    print("\nGame over! The word was:", secret_word)