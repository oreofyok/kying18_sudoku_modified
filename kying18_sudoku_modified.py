from pprint import pprint

#PRINT BOARD IN SIMPLIER WAY
#comment from origin
def find_next_empty(puzzle): #2
    
    for r in range(9):
        for c in range(9): # range(9) is 0, 1, 2, ... 8
            if puzzle[r][c] == -1:
                return r, c
        
    return None, None  

def find_next_empty2(puzzle): #2
    
    for r in range(9):
        for c in range(9): # range(9) is 0, 1, 2, ... 8
            if puzzle[r][c] == -1:
                return r, c
        
        return None, None 


def is_valid(puzzle, guess, row, col): 
    row_vals = puzzle[row]
    
    
    if guess in row_vals:
        return False 

    col_vals = [puzzle[i][col] for i in range(9)]
    
    
    if guess in col_vals:
        return False

    row_start = (row // 3) * 3 
    col_start = (col // 3) * 3

    for r in range(row_start, row_start + 3):
        for c in range(col_start, col_start + 3):
            if puzzle[r][c] == guess:
                return False

    return True

def solve_sudoku(puzzle): #1
    global already
    # if already == False:
    #     row, col = find_next_empty(puzzle)
    # elif already == True:
    #     row,col = find_next_empty2(puzzle2)
        
    row, col = find_next_empty(puzzle)
    
    
    if row is None:  
        return True 
    
    
    for guess in range(1, 10): 
        if is_valid(puzzle, guess, row, col):
            puzzle[row][col] = guess
            if solve_sudoku(puzzle):
                return True
                
        #pprint(puzzle) ; print()
    puzzle[row][col] = -1
            
    
        
    return False

def solve_sudoku2(puzzle,used_r,used_c,used_g,puzzle2): #1
    global already
    # if already == False:
    #     row, col = find_next_empty(puzzle)
    # elif already == True:
    #     row,col = find_next_empty2(puzzle2)
        
    row, col = find_next_empty2(puzzle2)
    
    
    if row is None:  
        return True 
    
            
    while row != None:
        if len(used_c) > 0:
            last_r = list(used_r)[-1]
            last_c = list(used_c)[-1]
            last_g = list(used_g)[-1]
        pprint(puzzle2)
        print("used = ",used_g)
        print("now puzzle row = ",row," col = ",col)
        
        while True:
            guess = int(input("enter number 1-9 or 10 to backward or 100 to delete all or 500 to show unswer: "))
            if guess < 10 and guess > 0:
                break
            elif guess == 10 and len(used_r) > 0:
                puzzle2[last_r][last_c] = -1
                used_r.pop() ; used_c.pop() ; used_g.pop()
                print() ; print("BACK 1")
                solve_sudoku2(puzzle,used_r,used_c,used_g,puzzle2)
            elif guess == 10 and len(used_r) == 0:
                print("cannot go back or reset")
            elif guess == 100 and len(used_r) > 0:
                while len(used_c) > 0:
                    puzzle2[used_r[-1]][used_c[-1]] = -1
                    used_r.pop() ; used_c.pop() ; used_g.pop()
                print() ; print("RESET")
                solve_sudoku2(puzzle,used_r,used_c,used_g,puzzle2)
            elif guess == 500:
                pprint(puzzle) ; print() ; pprint(puzzle2)
            else:
                print("number must between 0-9") 
                    
        if is_valid(puzzle2,guess,row,col):
            puzzle2[row][col] = guess
            #used_dict[f"puzzle{[row]}{[col]}"] = guess
            used_r.append(row) ; used_c.append(col)
            used_g.append(guess)
            #used.get(f"puzzle{[row]}{[col]}",guess)
            if solve_sudoku2(puzzle,used_r,used_c,used_g,puzzle2):
                return True
                
        puzzle[row][col] = -1
        
    return False

if __name__ == '__main__':
    example_board = [
        [3, 9, -1,   -1, 5, -1,   -1, -1, -1],
        [-1, -1, -1,   2, -1, -1,   -1, -1, 5],
        [-1, -1, -1,   7, 1, 9,   -1, 8, -1],

        [-1, 5, -1,   -1, 6, 8,   -1, -1, -1],
        [2, -1, 6,   -1, -1, 3,   -1, -1, -1],
        [-1, -1, -1,   -1, -1, -1,   -1, -1, 4],

        [5, -1, -1,   -1, -1, -1,   -1, -1, -1],
        [6, 7, -1,   1, -1, 5,   -1, 4, -1],
        [1, -1, 9,   -1, -1, -1,   2, -1, -1]
    ]
    
    example_board2 = [
        [3, 9, -1,   -1, 5, -1,   -1, -1, -1],
        [-1, -1, -1,   2, -1, -1,   -1, -1, 5],
        [-1, -1, -1,   7, 1, 9,   -1, 8, -1],

        [-1, 5, -1,   -1, 6, 8,   -1, -1, -1],
        [2, -1, 6,   -1, -1, 3,   -1, -1, -1],
        [-1, -1, -1,   -1, -1, -1,   -1, -1, 4],

        [5, -1, -1,   -1, -1, -1,   -1, -1, -1],
        [6, 7, -1,   1, -1, 5,   -1, 4, -1],
        [1, -1, 9,   -1, -1, -1,   2, -1, -1]
    ]
    mode = input("select mode 1.auto 2.manual: ")
    used_r = [] ; used_c = [] ; used_g = []
    already = False
    
    ss = solve_sudoku(example_board)
    
    if mode == "1":
        if ss == True:
            print("solve = CLEARED")
            pprint(example_board)
        elif ss == False:
            print("this sodoku can't be solved")
    elif mode == "2":
        if ss == True:
            ss2 = solve_sudoku2
            ss2(example_board,used_r,used_c,used_g,example_board2)
        elif ss == False:
            print("this sodoku can't be solved")
        
    
    

#SUDOKU
############################################################
# OPTIONAL HELPER FUNCTIONS
############################################################

def find_next_empty(puzzle):
    # finds the next row, col on puzzle that's not filled yet --> we represent these with -1
    # returns a row, col tuple (or (None, None) if there is none)
    pass

def is_valid(puzzle, guess, row, col):
    # figures out whether the guess at the row/col of the puzzle is a valid guess
    # returns True or False
    pass

############################################################
# SOLVER IMPLEMENTATION
############################################################

def solve_sudoku(puzzle):
    # solve sudoku using backtracking!
    # our puzzle is a list of lists, where each inner list is a row in our sudoku puzzle
    # return solution

    # step 1: choose somewhere on the puzzle to make a guess
    # step 1.1: if there's nowhere left, then we're done because we only allowed valid inputs
    # step 2: if there is a place to put a number, then make a guess between 1 and 9
    # step 3: check if this is a valid guess
    # step 3.1: if this is a valid guess, then place it at that spot on the puzzle
    # step 4: then we recursively call our solver!
    # step 5: it not valid or if nothing gets returned true, then we need to backtrack and try a new number
    # step 6: if none of the numbers that we try work, then this puzzle is UNSOLVABLE!!
    pass
