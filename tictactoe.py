theBoard={'top-L':' ','top-M':' ','top-R':' ','mid-L':' ','mid-M':' ','mid-R':' ','low-L':' ','low-M':' ','low-R':' '}

def printBoard(board):
    print(board['top-L']+'|'+board['top-M']+ '|' +board['top-R'])
    print('-+-+-')
    print(board['mid-L']+'|'+board['mid-M']+'|'+board['mid-R'])
    print('-+-+-')
    print(board['low-L']+'|'+board['low-M']+'|'+board['low-R'])
turn='X'
for i in range(9):
    printBoard(theBoard)
    if i>5:
        if theBoard['top-L']==theBoard['top-M'] and theBoard['top-M']==theBoard['top-R']:
            print("Winner")
            break
    while True:
        print('Turn for' + turn + 'Move on which space?')
        move=input()
        if move not in theBoard.keys() and move!=" ":
            print("Wrong input")
        else:        
            theBoard[move]=turn
            break
        if turn=='X':
            turn='O'
        else:
            turn='X'
printBoard(theBoard)