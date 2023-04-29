from os import system

items = ["piedra", "papel", "tijera", "lagarto", "spock"]

winmoves = {
    "piedra": ["tijera", "lagarto"],
    "papel": ["piedra", "spock"],
    "tijera": ["papel", "lagarto"],
    "lagarto": ["papel", "spock"],
    "spock": ["tijera", "piedra"]
}

def decide_winner(player_1_input, player_2_input):
    print(f"El jugador 1 escribio: {player_1_input.capitalize()}")
    print(f"El jugador 2 escribio: {player_2_input.capitalize()}")
    if player_1_input == player_2_input:
        print("Empate")
    elif player_1_input in winmoves[player_2_input]:
        print("Gana el jugador 2")
    else:
        print("Gana el jugador 1")
    play_again()
    

def start_game():
    player_1_input = input("Ingresa el valor que elije el jugador 1: ").lower()
    system("cls")
    player_2_input = input("Ingresa el valor que elije el jugador 2: ").lower()
    system("cls")

    if player_1_input in items and player_2_input in items:
        decide_winner(player_1_input, player_2_input)
    else:
        print("Los inputs recibidos son erroneos, por favor intente de nuevo.")
        start_game()


def play_again():
    user_input = input("¿Quieres jugar otra vez? escribe 'si' o 'no'\n").lower()
    if user_input == "si":
        system("cls")
        start_game()
    elif user_input == "no":
        print("Muchas gracias por jugar 'El Juego de Sheldon'.")
    else:
        print("Las lentejas son buenas pero hacer esto ... Inaceptable, asi que le preguntare de nuevo.")
        play_again()


start_game()