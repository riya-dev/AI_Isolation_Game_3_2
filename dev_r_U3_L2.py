# Name: Riya Dev
# Date: 12/16/2020

import random

class RandomPlayer:
   def __init__(self):
      self.white = "#ffffff" #"O"
      self.black = "#000000" #"X"
      self.directions = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
      self.opposite_color = {self.black: self.white, self.white: self.black}
      self.x_max = 5
      self.y_max = 5
      self.first_turn = True
      
   def best_strategy(self, board, color):
      # returns best move 
      # (column num, row num), 0
      possible_moves = self.find_moves(board, color)
      print(possible_moves)
      x = random.choice(list(possible_moves))
      return (int(x / 5), int(x % 5)), 0
     
   def find_moves(self, board, color):
      # finds all possible moves
      # returns a set, e.g., {0, 1, 2, 3, ...., 24} 
      # 0 5 10 15 20
      # 1 6 11 16 21
      # 2 7 12 17 22
      # 3 8 13 18 23
      # 4 9 14 19 24
      
      moves_found = set()
      for i in range(len(board)):
         for j in range(len(board[i])):
            if self.first_turn == True and board[i][j] == '.': 
               moves_found.add(i * self.y_max + j)
            elif (color == self.black and board[i][j] == 'X') or (color == self.white and board[i][j] == 'O'):
               for incr in self.directions:
                  x_pos = i + incr[0]
                  y_pos = j + incr[1]
                  stop = False
                  while 0 <= x_pos < self.x_max and 0 <= y_pos < self.y_max:
                     if board[x_pos][y_pos] != '.':
                        stop = True
                     if not stop:    
                        moves_found.add(x_pos*self.y_max+y_pos)
                     x_pos += incr[0]
                     y_pos += incr[1]
      self.first_turn = False
      return moves_found
   
      """
      moves = []
      selfrow = self % 5
      selfcol = int(self / 5)
      minbound, maxbound = -1, 5
      #print(selfrow, selfcol)
      
      # | -> up down -> +/- 1
      for row in range(5):
         if row < selfrow and board[row][selfcol] != '.':
            minbound = row
         if row > selfrow and board[row][selfcol] != '.':
            maxbound = row
      for x in range(minbound + 1, maxbound):
         if selfcol * 5 + x != self:
            moves.append(selfcol*5 + x)
         
            
      # -   right left +/- 5
      for col in range(5):
         if col < selfcol and board[selfrow][col] != '.':
            minbound = col
         if col > selfcol and board[selfrow][col] != '.':
            maxbound = col
      for x in range(minbound + 1, maxbound):
         if x * 5 + selfrow != self:
            moves.append(x * 5 + selfrow)
   
      # \   diagonal   +/- 6
      leftdiag = []
      minbound = -1
      maxbound = 25
      
      x = self
      while x >= 0 + 6: x = x - 6
      min = x
      
      x = self
      while x <= 24 - 6: x = x + 6
      max = x
      
      for x in range(min, max + 1, 6):
         leftdiag.append(x)
      # print(leftdiag)
      
      for x in leftdiag:
         if x < self and board[int(x % 5)][int(x / 5)] != '.':
            minbound = x
         if x > self and board[int(x % 5)][int(x / 5)] != '.':
            maxbound = x
      # print(minbound, maxbound, leftdiag)
      
      for x in leftdiag:
         if x > minbound and x < maxbound and x != self:
            moves.append(x)
   
      # /   diagonal   +/- 4
      rightdiag = []
      minbound = -1
      maxbound = 25
      
      x = self
      while x >= 0 + 4: x = x - 4
      min = x
      
      x = self
      while x <= 24 - 4: x = x + 4
      max = x
      
      for x in range(min, max + 1, 4):
         rightdiag.append(x)
      # print(leftdiag)
      
      for x in rightdiag:
         if x < self and board[int(x % 5)][int(x / 5)] != '.':
            minbound = x
         if x > self and board[int(x % 5)][int(x / 5)] != '.':
            maxbound = x
      # print(minbound, maxbound, rightdiag)
      
      for x in rightdiag:
         if x > minbound and x < maxbound and x != self:
            moves.append(x)
      
      print(moves)         
      return set(moves)
      """

class CustomPlayer:
   def __init__(self):
      self.white = "#ffffff" #"O"
      self.black = "#000000" #"X"
      self.directions = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
      self.opposite_color = {self.black: self.white, self.white: self.black}
      self.x_max = 5
      self.y_max = 5
      self.first_turn = True

   def best_strategy(self, board, color):
      # returns best move
      # return best_move, 0
      return self.minimax(board, color, 3)

   def minimax(self, board, color, search_depth):
      # returns best "value"
      return self.max_value(board, color, search_depth)
      
   def max_value(self, board, color, search_depth):
      possible_moves = self.find_moves(board, color)
      best_move = (-1, -1)
      
      if len(possible_moves) == 0: return best_move, -999
      elif len(self.find_moves(board, self.opposite_color[color])) ==  0: return best_move, 999
      
      if search_depth == 1:
         return best_move, self.evaluate(board, color, possible_moves)
         
      val = -9999
      for m in possible_moves:
         move = (m // self.y_max, m % self.y_max)
         new_board = self.make_move(board, color, move)
         m, v = self.min_value(new_board, self.opposite_color[color], search_depth - 1)
         # min_value(state, turn, tc, search_depth):
         if v > val:
            val = v
            best_move = move
      return best_move, val
      """
      # return value and state: (val, state)
      if search_depth == 0 or self.terminal_test(board, color):
         return self.evaluate(board, color, self.find_moves(board, color))
      if terminal_test(state, tc):
         return utility(turn, tc, state), state  # from max's view
      value = -1000000000 # float('-inf') -> -1000000
      if turn == 'X':
         otherturn = 'O'
      else: otherturn = 'X'
      for a, s in successors(state, turn):
         prevval = value
         value = max(value, min_value(s, otherturn, tc, search_depth)[0])
         if (prevval != value):
            state = s 
      return value, state
      """
   
   def min_value(self, board, color, search_depth):
      possible_moves = self.find_moves(board, color)
      best_move = (-1, -1)
      
      if len(possible_moves) == 0: return best_move, 999
      elif len(self.find_moves(board, self.opposite_color[color])) == 0: return best_move, -999
      
      if search_depth == 1:
         return best_move, self.evaluate(board, color, possible_moves)
         
      val = 9999
      for m in possible_moves:  
         move = (m // self.y_max, m % self.y_max)
         new_board = self.make_move(board, color, move)         
         m, v = self.max_value(new_board, self.opposite_color[color], search_depth - 1)
         if v < val:
            val = v
            best_move = move
      return best_move, val
      """
      # return value and state: (val, state)
      if terminal_test(state, tc): # from max's view
         if utility(turn, tc, state) == 1:
            return -1, state
         elif utility(turn, tc, state) == -1:
            return 1, state
         else: return 0, state
      value = 1000000000 # float('inf') -> 1000000
      if turn == 'X':
         otherturn = 'O'
      else: otherturn = 'X'
      for a, s in successors(state, turn):
         prevval = value
         value = min(value, max_value(s, otherturn, tc, search_depth)[0])
         if (prevval != value):
            state = s
      return value, state
      """

   def negamax(self, board, color, search_depth):
      # returns best "value"
      return 1
      
   def alphabeta(self, board, color, search_depth, alpha, beta):
      # returns best "value" while also pruning
      pass

   def make_move(self, board, color, move):
      # returns board that has been updated
      
      #print(self, board, color, move)
      new_board = [x[:] for x in board] #deep copy
      new_board[move[0]][move[1]] = 'O' if color==self.white else 'X'
   
      return new_board

   def evaluate(self, board, color, possible_moves):
      # returns the utility value
      return len(possible_moves) - 2 * len(self.find_moves(board, self.opposite_color[color]))

   def find_moves(self, board, color):
      # finds all possible moves
      moves_found = set()
      for i in range(len(board)):
         for j in range(len(board[i])):
            if self.first_turn == True and board[i][j] == '.': 
               moves_found.add(i * self.y_max + j)
            elif (color == self.black and board[i][j] == 'X') or (color == self.white and board[i][j] == 'O'):
               for incr in self.directions:
                  x_pos = i + incr[0]
                  y_pos = j + incr[1]
                  stop = False
                  while 0 <= x_pos < self.x_max and 0 <= y_pos < self.y_max:
                     if board[x_pos][y_pos] != '.':
                        stop = True
                     if not stop:    
                        moves_found.add(x_pos*self.y_max+y_pos)
                     x_pos += incr[0]
                     y_pos += incr[1]
      self.first_turn = False
      return moves_found

# board: [['.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.']]