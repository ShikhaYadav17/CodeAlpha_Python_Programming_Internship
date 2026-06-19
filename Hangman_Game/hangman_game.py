import random

# List of predefined words
words = ["python", "computer", "program", "science", "network"]

# Select a random word
word = random.choice(words)

guessed_letters = []
incorrect_guesses = 0
max_incorrect_guesses = 6

print("=" * 40)
print("      WELCOME TO HANGMAN GAME")
print("=" * 40)

while incorrect_guesses < max_incorrect_guesses:

    # Display the word with guessed letters
    display_word = ""

    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)
    print("Guessed Letters:", " ".join(guessed_letters))
    print("Incorrect Guesses Left:",
          max_incorrect_guesses - incorrect_guesses)

    # Check if player has guessed the word
    if "_" not in display_word:
        print("\n🎉 Congratulations!")
        print("You guessed the word:", word)
        break

    guess = input("\nEnter a letter: ").lower()

    # Validate input
    if len(guess) != 1 or not guess.isalpha():
        print("⚠ Please enter a single alphabet letter.")
        continue

    if guess in guessed_letters:
        print("⚠ You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess not in word:
        incorrect_guesses += 1
        print("❌ Wrong guess!")
    else:
        print("✅ Correct guess!")

else:
    print("\n❌ Game Over!")
    print("The correct word was:", word)

print("\nThank you for playing Hangman!")