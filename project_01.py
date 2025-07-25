import random

# List of words to choose from
word_list = ["python", "hangman", "computer", "programming", "developer", "code"]

# Choose a random word
word = random.choice(word_list)
guessed_letters = []
tries = 6  # Total chances

print(" Welcome to Hangman!")
print("_ " * len(word))

while tries > 0:
    guess = input("\nGuess a letter: ").lower()

    if not guess.isalpha() or len(guess) != 1:
        print(" Please enter a single valid letter.")
        continue

    if guess in guessed_letters:
        print(" You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print(" Good guess!")
    else:
        tries -= 1
        print(f" Wrong guess! You have {tries} tries left.")

    # Display current word progress
    display_word = [letter if letter in guessed_letters else "_" for letter in word]
    print(" ".join(display_word))

    # Check if player has guessed the whole word
    if "_" not in display_word:
        print("\n Congratulations! You guessed the word:", word)
        break
else:
    print("\n Game Over! The word was:", word)