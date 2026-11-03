'''
This file will contain your the code for your problems. 
'''

import numpy as np
import cv2
import random
# Originally for two player adversial games,  need to adapt to or support single agent/player
class Game:
    def __init__(self, problem, pZero, pOne,verbose=True):
      self.problem = problem      
      #self.players = [pZero,pOne] defaulted to two players 
      if isinstance(pOne, bool):
         verbose = pOne
         pOne = None

      if pOne is None:
         self.players = [pZero]          # Single-player environment
      else:
         self.players = [pZero, pOne]    # Two-player adversarial environment  
      self.verbose = verbose   
      if self.verbose:
         self.problem.showState()               
    def playGame(self):
      pCur=0
      while self.problem.isTerminal()==False:           
         move = self.players[pCur].getMove(self.problem)           
         self.problem.doMove(move)
         if self.verbose:
            self.problem.showState()
            print(f"Move {self.problem.ticks}:")
            print(self.problem.state)
         if len(self.players) > 1: # Now need condition for more than 1 player
            pCur = np.abs(pCur-1)  # Switch between the two players
        
      wIndex = self.problem.getWinner()
      if len(self.players) > 1:
         # code for 2 player resolution
         if wIndex == -1:
            winner = "DRAW"
         else:
            winner = self.players[wIndex]
         #display final state
         print(f"The Winner is {winner} ({wIndex})!")
      else:
         # code for single player resolution, no winner, score needed
         score = getattr(self.problem, 'score', 0)
         status = "SUCCESS" if wIndex == 0 else "TERMINATED"
         print(f"{status}! Final Score: {score} (Ticks: {self.problem.ticks})")

      if self.verbose:
         self.problem.showState(4000)
      return wIndex
# New class of game: snake
class Snake:
   """
   Grid:
      0:  Empty cell
      1:  Snake head
      2:  Snake body
      -1: Apple

   Actions:
      0:  Up    (-1,  0)
      1:  Down  ( 1,  0)
      2:  Left  ( 0, -1)
      3:  Right ( 0,  1)
   """
   UP = 0
   DOWN = 1
   LEFT = 2
   RIGHT = 3

   ACTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]
   ACTION_NAMES = {0: "UP", 1: "DOWN", 2: "LEFT", 3: "RIGHT"}
   OPPOSITES = {0: 1, 1: 0, 2: 3, 3: 2}
   def __init__(self):
      self.state = np.zeros((20,20)) # 20 by 20 grid
      self.ticks = -1

   def getLegalMoves(self, state=None):
      if state is None:
         state = self.state
      moves = []
      return moves
# New class of game: ball catch
class BallCatch:
   """
    Actions:
      0: Move LEFT   (dx = -1)
      1: STAY        (dx =  0)
      2: Move RIGHT  (dx = +1)
    """
   LEFT = 0
   STAY = 1
   RIGHT = 2

   ACTIONS = [-1, 0, 1]
   ACTION_NAMES = {0: "LEFT", 1: "STAY", 2: "RIGHT"}
   def __init__(self):
      self.state = np.zeros((20,20)) # 20 by 20 grid
      self.ticks = -1

   def getLegalMoves(self, state=None):
      if state is None:
         state = self.state
      moves = []
      return moves

# New class of game: Pac-Man
class PacMan:
   """
   Similar to snake but different encodings for the grid
   Grid:
      0: Empty corridor
      1: Pac-Man
      2: Wall
      3: Ghost
   -1: Food pellet
   
   Actions:
   0: UP    (-1,  0)
   1: DOWN  ( 1,  0)
   2: LEFT  ( 0, -1)
   3: RIGHT ( 0,  1)
   """
   UP = 0
   DOWN = 1
   LEFT = 2
   RIGHT = 3

   ACTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]
   ACTION_NAMES = {0: "UP", 1: "DOWN", 2: "LEFT", 3: "RIGHT"}
   OPPOSITES = {0: 1, 1: 0, 2: 3, 3: 2}

   # 11x11 grid with # as walls, G as ghosts, P as Pac-Man, . as food pellets
   DEFAULT_LAYOUT = [
      "###########",
      "#....#....#",
      "#.##.#.##.#",
      "#.........#",
      "#.##.#.##.#",
      "#....G....#",
      "#.##.#.##.#",
      "#....#....#",
      "#.##...##.#",
      "#....P....#",
      "###########",
   ]
   def __init__(self, layout=None, max_ticks=300, max_idle_ticks=80):
      self.raw_layout = layout if layout is not None else self.DEFAULT_LAYOUT
      self.height = len(self.raw_layout)
      self.width = len(self.raw_layout[0])
      self.max_ticks = max_ticks
      self.max_idle_ticks = max_idle_ticks
      self.reset()

   def reset(self):
      self.idle_ticks = 0
      self.score = 0
      self.terminal = False
      self.ticks = -1

   def getLegalMoves(self, state=None):
      if state is None:
         state = self.state
      moves = []
      return moves
"""
   def _updateState(self):

   def getLegalMoves(self, state=None):

   def doMove(self, move):

   def isTerminal(self, state=None):
        return self.terminal
   
   def getWinner(self):

   def showState(self, ms=150, state=None):
"""

class TicTacToe:
   def __init__(self):
      self.state = np.zeros((3,3))      
      self.ticks=-1      
   def getLegalMoves(self, state=None):
      if state is None:
         state = self.state
      moves = []
      mark = 1
      if np.sum(np.abs(state))%2!=0:
         mark = -1       
      for i in range(state.shape[0]):
         for j in range(state.shape[1]):
            if state[i,j]==0:
               moves.append((mark,(i,j)))
      return moves             
   def getSuccessor(self, move, state):
      mark = move[0]
      loc = move[1]
      state[loc] = mark
      return state
   def doMove(self,move):
      self.state = self.getSuccessor(move,self.state)
      self.ticks+=1
   def isTerminal(self, state=None):
      if state is None:
         state = self.state         
      terminal = False
      val = self.evalTerminal(state)      
      if val ==0 and np.sum(np.abs(state))==9:
         terminal = True
      if val!=0:
         terminal = True
      return terminal
   def evalTerminal(self, state=None):
      if state is None:
         state = self.state
      val = 0      
      
      pZeroWins = [np.max(np.sum(state,0))==3,np.max(np.sum(state,1))==3,np.trace(state)==3,np.trace(state[:,::-1])==3]
      pOneWins = [np.min(np.sum(state,0))==-3,np.min(np.sum(state,1))==-3,np.trace(state)==-3,np.trace(state[:,::-1])==-3]

      if np.any(pZeroWins):
         val = 1
      if np.any(pOneWins):
         val = -1
      return val
   def getWinner(self, state=None):
      if state is None:
         state = self.state
      val = self.evalTerminal(state)
      if val==1:
         return 0 
      elif val==-1:
         return 1
      else:
         return -1
   def showState(self, ms = 1000,state=None):
      if state is None:
         state = self.state  

      screen = np.zeros((150,150)).astype(np.uint8)         
      screen = cv2.line(screen,(0,49),(149,49),255) 
      screen = cv2.line(screen,(0,99),(149,99),255)
      screen = cv2.line(screen,(49,0),(49,149),255) 
      screen = cv2.line(screen,(99,0),(99,149),255)

      for i in range(state.shape[0]):
         for j in range(state.shape[1]):
            if state[i,j]==1:
               screen = cv2.line(screen,(5 +j*50,5+i*50),(44+j*50,44+i*50),255,2,cv2.LINE_AA) 
               screen = cv2.line(screen,(44+j*50,5+i*50),(5 +j*50,44+i*50),255,2,cv2.LINE_AA) 
            if state[i,j]==-1:
               screen = cv2.circle(screen, (25 +j*50,25+i*50), 20, 255, 2,cv2.LINE_AA) 
               
      cv2.imshow('TicTacToe',screen)
      cv2.waitKey(ms)
