import random

def generate_board():
    board = []
    for i in range(9):
        board.append([0] * 9)
    return board

def print_board(board):
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - -")
        for j in range(9):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")
            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")

def find_empty(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return (i, j)  # row, col
    return None

def valid(board, num, pos):
    # Check row
    for i in range(9):
        if board[pos[0]][i] == num and pos[1] != i:
            return False

    # Check column
    for i in range(9):
        if board[i][pos[1]] == num and pos[0] != i:
            return False

    # Check box
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if board[i][j] == num and (i, j) != pos:
                return False

    return True

def solve(board):
    find = find_empty(board)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1, 10):
        if valid(board, i, (row, col)):
            board[row][col] = i

            if solve(board):
                return True

            board[row][col] = 0

    return False

def remove_numbers(board):
    count = 0
    while count < 45:
        row = random.randint(0, 8)
        col = random.randint(0, 8)
        if board[row][col] != 0:
            board[row][col] = 0
            count += 1

def menu():
    print("1. Play Sudoku")
    print("2. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        play()
    elif choice == 2:
        exit()
    else:
        print("Invalid choice")
        menu()

def play():
    board = generate_board()    
    solve(board)
    remove_numbers(board)
    freezed_board = []
    for i in range(9):
        freezed_board.append([])
        for j in range(9):
            freezed_board[i].append(board[i][j])
    print("Enter 0 to exit")
    while True:
        print("\033c", end="")
        print_board(board)
        row = int(input("Enter row: "))
        if row == 0:
            exit()
        col = int(input("Enter column: "))
        if col == 0:
            exit()
        num = int(input("Enter number: "))
        if num == 0:
            exit()        
        if freezed_board[row - 1][col - 1] == 0:
            board[row - 1][col - 1] = num
        else:
            print("You can't change that number")
            input("Press enter to continue")
        if find_empty(board) == None:
            if valid(board, num, (row, col)):
                print("Congratulations, you won!")
                menu()
            else:
                print("Try again!")
                play()      

def main():
    menu()

main()