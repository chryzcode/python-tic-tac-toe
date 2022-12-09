board = [' ' for x in range(10)]

def insertLetter(letter,pos): #FUNCTION FOR INSERTING A LETTER INTO BOARD.
    board[pos] = letter

def spaceIsFree(pos):          #FUNCTION FOR RETURNING THE BOARD WITH ' '.
    return board[pos] == ' '

def printBoard(board):             #THIS FUNCTION IS FOR PRINTING THE BOARD,THE TABLE IN WHICH THE TIC TAC TOE GAME IS PLAYED.
    print('   |   |   ')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])   
    print('   |   |   ')
    print('------------')
    print('   |   |   ')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |   ')
    print('------------')
    print('   |   |   ')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |   ')

def isBoardFull(board):       #IN THIS FUNCTION IF THE PLACE OF A SINGLE BOX IS FILLED IT IS COUNTED AS 1.
    if board.count(' ') > 1:
        return False
    else:
        return True

def IsWinner(b,l):           #THIS FUNCTION SHOWS THE COMBINATIONS FOR THE PLAYER TO WIN THE GAME,THE LOGIC BEHIND THE GAME.
    return ((b[1] == l and b[2] == l and b[3] == l) or
    (b[4] == l and b[5] == l and b[6] == l) or
    (b[7] == l and b[8] == l and b[9] == l) or
    (b[1] == l and b[4] == l and b[7] == l) or
    (b[2] == l and b[5] == l and b[8] == l) or
    (b[3] == l and b[6] == l and b[9] == l) or
    (b[1] == l and b[5] == l and b[9] == l) or
    (b[3] == l and b[5] == l and b[7] == l))

def playerMove():   #FUNCTION FOR MAKING THE USER TO INPUT THE POSITION THEY WANT TO PUT 'X' OR 'O'.
    run = True
    while run:
        move = input("please select a position to enter the X between 1 to 9\n")
        try:
            move = int(move)
            if move > 0 and move < 10:
                if spaceIsFree(move):
                    run = False
                    insertLetter('X' , move)
                else:
                    print('Sorry, this space is occupied')
            else:
                print('please type a number between 1 and 9')

        except:
            print('Please type a number')

def computerMove(): #THIS PROGRAM IS USER VS THE COMPUTER SO THE FOLLOWING FUNCTION IS THE MOVES THE COMPUTER CAN MAKE.
    possibleMoves = [x for x , letter in enumerate(board) if letter == ' ' and x != 0  ]
    move = 0

    for let in ['O' , 'X']:
        for i in possibleMoves:
            boardcopy = board[:]
            boardcopy[i] = let
            if IsWinner(boardcopy, let):
                move = i
                return move

    cornersOpen = []
    for i in possibleMoves:
        if i in [1 , 3 , 7 , 9]:
            cornersOpen.append(i)

    if len(cornersOpen) > 0:
        move = selectRandom(cornersOpen)
        return move

    if 5 in possibleMoves:
        move = 5
        return move

    edgesOpen = []
    for i in possibleMoves:
        if i in [2,4,6,8]:
            edgesOpen.append(i)

    if len(edgesOpen) > 0:
        move = selectRandom(edgesOpen)
        return move

def selectRandom(li):
    import random
    ln = len(li)
    r = random.randrange(0,ln)
    return li[r]

def main():
    print("Welcome to the game!")
    printBoard(board)

    while not(isBoardFull(board)):
        if not(IsWinner(board , 'O')):
            playerMove()
            printBoard(board)
        else:
            print("sorry you loose!")
            break

        if not(IsWinner(board , 'X')):
            move = computerMove()
            if move == 0:
                print(" ")
            else:
                insertLetter('O' , move)
                print('computer placed an o on position' , move , ':')
                printBoard(board)
        else:
            print("you win!")
            break




    if isBoardFull(board):
        print("Tie game")

while True:
    x = input("Do you want to play? Press y for yes or n for no (y/n)\n")
    if x.lower() == 'y':
        board = [' ' for x in range(10)]
        print('--------------------')
        main()
    else:
        break
