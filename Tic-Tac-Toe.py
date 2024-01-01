class Player:
    def __init__(self, name, letter):
        self.name = name
        self.letter = letter

# Define players and ask for user input
player_1 = Player(input("Enter the first player's name: "), "X")
player_2 = Player(input("Enter the second player's name: "), "O")

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

    # Ensure the chosen cell is empty
    if board[row][column] == []:
        board[row][column] = player.letter
    else:
        print("Invalid move. The selected cell is already occupied. Try again.")
        player_turn(player)

def win(player):
    # Check rows
    for row in board:
        if all(cell == player.letter for cell in row):
            return True

    # Check columns
    for col in range(3):
        if all(row[col] == player.letter for row in board):
            return True

    # Check diagonals
    if all(board[i][i] == player.letter for i in range(3)) or all(board[i][2 - i] == player.letter for i in range(3)):
        return True

    return False

def is_board_full():
    for row in board:
        if any(cell == [] for cell in row):
            return False  # There is an empty cell, the board is not full
    return True  # All cells are occupied, the board is full

def check_win():
    if win(player_1):
        print(f"{player_1.name} wins!")
        return True
    elif win(player_2):
        print(f"{player_2.name} wins!")
        return True
    elif is_board_full():
        print("It's a tie!")
        return True
    else:
        return False

def game():
    print_intro()

    print(f"\nWelcome to the game {player_1.name} and {player_2.name}!")
    print(f"{player_1.name}, you'll be using {player_1.letter}, and {player_2.name}, you'll be using {player_2.letter}.")

    current_player = player_1

    while not is_winner:
        print_board()
        player_turn(current_player)
        if check_win():
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


