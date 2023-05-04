#Tic-Tac-Toe game
import random

key_mapping = {"Q":7, "W":8, "E":9, "A":4, "S":5, "D":6, "Z":1, "X":2, "C":3}

def greet():
    # Greet the player and explain the rules
    print("Welcome to Tic-Tac-Toe!")
    name = input("What is your name? \n")
    print(f"{name}, The board is numbered like the keyboard's number pad.")
    print("You are player 1 and will be playing against the computer as player 2.")
    print("Good luck!\n")

def display_board(board):
    # Display the board
    print(f"{board[7]}|{board[8]}|{board[9]}")
    print("-+-+-")
    print(f"{board[4]}|{board[5]}|{board[6]}")
    print("-+-+-")
    print(f"{board[1]}|{board[2]}|{board[3]}")

def player_input():
    # Ask the player to choose X or O
    marker = ""
    while marker != "X" and marker != "O":
        marker = input("Player 1, choose X or O: ").upper()
    player1 = marker
    if player1 == "X":
        player2 = "O"
    else:
        player2 = "X"
    return (player1, player2)

def place_marker(board, marker):
    position = input("Where do you want to place your marker? ").upper()
    if position in key_mapping:
        if board[key_mapping.get(position)] == " ":
            board[key_mapping.get(position)] = marker
        else:
            print("That position is already taken. Please try again.")
            place_marker(board, marker)
    else:
        print("Invalid input. Please try again.")
        place_marker(board, marker)

def computer_place_marker(board, marker):
    # Computer places a marker
    position = random.randint(1, 9)
    if board[position] == " ":
        board[position] = marker
        print(f"The computer has placed its marker at position: {position}.")
    else:
        computer_place_marker(board, marker)
    


def win_check(board, mark): 
    # Check if a player has won
    if board[7] == board[8] == board[9] == mark:
        return True
    elif board[4] == board[5] == board[6] == mark:
        return True
    elif board[1] == board[2] == board[3] == mark:
        return True
    elif board[7] == board[4] == board[1] == mark:
        return True
    elif board[8] == board[5] == board[2] == mark:
        return True
    elif board[9] == board[6] == board[3] == mark:
        return True
    elif board[7] == board[5] == board[3] == mark:
        return True
    elif board[9] == board[5] == board[1] == mark:
        return True
    else:
        return False

if __name__ == "__main__":
    greet()
    board = [" "] * 10
    display_board(board)
    player1_marker, player2_marker = player_input()
    print(f"Player 1 is {player1_marker}")
    print(f"Player 2 is {player2_marker}")

    number_of_turns = 0
    while True:
        place_marker(board, player1_marker)
        display_board(board)
        if number_of_turns >= 2:
            if win_check(board, player1_marker):
                print("Player 1 wins!")
                break
        computer_place_marker(board, player2_marker)
        display_board(board)
        if number_of_turns >= 2:
            if win_check(board, player2_marker):
                print("Player 2 wins!")
                break
        number_of_turns += 1
        if number_of_turns == 4:
            print("It's a tie!")
            break
