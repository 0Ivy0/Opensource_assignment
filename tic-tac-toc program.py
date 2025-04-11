##################

#프로그램명: tic-tac-toc program

#작성자: 소프트웨어학부/문서연

#작성일: 2025.04.11

#프로그램 설명: 틱텍토 게임 구현 (chatGpt를 사용하였음)

###################

import random

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board, player):
    for row in board:
        if all(s == player for s in row):
            return True
    
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    
    return False

def is_full(board):
    return all(all(cell != " " for cell in row) for row in board)

def get_computer_move(board):
    empty_cells = [(r, c) for r in range(3) for c in range(3) if board[r][c] == " "]
    return random.choice(empty_cells)

def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    player, computer = "X", "O"
    
    while True:
        print_board(board)
        
        if player == "X":
            try:
                row, col = map(int, input("Enter row and column (0-2, separated by space): ").split())
                if board[row][col] != " ":
                    print("Cell already taken, try again.")
                    continue
            except (ValueError, IndexError):
                print("Invalid input, try again.")
                continue
        else:
            print("Computer's turn...")
            row, col = get_computer_move(board)
        
        board[row][col] = player
        
        if check_winner(board, player):
            print_board(board)
            print(f"{player} wins!")
            break
        
        if is_full(board):
            print_board(board)
            print("It's a draw!")
            break
        
        player = "O" if player == "X" else "X"

if __name__ == "__main__":
    tic_tac_toe()
