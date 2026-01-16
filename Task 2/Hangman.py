import random
import time
WORDS_WITH_HINTS = {
    "fish": "Lives in water",
    "dark": "Opposite of light",
    "apple": "A common fruit",
    "chair": "Furniture to sit",
    "phone": "Device for calling"
}
hangman_stages = [
    """
     +---+
     |   O
     |  /|\\
     |  / \\
    ===
    """,
    """
     +---+
     |   O
     |  /|\\
     |
    ===
    """,
    """
     +---+
     |   O
     |
     |
    ===
    """,
    """
     +---+
     |
     |
     |
    ===
    """
]
LAST_LOSS_TIME = 0     # store timestamp after losing
COOLDOWN = 3 * 3600     # 3 hours in seconds
def play_game():
    global LAST_LOSS_TIME
    # Check cooldown
    current_time = time.time()
    if current_time - LAST_LOSS_TIME < COOLDOWN:
        wait = int((COOLDOWN - (current_time - LAST_LOSS_TIME)) / 60)
        print(f"You must wait {wait} minutes before playing again.")
        return
    # Pick random word + hint
    word = random.choice(list(WORDS_WITH_HINTS.keys()))
    hint = WORDS_WITH_HINTS[word]
    guessed = ["_"] * len(word)
    lives = 3
    used_letters = set()
    print("Welcome to Hangman!")
    print(f"Hint: {hint}")
    print("Word:", " ".join(guessed))
    while lives > 0 and "_" in guessed:
        guess = input("Enter a letter: ").lower()
        if not guess.isalpha() or len(guess) != 1:
            print("Enter only one valid letter!")
            continue
        if guess in used_letters:
            print("Already guessed!")
            continue
        used_letters.add(guess)
        if guess in word:
            for i, letter in enumerate(word):
                if letter == guess:
                    guessed[i] = letter
            print("Correct!")
        else:
            lives -= 1
            print("Wrong letter!")
        print(hangman_stages[lives])
        print("Word:", " ".join(guessed))
        print(f"Lives left: {lives}")
    # Win / Loss outcome
    if "_" not in guessed:
        print(" You win! The word was:", word)
    else:
        print(" You lost! The word was:", word)
        LAST_LOSS_TIME = time.time()
        print("You can try again after 3 hours.")
# Start Game
play_game()