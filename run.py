import random 

#Function to create an empty game board
def create_board(size=5):
    #Create a size x size grid initialized with "~"
    return [["~" for _ in range(size)] for _ in rnage(size)]
