import pprint

# import math
# def Eval(board):
#     for row in range(0,3):
#         if board[row][0] == board[row][1] and board[row][1] == board[row][2]:
#             if board[row][0] == 'X':
#                 return 10
#             elif board[row][0] == 'O':
#                 return -10
            
#     for col in range(0,3):
#         if board[0][col] == board[1][col] and board[1][col] == board[2][col]:
#             if board[0][col] == 'X':
#                 return 10
#             elif board[0][col] == 'O':
#                 return -10
    
#     if board[0][0] == board[1][1] and board[1][1] == board[2][2]:
#          if board[0][0] == 'X':
#                 return 10
#          elif board[0][0] == 'O':
#                 return -10

#     if board[0][2] == board[1][1] and board[1][1] == board[2][0]:
#          if board[0][2] == 'X':
#                 return 10
#          elif board[0][2] == 'O':
#                 return -10 



# board = [
#      ['X','O','_'],
#      ['X','O','X'],
#      ['O','O','X']     
# ]

# print(Eval(board))



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

def isMovesLeft(board) : 
  
    for i in range(len(board)):
        for j in range(len(board)):
            if (board[i][j] == '-'):
                return True 
    return False

#! Evaluating function
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

#! max -> X(true) min -> O (false)

def minMaxL(board,player,states, limit):
     
     '''States -> cantidad de llamados recursivos que hace'''
     #TODO poner como limite cierta cantidad de states
     
     points = EvalL(board)

     if points == 1 :
          return points, states
     if points == -1:
          return points, states
     
     if isMovesLeft(board) == False:
          return 0, states
     
     if states == limit:
          return points,states
     
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
     minScore = float('inf')
     maxStates = float('inf')
     move = ()
     for row in range(len(board)):
          for col in range(len(board)):
               if board[row][col] == '-':
                    board[row][col] = player
                    if player == X:
                         score, states = minMaxL(board, False, 0, limit)
                         if score >= maxScore and states < maxStates:
                              maxScore = score
                              maxStates = states
                              move = (row,col)
                              '''Si encuentra una jugada que gana directamente hace break'''
                              if states == 0:
                                   break
                    if player == O:
                         score, states = minMaxL(board, True, 0, limit)
                         if score <= minScore and states < maxStates:
                              minScore = score
                              maxStates = states
                              move = (row,col)
                    board[row][col] = '-'
          if states == 0:
               break
                    

     board[move[0]][move[1]] = player
     # pprint.pprint(board)
     
     if maxScore == float('-inf'):
          return minScore, move
     if minScore == float('inf'):
          return maxScore,move
     
boardL = [
     ['-','-','-','X'],
     ['X','-','-','O'],
     ['O','-','-','-'],
     ['X','O','-','-']  
]

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
               return 0
          
          bestMove(board, player, limit)
          pprint.pprint(board)
          val = input('PAUSA')

          if player == O:
               player = X
          else:
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
               return 0
          
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

X, O = 'X','O'
# print(bestMove(boardL, O))
EvE(boardL,X, 1000000000000)
# PvE(boardL, X, 1000)
