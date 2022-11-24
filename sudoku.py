base  = 3
side  = base*base

# pattern for a baseline valid solution
def pattern(r,c): return (base*(r%base)+r//base+c)%side

# randomize rows, columns and numbers (of valid base pattern)
from random import sample
def shuffle(s): return sample(s,len(s))

rBase = range(base) 
rows  = [ g*base + r for g in shuffle(rBase) for r in shuffle(rBase) ] 
cols  = [ g*base + c for g in shuffle(rBase) for c in shuffle(rBase) ]
nums  = shuffle(range(1,base*base+1))

# produce board using randomized baseline pattern
board = [ [nums[pattern(r,c)] for c in cols] for r in rows ]

squares = side*side
empties = 17
for p in sample(range(squares),empties):
    board[p//side][p%side] = 0

numSize = len(str(side))
def game():
    for line in board:
        print(*(f"{n or '.':{numSize}} " for n in line))   



def menu():
    print("Selamat datang ke Sudoku!")
    print("1. Main Sudoku")
    print("2. Keluar")
    choice = int(input("Masukkan pilihan anda: "))
    if choice == 1:
        play()
    elif choice == 2:
        exit()
    else:
        print("Masukkan 1 atau 2 sahaja! Sila input sekali lagi")
        menu()

def play():
    while True:
        game()
        row = int(input("Enter row: "))
        if row == int(0) or row > int(10):
            print("Barisan(row) " + str(row) + " does not exist. Please enter a valid row from 1-9 instead.")
            play() 
        col = int(input("Enter column: "))
        if col == 0 or col > 10:
            print("Column " + str(col) + " does not exist. Please enter a valid column from 1-9 instead.")
            play() 
        num = int(input("Enter number: "))

        
        if num < 10 and num !=0 :
            board[row-1][col-1] = num
            has_dups_row = any(f == s != 0 for f, s in zip(sorted(board[row-1])[:-1], sorted(board[row-1])[1:]))
            has_dups_col = any(f == s != 0 for f, s in zip(sorted(board[col-1])[:-1], sorted(board[col-1])[1:]))
            dups_vals_row = sorted(set(f for f, s in zip(sorted(board[row-1])[:-1], sorted(board[row-1])[1:]) if f == s))
            dups_vals_col = sorted(set(f for f, s in zip(sorted(board[col-1])[:-1], sorted(board[col-1])[1:]) if f == s))
            if has_dups_row == True or has_dups_col == True:
                print(dups_vals_row)
                print(dups_vals_col)
                print("You are inserting repeated numbers!")
                board[row-1][col-1] = "."
        else: 
            print("Invalid Input")


menu()
