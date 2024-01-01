# Creates a player class for each player
class Player:
  def __init__(self, name):
    self.name = name

# Initialises the board
board = [
  [[], [], []],
  [[], [], []],
  [[], [], []],
]

# Function to print the board
def print_board():
  for row in board:
    print(row)

# Print out the introduction to the game
def intro():
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

def game():
  intro()
  
  # Define players and ask for user input
  player_1 = Player(input("Enter the first players name: "))
  player_2 = Player(input("Enter the second persons name: "))  
  
  # Prints a welcome message
  print("\nWelcome to the game {player_1_name} and {player_2_name}!".format(player_1_name = player_1.name, player_2_name = player_2.name))
  
  is_winner = False
  current_player = player_1

  while is_winner == False:
    print_board()
    if current_player == player_1:
      print("It's your turn {}!".format(player_1.name))
      input()
      current_player = player_2
    else:
      print("It's your turn {}!".format(player_2.name))
      input()
      current_player = player_1

game()

