import save_file
import hangman_game


def show_menu():
    print("\n1. Spela Hangman")
    print("2. Visa de senaste 5 resultsen")
    print("3. Avsluta")


def main_program():
    while True:
        show_menu()
        val = input("\nVälj ett alternativ: ")

        if val == "1":
            hangman_game.play_hangman()
        elif val == "2":
            save_file.show_results()
        elif val == "3":
            print("Avslutar spelet.")
            break
        else:
            print("Ogiltigt val, försök igen.")


main_program()
