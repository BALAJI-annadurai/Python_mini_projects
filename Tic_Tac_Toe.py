#for make space between two boards
def clear_output():
    print('\n'*50)

#tic tac toe board     
def display_board(board):
    clear_output()
    print(board[7],'|',board[8],'|',board[9])
    print('-'*10)
    print(board[4],'|',board[5],'|',board[6])
    print('-'*10)
    print(board[1],'|',board[2],'|',board[3])
    
#sample board for identify the 
def sample_board():
    sample_board=['#','1','2','3','4','5','6','7','8','9']
    display_board(sample_board)
    print('Demo Board\n')
    
def player_choice():
    choice=''
    while choice!='X'or choice!='O':
        choice=input("player 1: enter your playing key( X or O ):").upper()
        if choice=='X':
            return('X','O')
        elif choice=='O':
            return('O','x')
        else:
            pass

def start_game():
    start=False
    while not start:
        choice=input("Ready to play? ( yes / no ):").lower()
        start=(choice=='yes')
    return start

def place_keys(board,choice,position):
    board[position]=choice

def win_checker(board,choice):
    return(board[7]==choice and board[8]==choice and board[9]==choice or 
           board[4]==choice and board[5]==choice and board[6]==choice or 
           board[1]==choice and board[2]==choice and board[3]==choice or 
           board[1]==choice and board[4]==choice and board[7]==choice or 
           board[2]==choice and board[5]==choice and board[8]==choice or
           board[3]==choice and board[6]==choice and board[9]==choice or 
           board[1]==choice and board[5]==choice and board[9]==choice or 
           board[3]==choice and board[5]==choice and board[7]==choice )

def empty_board_square(board,position):
    return(board[position]==' ')

def full_board(board):
    for i in range(1,10):
        if board[i]==' ':
            return False
    return True

def player_position_choice(board,player):
    position=0
    while position not in [1,2,3,4,5,6,7,8,9] or not empty_board_square(board,position):
        position=int(input(f'{player}\nEnter the square position (1-9):'))
    return position

def re_game():
    choice=' '
    while choice!='yes' and choice!='no':
        choice=input("play again ? ( Yes / No ):").lower()
    return choice=='yes'


def tic_tac_toe():
    print('Welcome to the Tic Tac Toe ')
    while True:
        
        game_board=['#']+[' ']*9   #initialize the game board
        
        clear_output()
        
        player_1,player_2=player_choice()    #selecting the players board piece choice
        
        #sample board
        sample_board()
        
        start=start_game()
        
        turn='player 1'
        
        while start :   # ask the user for start the game ?
            
            if turn =='player 1':
                
            
                #display the game board
                display_board(game_board)
            
                #position selection 
                position=player_position_choice(game_board,turn)
            
                #place the player piece in the board 
                place_keys(game_board,player_1,position)
            
                #check if player_1 wins
                if win_checker(game_board,player_1):
                    display_board(game_board)
                    print('player 1 wins!!!')
                    start=False
                    
                #check for tie    
                elif full_board(game_board):
                    display_board(game_board)
                    print('The game is Tie .')
                    start=False
                 
                #pass the move to player 2
                else:
                    turn='player 2'
                
            else:
                
            
                #display the game board
                display_board(game_board)
            
                #position selection 
                position=player_position_choice(game_board,turn)
            
                #place the player piece in the board 
                place_keys(game_board,player_2,position)
            
                #check if player_2 wins
                if win_checker(game_board,player_2):
                    display_board(game_board)
                    print('player 2 wins!!!')
                    start=False
                    
                #check for tie    
                elif full_board(game_board):
                    display_board(game_board)
                    print('The game is Tie .')
                    start=False
                 
                #pass the move to palyer 1
                else:
                    turn='player 1'
        
        # ask for replay the game
        if not re_game():
            break
    # end the game 
    print('Game Over')

tic_tac_toe()
    
