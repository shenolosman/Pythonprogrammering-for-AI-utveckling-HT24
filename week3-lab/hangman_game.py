import random
import save_file

word_list = [
    "hangman",
    "python",
    "responsibility",
    "game",
    "program",
    "selection",
    "penalty",
    "magazine",
    "decision",
    "agreement",
    "collection",
]


def play_hangman():
    word = random.choice(word_list)
    right_word = ["_"] * len(word)
    guessed_letters = []
    fault = 0

    max_fault = len(word) - 1
    fault = 0

    while True:
        print("\nOrd: ", " ".join(right_word))
        print(f"Gissade bokstäver: {', '.join(guessed_letters)}")
        print(f"Antal fel: {fault}/{max_fault}")

        guess = input("Gissa en bokstav: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Vänligen gissa en enda bokstav.")
            continue

        if guess in guessed_letters:
            print("Du har redan gissat denna bokstav.")
            continue

        guessed_letters.append(guess)

        if guess in word:
            for index, letter in enumerate(word):
                if letter == guess:
                    right_word[index] = letter
            print(f"Bra! {guess} finns i ordet!")
        else:
            fault += 1
            print(f"Tyvärr, {guess} finns inte i ordet.")

        if "_" not in right_word: #
            print(f"Grattis! Du gissade rätt ord: {word}")
            save_file.save_results(f"Vinst - Ord: {word} - fault: {fault}")
            break
        elif fault >= max_fault:
            print(f"Game Over! Ordet var: {word}")
            save_file.save_results(f"Förlust - Ord: {word} - fault: {fault}")
            break
