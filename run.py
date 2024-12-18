import random


# Function to create an empty game board
def create_board(size=5):
    """Create a size x size grid initialized with '~'."""
    return [["~" for _ in range(size)] for _ in range(size)]


# Function to display the game board
def print_board(board, show_ships=False, label=""):
    """Display the game board."""
    print(f"\n{label}")
    col_numbers = "   " + " ".join(str(i) for i in range(len(board[0])))
    print(col_numbers)
    for idx, row in enumerate(board):
        if show_ships:
            row_content = " ".join(row)
        else:
            row_content = " ".join(
                '~' if cell == 'S' else cell for cell in row
            )
        print(f"{idx:2} {row_content}")


# Function to place ships randomly on the board
def place_multiple_ships(board, ship_count=3):
    """Randomly place ships on the board."""
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
    """Get a valid player's guess."""
    while True:
        try:
            print(
                f"Enter a row (0-{board_size - 1}) and "
                f"column (0-{board_size - 1})."
            )
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


# Function for the computer to randomly guess
def get_computer_guess(board_size, previous_guesses):
    """Generate a random guess for the computer."""
    while True:
        # Randomly select row and column for the computer's guess
        row = random.randint(0, board_size - 1)
        col = random.randint(0, board_size - 1)
        if (row, col) not in previous_guesses:
            return row, col


# Function to check if a guess is a hit or miss
def check_guess(board, guess, ships, score, previous_guesses,
                is_player_turn=True):
    """Check if the guess hits or misses a ship."""
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
    """Play the Battleship game."""
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
    print(f"Board size: {board_size}x{board_size}.")
    print(f"Ships to sink: {ship_count}.")
    print_board(player_board, show_ships=True, label="Your Board")
    print_board(computer_board, show_ships=False, label="Computer's Board")

    # Gameplay loop
    for turn in range(turns):
        # Player's turn
        print(f"\nTurn {turn + 1}/{turns} - Your Turn")
        guess = get_player_guess(board_size, player_previous_guesses)
        if check_guess(computer_board, guess, computer_ships,
                       player_score, player_previous_guesses, True):
            print("Congratulations, you sunk all the computer's ships!")
            break
        print_board(player_board, show_ships=True, label="Your Board")

        # Computer's turn
        print(f"\nTurn {turn + 1}/{turns} - Computer's Turn")
        computer_guess = get_computer_guess(board_size,
                                            computer_previous_guesses)
        print(f"Computer guesses: {computer_guess[0]} {computer_guess[1]}")
        if check_guess(player_board, computer_guess, player_ships,
                       computer_score, computer_previous_guesses, False):
            print("The computer sunk all your ships!")
            break
        print_board(player_board, show_ships=True, label="Your Board")
        print_board(computer_board, show_ships=False,
                    label="Computer's Board")

    # Game over - reveal boards
    print("\nGame Over!")
    print_board(player_board, show_ships=True, label="Your Board")
    print_board(computer_board, show_ships=True, label="Computer's Board")
    if not computer_ships and not player_ships:
        print("It's a tie!")
    elif not computer_ships:
        print("You won!")
    elif not player_ships:
        print("You lost!")

    print(f"Final Score: {player_name} - {player_score['hits']} hits, "
          f"{player_score['misses']} misses.")
    print(f"Computer - {computer_score['hits']} hits, "
          f"{computer_score['misses']} misses.")
    return player_score['hits']


# Function to display a simplified guide
def how_to_play():
    """Display instructions for the game."""
    print("\nHow to Play Battleship:")
    print("1. Guess a row and column to attack.")
    print("2. Hits are marked as 'H'; misses are 'X'.")
    print("3. Sink all opponent's ships to win!")
    print("4. Computer takes turns guessing your ships. Good luck!")


# Main menu to start the game
def main_menu():
    """Display the main menu and handle user input."""
    print("\n" + "=" * 50)
    print(" " * 10 + "WELCOME TO BATTLESHIP" + " " * 10)
    print("=" * 50)

    player_name = input("\nEnter your name: ").strip() or "Player"

    while True:
        print("\n" + "=" * 50)
        print("1. Start Game")
        print("2. How to Play")
        print("3. Exit")
        print("=" * 50)
        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            while True:
                hits = play_battleship(player_name)
                while True:
                    replay = input("\nDo you want to play again? (yes/no): "
                                   ).strip().lower()
                    if replay == "no":
                        print(f"Thanks for playing, {player_name}! "
                              f"Final score: {hits} hits!")
                        return
                    elif replay == "yes":
                        print("Restarting the game...\n")
                        break
                    else:
                        print("Invalid input. Please type 'yes' or 'no'.")
        elif choice == "2":
            how_to_play()
        elif choice == "3":
            print(f"Goodbye, {player_name}!")
            break
        else:
            print("Invalid choice. Enter 1, 2, or 3.")


# Run the game
if __name__ == "__main__":
    main_menu()
