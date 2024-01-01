class Player:
    def __init__(self, name, letter):
        self.name = name
        self.letter = letter

def print_intro():
    print("""
░██╗░░░░░░░██╗███████╗██╗░░░░░░█████╗░░█████╗░███╗░░░███╗███████╗░░████████╗░█████╗░
░██║░░██╗░░██║██╔════╝██║░░░░░██╔══██╗██╔══██╗████╗░████║██╔════╝░░╚══██╔══╝██╔══██╗
░╚██╗████╗██╔╝█████╗░░██║░░░░░██║░░╚═╝██║░░██║██╔████╔██║█████╗░░░░░░░██║░░░██║░░██║
░░████╔═████║░██╔══╝░░██║░░░░░██║░░██╗██║░░██║██║╚██╔╝██║██╔══╝░░░░░░░██║░░░██║░░██║
░░╚██╔╝░╚██╔╝░███████╗███████╗╚█████╔╝╚█████╔╝██║░╚═╝░██║███████╗░░░░░██║░░░╚█████╔╝
░░░╚═╝░░░╚═╝░░╚══════╝╚══════╝░╚════╝░░╚════╝░╚═╝░░░░░╚═╝╚══════╝░░░░░╚═╝░░░░╚════╝░

████████╗██╗░█████╗░░░░░░░████████╗░█████╗░░█████╗░░░░░░░████████╗░█████╗░███████╗██╗
╚══██╔══╝██║██╔══██╗░░░░░░╚══██╔══╝██╔══██╗██╔══██╗░░░░░░╚══██╔══╝██╔══██╗██╔════╝██║
░░░██║░░░██║██║░░╚═╝█████╗░░░██║░░░███████║██║░░╚═╝█████╗░░░██║░░░██║░░██║█████╗░░██║
░░░██║░░░██║██║░░██╗╚════╝░░░██║░░░██╔══██║██║░░██╗╚════╝░░░██║░░░██║░░██║██╔══╝░░╚═╝
░░░██║░░░██║╚█████╔╝░░░░░░░░░██║░░░██║░░██║╚█████╔╝░░░░░░░░░██║░░░╚█████╔╝███████╗██╗
░░░╚═╝░░░╚═╝░╚════╝░░░░░░░░░░╚═╝░░░╚═╝░░╚═╝░╚════╝░░░░░░░░░░╚═╝░░░░╚════╝░╚══════╝╚═╝
    """)

def print_board():
    for row in board:
        print(row)

def player_turn(player):
    print(f"It's your turn {player.name}!")
    row = int(input("Which row do you want to play on? "))
    column = int(input("Which column do you want to play on? "))
    # Add logic to update the board based on player's input

def check_win():
    # Add logic to check for a win
    pass

def announce_winner(player):
    print(f"Congratulations, {player.name}! You've won!")

def game():
    print_intro()

    # Define players and ask for user input
    player_1 = Player(input("Enter the first player's name: "), "X")
    player_2 = Player(input("Enter the second player's name: "), "O")

    print(f"\nWelcome to the game {player_1.name} and {player_2.name}!")
    print(f"{player_1.name}, you'll be using {player_1.letter}, and {player_2.name}, you'll be using {player_2.letter}.")

    current_player = player_1

    while is_winner == False:
        print_board()
        player_turn(current_player)
        if check_win():
            announce_winner(current_player)
            break
        current_player = player_2 if current_player == player_1 else player_1


# Initialises the board
board = [
    [[], [], []],
    [[], [], []],
    [[], [], []],
]
is_winner = False

game()


