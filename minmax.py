import pprint

def checkIsValid(board):
     numX = 0
     numO = 0
     for row in range(len(board)):
          for col in range(len(board)):
               if board[row][col] == 'X':
                    numX += 1
               if board[row][col] == 'O':
                    numO += 1
     if (numO < numX-1) or (numO > numX):
          return False
     else:
          return True

def search_empty(board): 
    for i in range(len(board)):
        for j in range(len(board)):
            if (board[i][j] == '-'):
                return i, j

def isMovesLeft(board): 
  
    for i in range(len(board)):
        for j in range(len(board)):
            if (board[i][j] == '-'):
                return True 
    return False

def EvalL(board):
     
    for row in range(len(board)):
          for col in range(len(board)):
               if row+1 <= 3 and col+1 <= 3:
                    if board[row][col] == board[row+1][col] and board[row+1][col] == board[row+1][col+1]:
                         if board[row][col] == X:
                              return 1
                         elif board[row][col] == O:
                              return -1
    return 0


def minMaxL(board, player, states, limit):
     
     '''States -> cantidad de llamados recursivos que hace; (con un tablero vacio tiene un maximo de )'''
     
     points = EvalL(board)

     if points == 1 :
          return points, states
     if points == -1:
          return points, states
     
     if isMovesLeft(board) == False:
          return 0, states
     
     if states == limit:
          return points,states-1 
     
     if player:
          maxEval = float('-inf')
          for row in range(len(board)):
               for col in range(len(board)):
                    if board[row][col] == '-':
                         board[row][col] = X
                         score, states = minMaxL(board,False,states+1, limit)
                         maxEval = max(score ,maxEval)
                         board[row][col] = '-'
          return maxEval, states
     
     else:
          minEval = float('inf')
          for row in range(len(board)):
               for col in range(len(board)):
                    if board[row][col] == '-':
                         board[row][col] = O
                         score, states = minMaxL(board,True,states+1,limit)
                         minEval = min(score ,minEval)
                         board[row][col] = '-'
          return minEval, states

                    
def bestMove(board, player, limit):
     
     maxScore = float('-inf')
     minScore = 1
     states = -1
     move = ()
     for row in range(len(board)):
          for col in range(len(board)):
               if board[row][col] == '-':
                    board[row][col] = player
                    if player == X:
                         score, states = minMaxL(board, False, 0, limit)
                         board[row][col] = '-'
                         if score > maxScore:
                              maxScore = score
                              move = (row,col)
                         if states == 0:
                              maxScore = score
                              move = (row, col)
                              break
                              
                    elif player == O:
                         score, states = minMaxL(board, True, 0, limit)
                         board[row][col] = '-'
                         if score < minScore: 
                              minScore = score
                              move = (row,col)
                         if states == 0:
                              minScore = score
                              move = (row, col)
                              break
          if states == 0:
               break
     
     if move == ():
          i, j = search_empty(board)
          move = (i, j)
                     
     board[move[0]][move[1]] = player
     # pprint.pprint(board)
     
     if player == X:
          return maxScore, move
     else:
          return minScore, move

#* EMPATE
boardL = [
     ['X','-','-','X'],
     ['-','-','-','O'],
     ['O','-','-','-'],
     ['X','O','-','X']  
] 


# boardL = [
#      ['X','-','-','X'],
#      ['-','X','-','O'],
#      ['O','-','O','-'],
#      ['X','O','-','X']  
# ] 

# boardL = [
#      ['-','-','-','-'],
#      ['-','-','-','-'],
#      ['-','-','-','-'],
#      ['-','-','-','-']  
# ]

def EvE(board, player, limit):
     if not checkIsValid(board):
          return False

     flag = True
     points = 0
     while flag:
          points = EvalL(board)

          if points == 1 or points == -1:
               flag = False
               break
     
          if isMovesLeft(board) == False:
               flag = False
               break
          
          bestMove(board, player, limit)
          pprint.pprint(board)
          val = input('Pulsa para continuar ')
          print('\n')

          if player == O:
               player = X
          else:
               player = O
     
     if points == 1 :
          # pprint.pprint(board)
          print('GANO X')
          return points
     
     if points == -1:
          # pprint.pprint(board)
          print('GANO O')
          return points
     
     else:
          # pprint.pprint(board) 
          print('EMPATE')
          return points
     
def PvE(board, player, limit):
     if not checkIsValid(board):
          return False

     flag = True
     points = 0
     while flag:
          points = EvalL(board)

          if points == 1 or points == -1:
               flag = False
               break
     
          if isMovesLeft(board) == False:
               flag = False
               break
          
          if player == O:
               pprint.pprint(board)
               posI = int(input('Ingrese el numero de la fila: '))
               posJ = int(input('Ingrese el numero de la columna: '))
               board[posI][posJ] = player
               player = X
               
          else:
               bestMove(board, player, limit)
               player = O
     
     if points == 1 :
          pprint.pprint(board)
          print('GANO X')
          print("")
          return points
     if points == -1:
          pprint.pprint(board)
          print('GANO O')
          print("")
          return points
     else:
          pprint.pprint(board) 
          print('EMPATE')
          return points

X, O = 'X','O'

respusta = int(input('Ingrese 1 si quiere jugar contra la maquina, 2 si quiere observar a la maquina jugar contra ella misma '))

if respusta == 1:
     PvE(boardL, X, 10000000)
else:
     EvE(boardL,X, 1000000000)