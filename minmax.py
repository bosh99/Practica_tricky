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

ple, cont = 'O','X'

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
  
    for i in range(4) :
        for j in range(4) :
            if (board[i][j] == '-') :
                return True 
    return False

#! Evaluating function
def EvalL(board):
     
    for row in range(len(board)):
          for col in range(len(board)):
               if row+1 <= 3 and col+1 <= 3:
                    if board[row][col] == board[row+1][col] and board[row+1][col] == board[row+1][col+1]:
                         if board[row][col] == ple:
                              return 1
                         elif board[row][col] == cont:
                              return -1
    return 0

#! max -> X(true) min -> O (false)

def minMaxL(board,player,states):
     points = EvalL(board)

     if points == 1 :
          # pprint.pprint(board)
          # print('GANO X')
          # print("")
          return points
     if points == -1:
          # pprint.pprint(board)
          # print('GANO O')
          # print("")
          return points
     
     if isMovesLeft(board) == False:
          return 0
     
     if player:
          maxEval = float('-inf')
          for row in range(len(board)):
               for col in range(len(board)):
                    if board[row][col] == '-':
                         board[row][col] = ple
                         maxEval = max(minMaxL(board,False,states+1),maxEval)
                         board[row][col] = '-'
          return maxEval
     
     else:
          minEval = float('inf')
          for row in range(len(board)):
               for col in range(len(board)):
                    if board[row][col] == '-':
                         board[row][col] = cont
                         minEval = min(minMaxL(board,True,states+1),minEval)
                         board[row][col] = '-'
          return minEval

                    
def bestMove(board, player):
     
     maxScore = float('-inf')
     move = ()
     for row in range(len(board)):
          for col in range(len(board)):
               if board[row][col] == '-':
                    board[row][col] = player
                    if player == ple:
                         score = minMaxL(board, False, 0)
                    if player == cont:
                         score = minMaxL(board, True, 0)
                    board[row][col] = '-'
                    if score > maxScore:
                         maxScore = score
                         move = (row,col)

     board[move[0]][move[1]] = player
     pprint.pprint(board)
     print("")
     return maxScore,move
     
boardL = [
     ['X','X','O','O'],
     ['-','X','-','-'],
     ['-','-','+','+'],
     ['+','+','+','+']  
]

# def play(board, player):
#      if not checkIsValid(board):
#           return False

#      flag = True
#      points = 0
#      while flag:
#           points = EvalL(board)

#           if points == 1 or points == -1:
#                flag = False
#                break
     
#           if isMovesLeft(board) == False:
#                return 0
          
#           bestMove(board, player)
#           player = 'O'
     
#      if points == 1 :
#           # pprint.pprint(board)
#           # print('GANO X')
#           # print("")
#           return points
#      if points == -1:
#           # pprint.pprint(board)
#           # print('GANO O')
#           # print("")
#           return points
     


print(bestMove(boardL, ple))