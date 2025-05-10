
---

# 🎮 Tic Tac Toe (Console-Based Python Game)

A simple **console-based Tic Tac Toe game** built with Python. It allows two players to take turns on a 3x3 board, entering their moves via keyboard. The game detects wins, ties, and offers an option to replay after each game session.

## 🧠 Features

* Two-player support in the terminal
* Clear demo board for position reference
* Custom choice of X or O for Player 1
* Game board display after every move
* Win detection for rows, columns, and diagonals
* Tie detection
* Replay option after each round

---

## 🖥️ Game Flow

1. Player 1 chooses X or O.
2. Players take turns selecting positions (1–9).
3. Game ends if:

   * A player wins (3 in a row, column, or diagonal)
   * All cells are filled (tie)
4. Option to play again.

---

## 📦 Project Structure

```
tic_tac_toe.py      # Main Python file with game logic
```

---

## ▶️ How to Run

1. Make sure you have Python 3 installed.

2. Save the code in a file named `tic_tac_toe.py`.

3. Run the script:

```bash
python tic_tac_toe.py
```

---

## 🎨 Sample Board Reference

The game uses a 3x3 board with numbered positions:

```
7 | 8 | 9
---------
4 | 5 | 6
---------
1 | 2 | 3
```

Players select a number (1-9) to place their mark on the corresponding spot.

---

## 🧩 How it Works

* `display_board()`: Renders the current board.
* `sample_board()`: Displays a demo board to guide input.
* `player_choice()`: Player 1 chooses X or O.
* `place_keys()`: Places a symbol on the board.
* `win_checker()`: Checks all 8 possible win conditions.
* `full_board()`: Checks if the board is full.
* `player_position_choice()`: Validates and receives the position.
* `re_game()`: Asks the player whether to replay.

---

## ❗ Example

```text
Welcome to the Tic Tac Toe
player 1: enter your playing key (X or O): X
Ready to play? (yes / no): yes
<Board is shown>
player 1
Enter the square position (1-9): 5
<Updated board shown>
player 2
Enter the square position (1-9): 1
...
player 1 wins!!!
play again? (yes / no): no
Game Over
```

---

## 📜 License

This project is licensed under the MIT License.

---
