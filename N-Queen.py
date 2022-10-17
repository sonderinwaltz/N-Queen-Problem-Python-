q = int(input("Enter the number of queens: ")) #input number of queens
flag = 0
count = 0

def printSol(column, posD, negD, board, row, q): #to print the solutions using backtracking
    global flag, count #set global variables
    if row == q: #when solution is found
        count += 1 #increment count
        if (flag < 10): #stop output when flag exceeds 10
            flag += 1 #increment flag
            for row in range(q):
                for col in range(q):
                    print(board[row][col], end = " ") #print solution
                print()
            print()
    for col in range(q):
        if col in column or (row + col) in posD or (row - col) in negD:
            continue #if the current column or diagonal already has a queen
        column.add(col)
        posD.add(row + col)
        negD.add(row - col)
        board[row][col] = "1" #queen placed
        printSol(column, posD, negD, board, row + 1, q)
        column.remove(col) #resetting the board
        posD.remove(row + col)
        negD.remove(row - col)
        board[row][col] = "0" #queen removed
        
column = set() #to track columns that already have a queen
posD = set() #(r + c)
negD = set() # (r - c)
board = [["0"] * q for i in range(q)] #start with empty board
print("The first few (not more than 10) arrangements are: \n")
printSol(column, posD, negD, board, 0, q) #call function to print solutions
print("Total possible arrangements: ", count)
              
