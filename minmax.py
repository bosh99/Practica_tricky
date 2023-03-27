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



#! Evaluating function
def EvalL(board):
     
    for row in range(len(board)):
          for col in range(len(board)):
               if row+1 <= 3 and col+1 <= 3:
                    if board[row][col] == board[row+1][col] and board[row+1][col] == board[row+1][col+1]:
                         if board[row][col] == 'X':
                              return 1
                         elif board[row][col] == 'O':
                              return -1
    return 0

#! max -> X(true) min -> O (false)

def minMaxL(board,player,states):
     points = EvalL(board)

     if points == 1 :
          return points
     if points == -1:
          return points
     
     if player:
          for row in range(len(board)):
               for col in range(len(board)):
                    if board[row][col] == '-':
                         board[row][col] = 'X'
                         obj = max(minMaxL(board,False,states+1))
                         board[row][col] = '-'
          return obj
     
     else:
          for row in range(len(board)):
               for col in range(len(board)):
                    if board[row][col] == '-':
                         board[row][col] = 'O'
                         obj = min(minMaxL(board,True,states+1))
                         board[row][col] = '-'
          return obj
                    

                     

    
    




boardL = [
     ['-','-','-','-'],
     ['-','-','X','O'],
     ['-','X','O','-'],
     ['-','X','-','O']  
]                        
