size = 3
board = []
for i in range(size):
    row = []
    for j in range(size):
        row.append(' ')
    board.append(row)

x = 0
y = 0

def display_board(board):
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.
   for i in board: 
       print(i)

def make_list_of_free_fields(board):
    # The function browses the board and builds a list of all the free squares; 
    # the list consists of tuples, while each tuple is a pair of row and column numbers.
    
    availableSpaces = []
    for i in board:
        for j in i:
            if (j == ' '):
                availableSpaces.append([i,j])
            
    print("Available spaces: ", availableSpaces)

def enter_move(board):
    # The function accepts the board's current status, asks the user about their move, 
    # checks the input, and updates the board according to the user's decision.
    avilableSpaces = make_list_of_free_fields(board)
    display_board(board)
    print('Available spaces', board, ' -----> ', avilableSpaces)
    
    x_input = input("Please enter your next move in X: ", )
    y_input = input("Please enter your next move in Y: ")
    
    x = int(x_input)
    y = int(y_input)
    
    
    isAvailable = False
    isAvailable = board[x][y] == ' '
    print('isAvailable -->', isAvailable)
    if (isAvailable == False):
        print('Selecte a different space: \n', "this is the current board", board)
    else:
        board[x][y] = "X"
        display_board(board)
    





def victory_for(board, sign):
    # The function analyzes the board's status in order to check if 
    # the player using 'O's or 'X's has won the game
    print(board)
    isWinner = False
    for i in board:
        squares = []
        current = i
        next = i + 1
        if (i == next):
            squares.clear()
        
        check_win = all(sign == n for n in squares)
        if (check_win == True):
            isWinner = True
            print('Winner', sign)
            squares.clear()
            break
            
        for j in board:
            get_position_value = board[i][j]
            squares.append(get_position_value)
            
    enter_move(board)
        
            
            
    
    


def draw_move(board):
    # The function draws the computer's move and updates the board.
    print(board)



def start_game():
    enter_move(board)
    
    



print(victory_for(board, 'X'))