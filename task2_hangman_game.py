import random

# Words and hints
words = {
    "python": "A popular programming language",
    "computer": "An electronic machine used to process data",
    "internet": "A global network connecting computers",
    "keyboard": "Used to type on a computer",
    "satellite": "An object that moves around a planet",
    "elephant": "The largest land animal",
    "engineer": "A person who designs and builds things"
}

# Hangman drawings
stages = [
    """
       -----
       |   |
           |
           |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
           |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
       |   |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
      /|   |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
      /|\\  |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
      /|\\  |
      /    |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
      /|\\  |
      / \\  |
           |
    =========
    """
]

# Select random word
word = random.choice(list(words.keys()))
hint = words[word]

guessed_letters = set()
wrong_guesses = 0
max_wrong = 6

print("================================")
print("       🎮 HANGMAN GAME")
print("================================")

print("\n💡 Hint:", hint)

while wrong_guesses < max_wrong:

    # Display current word
    display = ""

    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "

    print("\nWord:", display)

    # Check win
    if all(letter in guessed_letters for letter in word):
        print("\n🎉 Congratulations!")
        print("You guessed the word:", word)
        break

    print(stages[wrong_guesses])
    print("Wrong guesses:", wrong_guesses, "/", max_wrong)

    # Take input
    guess = input("Enter a letter: ").lower()

    # Validate input
    if len(guess) != 1 or not guess.isalpha():
        print("⚠️ Please enter only one letter.")
        continue

    # Check repeated letter
    if guess in guessed_letters:
        print("⚠️ You already guessed this letter.")
        continue

    guessed_letters.add(guess)

    # Check guess
    if guess in word:
        print("✅ Correct guess!")
    else:
        wrong_guesses += 1
        print("❌ Wrong guess!")

else:
    print(stages[wrong_guesses])
    print("\n😢 Game Over!")
    print("The correct word was:", word)