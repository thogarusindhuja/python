#!/usr/bin/env python
# coding: utf-8

# In[1]:


import IPython.display 


# In[ ]:


# we need toimport IPython.display


# In[ ]:


#clear output is only used in python 


# In[2]:


from IPython.display import clear_output

def display_board(board):
    clear_output()
    
    print(board[7]+'|'+board[8]+'|'+board[9])
    print('-|-|-|-')
    print(board[4]+'|'+board[5]+'|'+board[6])
    print('-|-|-|-')
    print(board[1]+'|'+board[2]+'|'+board[3])
    print('-|-|-|-')


# In[13]:


test_board = ['#', 'X','O','X','O','X','O','X','O','X']
display_board(test_board)


# In[14]:


def player_input():
    
    '''''
    OUTPUT = (Player 1 marker, Player 2 marker)
    
    '''''
    
    
    marker = ''
#keep asking player 1 to choose x or o

    while marker != 'X' and marker != 'O':
        marker = input('player 1, choose X or O: ').upper()
        
    
    if marker == 'X':
        
        return ('X','O')
        
    else:
        return ('O','X')
        


# In[15]:


player1_marker , player2_marker = player_input() 


# In[16]:


player2_marker


# In[17]:


def place_marker(board, marker, position):
    board[position] = marker


# In[18]:


test_board


# In[9]:


place_marker(test_board, '$',8)
display_board(test_board)


# In[20]:


def win_check(board, mark):
   #win tic tac toe?

# all rows, and check to see if they all share the same marker?
   
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or 
    (board[4] == board[5] == board[6] == mark) or
    (board[1] == mark and board[2] == mark and board[3] == mark) or # across the bottom
    (board[7] == mark and board[4] == mark and board[1] == mark) or # down the middle
    (board[8] == mark and board[5] == mark and board[2] == mark) or # down the middle
    (board[9] == mark and board[6] == mark and board[3] == mark) or # down the right side
    (board[7] == mark and board[5] == mark and board[3] == mark) or # diagonal
    (board[9] == mark and board[5] == mark and board[1] == mark)) # diagonal
    
# all colums, check to see if marker matches
# 2 diagonals, check to see match
# you can write as first statement 
    


# In[23]:


display_board(test_board) # we need to dispay board first to check whetherboard is displaying or not
win_check(test_board,'X')


# In[24]:


import random #random module to decide randomly which player goes first

def choose_first():
    
    flip = random.randint(0,1)
    
    if flip == 0:
        return 'Player 1'
    else:
        return 'Player 2'


# In[25]:


def space_check(board, position): #function that returns a boolean including whether a space on board is freely availale or not
    
    return board[position] == ' '


# In[26]:


def full_board_check(board): #to check board is full or not
    
    for i in range(1,10): #10 is not included checking every space
        if space_check(board,i):
            return False
    return True   


# In[33]:


def player_choice(board):
    
    position = 0 # players next position and uses the function from previous step6 whether checks its or not
    
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board,position):
        position = int(input('Choose a position: (1-9)'))
    return position


# In[34]:


def replay(): # to replay if its tie or not and space still available or not
    
    choice = input("play again? Enter Yes or No")
    
    return choice == 'Yes'


# In[ ]:


# while loop to run

print('Welcome to Tic Tac Toe')

while True:

# play the game

## set everything up (board, whos first, choose markers x, o)
    the_board = ['']*10
    player1_marker,player2_marker = player_input()
    
    
    turn = choose_first()
    print(turn + ' will go first')
    
    play_game = input('Ready to play? y or n? ')
    
    if play_game == 'y':
        game_on = True
    else:
        game_on = False
        
## game play
    while game_on:
        
        if turn== 'Player 1':
        
            #show the board
            display_board(the_board)
            #choose a position
            position = player_choice(the_board)
            
            
            #place the marker on the position
            place_marker(the_board,player1_marker,position)
            
            #check if they won
            if win_check(the_board,player1_marker):
                display_board(the_board)
                print('PLAYER 1 has won!!')
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print("TIE GAME!")
                    game_on = False
                else:
                    turn = 'player 2'
                    
        else:
        
            #show the board
            display_board(the_board)
            #choose a position
            position = player_choice(the_board)
            
            
            #place the marker on the position
            place_marker(the_board,player2_marker,position)
            
            #check if they won
            if win_check(the_board,player1_marker):
                display_board(the_board)
                print('PLAYER 2 has won!!')
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print("TIE GAME!")
                    game_on = False
                else:
                    turn = 'player 1'
                    
            
           
            
            
            



    if not replay():
        break



#break out of while loop


# In[ ]:





# In[ ]:




