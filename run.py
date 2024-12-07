import random 

#Function to create an empty game board
def create_board(size=5):
    #Create a size x size grid initialized with "~"
    return [["~" for _ in range(size)] for _ in rnage(size)]

#Function to display the game board
def print_board(board, show_ships=False, label=""):
    print(f"\n{label}")
    print("   " + " ".join(str(i) for i in range(len(board[0]))))  # Print column numbers
    for idx, row in enumerate(board):
        if show_ships:
            # Show the entire board content (including ships marked as "S")
            print(f"{idx:2} " + " ".join(row))
        else:
            # Hide ships by displaying "~" for ship positions
            print(f"{idx:2} " + " ".join('~' if cell == 'S' else cell for cell in row))

# Function to place ships randomly on the board
def place_multiple_ships(board, ship_count=3):
    ships = []
    while len(ships) < ship_count:
        # Randomly select row and column
        row = random.randint(0, len(board) - 1)
        col = random.randint(0, len(board[0]) - 1)
        if (row, col) not in ships:  # Ensure no overlapping ships
            ships.append((row, col))
            board[row][col] = "S"  # Mark the ship position on the board
    return ships

# Function to get player's guess, ensuring valid input
def get_player_guess(board_size, previous_guesses):
    while True:
        try:
            print(f"Enter a row (0-{board_size - 1}) and column (0-{board_size - 1}).")
            row = int(input("Guess Row: "))
            col = int(input("Guess Column: "))
            if 0 <= row < board_size and 0 <= col < board_size:
                if (row, col) in previous_guesses:
                    print("You already guessed there! Try again.")
                else:
                    return row, col
            else:
                print("Invalid input! Please guess within range.")
        except ValueError:
            print("Invalid input! Please enter integers.")