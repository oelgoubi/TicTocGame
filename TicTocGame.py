


# Run The GAME using the command line : python TicTocGame.py



# Initialize Variables
game = [[0,0,0],
        [0,0,0],
        [0,0,0]]

# There is only 2 players 1 and 2 by Default is 2 --> but when the game starts the player 1 
# will start
currPlayer =2



def check(row):
    if(row.count(row[0]) == len(row) and row[0] !=0 ):
        return True
    else:
        return False



def checkWin(game_matrix):
    row = []
    col2row = []
    for i in range(0,len(game_matrix)):
        for j in range(0,len(game_matrix)):
            col2row.append(game_matrix[j][i])
            row.append(game_matrix[i][j])
        
        if (check(col2row) or check(row)):
            return True
        row = []
        col2row=[]

    #check Diagonal Right
    diagR2L = []
    for i in range(len(game_matrix)-1,-1,-1):
        diagR2L.append(game_matrix[i][i])
    #check Right to Left    
    diagL2R = []
    for i in range(0,len(game_matrix)):
        diagL2R.append(game_matrix[i][i])

    if (check(diagL2R) or check(diagR2L)):
            return True




# Display and update the Game Board after each modification By the Player
def game_board(game_map,player=0,row=0,col=0, just_display=False):
    try:
        if not just_display:
            game_map[row][col]=player
        print("   0  1  2")
        for count, row in enumerate(game):
            print(count, row)

        return game_map
    except IndexError as e:
        print('Error : Make sure you input row/column as 0 1 or 2 ?', e)
    except Exception as e:
        print("Something went very wrong", e)


# Check if a player can fill a specific square 
def caseNotFree(game,row,col):
    if(game[row][col]!=0):
        return True
    else:
        return False



def changePlayer(currPlayer):
    if currPlayer == 1:
        return 2
    else:
        return 1




game = game_board(game, just_display=True)

print("----------------Hello in The Tic Toc Game--------------")




choix = input('do you wanna play : if yes enter : 1 or  0 to quit :')


while int(choix)!=1 and int(choix)!=0:
    choix = input('-------------Please if  you wanna play  enter : 1 or  0 to quit :')

while(int(choix) == 1):
    game = game_board(game, just_display=True)
    while(not checkWin(game)):
        currPlayer = changePlayer(currPlayer)
        print("Turn of the player :", currPlayer)
        row,col= map(int,input("Enter row and Col target :").split())
        while caseNotFree(game,row,col):
            print("The box you tried to mark is already marked !")
            row,col= map(int,input("Enter a new row and Col target :").split())
        game = game_board(game,player=currPlayer,row=row,col=col)
        game = game_board(game, just_display=True)
    
    print("THE WINNER is The Player", currPlayer)
    choix = input('do you wanna play again : if yes enter : 1 or  0 to quit :')





print("-------------------------------Good Bye----------------------------------")


    

# This Game Can be developed and Changing the rules of winning




