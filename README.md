# **BATTLESHIP Game**

Battleship is a Python terminal-based game where players compete against the computer in a battle of strategic guessing. Each player’s objective is to find and sink all of the opponent's ships before their own fleet is destroyed.

This project is built using Python and runs in a terminal environment. It has been tested locally and is designed to provide an engaging and interactive gaming experience.  

---

## **Live Version**

Play the game live in the terminal [here](https://battleship-game-1-74fead82ca45.herokuapp.com).

---

## **How to Play**

Battleship is based on the classic **pen-and-paper game**, where players guess coordinates to find and sink ships hidden on a grid.

### **Gameplay Rules**
1. The board size is 5x5 by default.
2. Both the player and computer have ships randomly placed on their respective boards.
3. Ships are marked as 'S' on the player's board but hidden on the computer's board.
4. **Objective:** Sink all of the opponent's ships.
5. Players and the computer take turns guessing coordinates to hit ships.
   - Hits are marked as `'H'`.
   - Misses are marked as `'X'`.
6. Input must be valid (within grid range and not a previously guessed coordinate).

---

## **Features**

### **Current Features**
- **Random Board Generation**
   - Ships are randomly positioned on both boards at the start of the game.
   - Players cannot see the computer's ship locations.
- **Input Validation**
   - Prevents out-of-bound guesses or duplicate inputs.
   - Ensures only numeric entries are accepted for rows and columns.
- **Gameplay Mechanics**
   - Players take turns with the computer to guess positions on the opponent's board.
   - Hits and misses are displayed after each round.
   - Score is updated dynamically for hits and misses.
- **Visual Boards**
   - Displays the player's board (with ships) and the computer's board (hidden ships).
- **Turn Limits**
   - The game allows a maximum of 10 turns unless one side wins earlier.
- **End Game**
   - Game declares a winner once all ships of either player are destroyed.

### **Future Features**
- Allow players to customize board size and ship count.
- Introduce different ship sizes (e.g., 2x1 or 3x1).
- Implement a leaderboard to track scores over multiple games.

---

## **Code Design**

### **Game Board**
The board is represented as a 2D grid. Each cell can contain:
- `~`: Empty water
- `S`: A ship (visible on the player's board only)
- `H`: A hit
- `X`: A missed guess

The game manages two separate boards: one for the player and one for the computer.

### **Key Functions**
1. **`create_board(size)`**
   - Initializes the game grid with empty cells (`~`).
2. **`place_multiple_ships(board, ship_count)`**
   - Randomly places ships on the board.
3. **`check_guess(board, guess, ships)`**
   - Validates and processes each guess (hit or miss).
4. **`get_player_guess()`**
   - Ensures valid player input for guesses.
5. **`play_battleship()`**
   - Contains the main game loop.
6. **`print_board()`**
   - Displays the player's and computer's boards.

---

## **Testing**

### **Manual Testing**
- **Validated Input Handling**
   - Tested out-of-bounds inputs (e.g., negative numbers, too high) and non-numeric entries.
   - Confirmed duplicates are not accepted.
- **Game Logic**
   - Verified correct marking of hits and misses on both boards.
   - Tested edge cases for sinking ships.
- **Winning/Losing Scenarios**
   - Ensured the game ends correctly when all ships are sunk or turns run out.

### **Code Validation**
- Passed through **PEP8** linter with no errors.

---

## **Bugs**

### **Solved Bugs**
- Fixed indexing errors by ensuring ship placement respected 0-based indexing.
- Addressed validation issues for duplicate or out-of-bound guesses.

### **Remaining Bugs**
- None identified.

---

## Heroku Deployment Guide

Follow these steps to deploy your project on Heroku:


### 1. Set Up Heroku
- Go to [Heroku](https://www.heroku.com/), create an account (if needed), and log in.
- On the dashboard, click **"New"** → **"Create New App"**.
- Enter a name for your app and choose your region, then click **"Create App"**.


### 2. Add Buildpacks
- Go to the **"Settings"** tab of your app.
- Scroll to **"Buildpacks"** and add:
  1. **Python** first.
  2. **Node.js** second.


### 3. Connect GitHub Repository
- Go to the **"Deploy"** tab.
- Under **"Deployment Method"**, select **"GitHub"**.
- Find your repository and click **"Connect"**.


### 4. Deploy Your App
- **Automatic Deploys** (Optional): Enable this to auto-deploy changes.
- **Manual Deploy**: Select your branch (e.g., `main`) and click **"Deploy Branch"**.


### 5. Open Your App
- Once deployed, click **"View App"** to access your live application.

---

## **Credits**

- [Code Institute](https://codeinstitute.net/) for the deployment terminal.
- [Wikipedia](https://en.wikipedia.org/wiki/Battleship_(game)) for the Battleship game concept.