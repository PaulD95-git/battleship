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

#Function for the computer to randomly guess
def get_computer_guess(board_size, previous_guesses):
    while True:
        # Randomly select row and column for the computer's guess
        row = random.randint(0, board_size - 1)
        col = random.randint(0, board_size - 1)
        if (row, col) not in previous_guesses:
            return row, col

# Function to check if a guess is a hit or miss
def check_guess(board, guess, ships, score, previous_guesses, is_player_turn=True):
    row, col = guess
    if guess in previous_guesses:
        # Return False if the guess was already made
        return False 

    if guess in ships:
        print("Hit!")  # A ship was hit
        ships.remove(guess)  # Remove the ship from the list
        board[row][col] = "H"  # Mark the board with "H" for hit
        score['hits'] += 1  # Increment the hit score
        previous_guesses.add(guess)
        if not ships:  # All ships have been sunk
            return True
    else:
        print("Miss!")  # The guess missed
        board[row][col] = "X"  # Mark the board with "X" for miss
        score['misses'] += 1  # Increment the miss score
        previous_guesses.add(guess)
    return False

    # Function to play the main game
def play_battleship(player_name):
    board_size = 5  # Set board size
    ship_count = 3  # Number of ships
    turns = 10  # Number of turns allowed

    # Initialize the player's board and ships
    player_board = create_board(board_size)
    player_ships = place_multiple_ships(player_board, ship_count)
    player_score = {'hits': 0, 'misses': 0}
    player_previous_guesses = set()

    # Initialize the computer's board and ships
    computer_board = create_board(board_size)
    computer_ships = place_multiple_ships(computer_board, ship_count)
    computer_score = {'hits': 0, 'misses': 0}
    computer_previous_guesses = set()

    # Display initial boards
    print(f"\nWelcome to Battleship, {player_name}!")
    print(f"Board size: {board_size}x{board_size}. Ships to sink: {ship_count}.")
    print_board(player_board, show_ships=True, label="Your Board")  
    print_board(computer_board, show_ships=False, label="Computer's Board")

    # Gameplay loop
    for turn in range(turns):
        # Player's turn
        print(f"\nTurn {turn + 1}/{turns} - Your Turn")
        guess = get_player_guess(board_size, player_previous_guesses)
        if check_guess(computer_board, guess, computer_ships, player_score, player_previous_guesses, True):
            print("Congratulations, you sunk all the computer's ships!")
            break
        print_board(player_board, show_ships=True, label="Your Board")

        # Computer's turn
        print(f"\nTurn {turn + 1}/{turns} - Computer's Turn")
        computer_guess = get_computer_guess(board_size, computer_previous_guesses)
        print(f"Computer guesses: {computer_guess[0]} {computer_guess[1]}")
        if check_guess(player_board, computer_guess, player_ships, computer_score, computer_previous_guesses, False):
            print("The computer sunk all your ships!")
            break
        print_board(player_board, show_ships=True, label="Your Board")