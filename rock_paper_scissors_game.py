import random

def print_results(wins, losses, ties):
    print(f"Végső eredmény - Győzelmek: {wins}, Vereségek: {losses}, Döntetlenek: {ties}")
    print("Köszönjük a játékot!")

def get_computer_choice():
    return random.choice(["kő", "papír", "olló"])

def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "döntetlen"
    elif (player_choice == "kő" and computer_choice == "olló") or \
         (player_choice == "olló" and computer_choice == "papír") or \
         (player_choice == "papír" and computer_choice == "kő"):
        return "nyertél"
    else:
        return "vesztettél"

def main():
    print("Üdvözölek a Kő, Papír, Olló játékban!")

    wins = 0
    losses = 0
    ties = 0

    while True:s
        player_choice = input("Válassz karaktert: Kő, Papír, Olló -> ").lower()
        
        if player_choice not in ["kő", "papír", "olló"]:
            print("Érvénytelen választás, kérlek válassz 'kő', 'papír', vagy 'olló' közül.")
            continue

        computer_choice = get_computer_choice()
        print(f"A gép választása: {computer_choice}")
        result = determine_winner(player_choice, computer_choice)
        if result == "nyertél":
            print("Nyertél!")
            wins += 1
        elif result == "vesztettél":
            print("Vesztettél!")
            losses += 1
        else:
            print("Döntetlen!")
            ties += 1
        
        print(f"Győzelmek: {wins}, Vereségek: {losses}, Döntetlenek: {ties}")

        play_again = input("Szeretnél újra játszani? (i/n): ").lower()
        if play_again != "i":
            break

    print_results(wins, losses, ties)

if __name__ == "__main__":
    main()