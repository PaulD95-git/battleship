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