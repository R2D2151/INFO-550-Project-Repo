'''
This file will contain your the code for your problems. 
'''

import numpy as np
import cv2
import random

from algorithms import RandomAgent
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
         # code for 2 player resolution (For pacman its the Pacman vs Ghost) 
         # Pacman wins if it eats all the pellets or ends with a positive score, Ghost wins if Pacman dies with 0 score
         if wIndex == -1:
            winner = "BLINKY" # Red ghost's name
         else:
            winner = "PAC-MAN" #self.players[wIndex]   Configured just for Pac-Man
         #display final state
         score = getattr(self.problem, 'score', 0)
         print(f"The Winner is {winner} ({wIndex})!")
         print(f"Final Score: {score} (Ticks: {self.problem.ticks})")
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

   # Initialize ball catch game environment 
   # Grid dimensions, paddle width, number of balls, ball speed, maximum misses, and maximum ticks
   # ball speed: traverses multiple grid points in one tick? Need to account for distance traveled when compared to the height (speed may need to be a factor of the height)
   # max misses: not an immediate game over when missing, but maybe agent can be good enough to not miss
   def __init__(self, height=10, width=10, paddle_width=2, num_balls=1,
                 ball_speed=1, max_misses=3, max_ticks=200):
      
      self.height = height
      self.width = width
      self.paddle_width = paddle_width
      self.num_balls = num_balls
      self.ball_speed = ball_speed
      self.max_misses = max_misses
      self.max_ticks = max_ticks
      self.reset()
"""
   # Reset paddle position, score, misses, and falling balls
   def reset(self):
      self.ticks = -1
      self.score = 0
      self.misses = 0
      self.terminal = False

      # Center paddle along bottom row
      self.paddle_x = (self.width - self.paddle_width) // 2
      self.paddle_y = self.height - 1

      # Spawn initial balls (staggered initial heights if multiple balls) WIP
      self.balls = []
      for i in range(self.num_balls):
         self.balls.append(self._spawnBall())

      self._updateState()
      return self.state

   # Similar to balls spawning in snake, but remember to remove ball and spawn new one accordingly
   # Paddle doesn't grow like in snake WIP
   def _spawnBall(self):

   def _updateState(self):

   def getLegalMoves(self, state=None):
      if state is None:
         state = self.state
      moves = []
      return moves
   
   def doMove(self, move):

   def isTerminal(self, state=None):
      return self.terminal

   def getWinner(self, state=None):
"""
# New class of game: Pac-Man, for now ghost will also be random agent along with pacman
class PacMan:
   """
   Similar to snake but different encodings for the grid
   Grid:
      0: Empty corridor  
      1: Pac-Man     P
      2: Wall        #
      3: Ghost       G
     -1: Food pellet .
   
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

   def __init__(self, layout=None, ghost= None, max_ticks=300, max_idle_ticks=80):
      self.raw_layout = layout if layout is not None else self.DEFAULT_LAYOUT
      self.height = len(self.raw_layout)
      self.width = len(self.raw_layout[0])
      self.ghost = ghost if ghost is not None else RandomAgent()
      self.max_ticks = max_ticks
      self.max_idle_ticks = max_idle_ticks
      self.reset()

   def reset(self):
      self.idle_ticks = 0
      self.score = 0
      self.terminal = False
      self.ticks = -1
      self.pacman_dir = self.RIGHT # Pacman moving right by default
      self.ghost_dir = self.LEFT # Ghost moving left by default

      # Initialize walls, food pellets, Pac-Man, and ghosts based on the layout
      self.walls = set()
      self.pellets = set()
      self.ghosts = []

      pac_start = None
      # Enumerate through the layout to identify walls, pellets, Pac-Man's starting position, and ghosts
      for r, row in enumerate(self.raw_layout):
         for c, cell in enumerate(row):
            if cell == '#':
               self.walls.add((r, c))
            elif cell == '.':
               self.pellets.add((r, c))
            elif cell == 'P':
               pac_start = (r, c)
            elif cell == 'G':  # Ghost will have a random starting direction as well, but default layout shows walls on top and bottom so the ghost can only move left or right
               self.ghosts.append({ "position": (r, c), "direction": random.choice([self.LEFT, self.RIGHT]) })

      # # Where does pacman start
      # if pac_start is None:
      #       pac_start = (self.height - 2, self.width // 2)  # Corresponds with the default layout
      self.pacman = pac_start

      # # Where does ghost start in default layout
      # if not self.ghosts:
      #    self.ghosts.append({ "position": (self.height - 2, self.width // 2), "direction": random.choice([self.LEFT, self.RIGHT]) })

      # Pellets
      self.total_pellets = max(1, len(self.pellets))
      self._updateState()
      return self.state

   # _updateState needed for reset and eveything else now
   # Same way of painting grid will hopefully be used in other games
   # Using grid representations here
   def _updateState(self):
      self.state = np.zeros((self.height, self.width), dtype=int)
      for r, c in self.walls:
         self.state[r, c] = 2
      for r, c in self.pellets:
         self.state[r, c] = -1
      for ghost in self.ghosts:
         gr, gc = ghost['position']
         self.state[gr, gc] = 3
      pr, pc = self.pacman
      self.state[pr, pc] = 1

   # Pacman cannot move into walls
   def getLegalMoves(self, state=None):
      if self.terminal:
         return []
      # Position of pacman
      pr, pc = self.pacman
      legal_moves = []
      for action_idx, (dr, dc) in enumerate(self.ACTIONS):
         new_r, new_c = pr + dr, pc + dc
         # Inequality check to ensure new position is within bounds and not a wall
         if 0 <= new_r < self.height and 0 <= new_c < self.width:
            if (new_r, new_c) not in self.walls:
               legal_moves.append(action_idx)
      return legal_moves
   
   #separate legal moves for pacman and ghost, pacman cannot move into walls, ghost cannot move into walls, same logic used but does not invoke terminal state
   def getGhostLegalMoves(self):
      gr, gc = self.ghosts[0]['position']  
      legal_moves = []
      for action_idx, (dr, dc) in enumerate(self.ACTIONS):
         new_r, new_c = gr + dr, gc + dc
         if 0 <= new_r < self.height and 0 <= new_c < self.width:
            if (new_r, new_c) not in self.walls:
               legal_moves.append(action_idx)
      return legal_moves


   # Executing pacman movement, collision with ghost (wall collision does nothing), pellets eaten, ghost movement and it's collision with pacman.
   # Idle ticks and max ticks are also checked here, and the state is updated at the end of the function.
   def doMove(self, move):
      if self.terminal:
         return
      
      self.ticks += 1
      self.idle_ticks += 1

      # Same move tracking as snake, but pacman can turn 180 degrees
      # return list of move, up down, left, right
      move_idx = move if isinstance(move, int) else self.ACTIONS.index(move)
      legal_moves = self.getLegalMoves()
      if move_idx not in legal_moves:
         move_idx = self.pacman_dir  # If the move is illegal, continue in the current direction

      # Moving pacman to new position
      self.pacman_dir = move_idx
      dr, dc = self.ACTIONS[move_idx]
      new_pac = (self.pacman[0] + dr, self.pacman[1] + dc)
      if new_pac not in self.walls:   # Cannot move into wall, no position change if wall is in the way
         self.pacman = new_pac 

      # Pacman steps into ghost, score penalty for dying more than idling, game ends
      for ghost in self.ghosts:
         if self.pacman == ghost['position']:
            self.score -= 10
            self.terminal = True
            self._updateState()
            return

      # Pacman eats pellet" pacman steps into pellet, remove the pellet and update score
      if self.pacman in self.pellets:
         self.pellets.remove(self.pacman)
         self.score += 1
         # In case all pellets are eaten, the game ends successfully, extra bonus score!
         if len(self.pellets) == 0:
            self.terminal = True
            self.score += 100 
            self._updateState()
            return
      

      # Ghost step, random movement, ghost steps into pacman
      # Treating like 2 players, so ghost will also have a move, but it will be random for now, and the ghost will not eat pellets or walls, just move around
      ghost_move_idx = move if isinstance(move, int) else self.ACTIONS.index(move)
      ghost_legal_moves = self.getGhostLegalMoves()
      if ghost_move_idx not in ghost_legal_moves:
         ghost_move_idx = self.ghost_dir  # If the move is illegal, continue in the current direction

      # Moving pacman to new position
      self.ghost_dir = ghost_move_idx
      dr, dc = self.ACTIONS[ghost_move_idx]
      new_ghost = (ghost['position'][0] + dr, ghost['position'][1] + dc)
      if new_ghost not in self.walls:   # Cannot move into wall, no position change if wall is in the way
         ghost['position'] = new_ghost 
         # Same logic for ghost into pacman
         if ghost['position']  == self.pacman:
            self.score -= 50
            self.terminal = True
            self._updateState()
            return

      # Timeout check
      if self.idle_ticks >= self.max_idle_ticks:
         self.terminal = True

      self._updateState()

   def isTerminal(self, state=None):
        return self.terminal

   # Return 0 if all pellets eaten or ended with positive score (pacman dies from ghost or ticks run out), -1 otherwise.
   def getWinner(self):
      return 0 if (len(self.pellets) == 0 or self.score > 0) else -1

   def showState(self, ms=150, state=None):
      if state is None:
         state = self.state  

      cell_size = 50
      screen = np.zeros((self.height * cell_size, self.width * cell_size, 3), dtype=np.uint8)

      # Draw walls (gray)
      for r, c, in self.walls:
         cv2.rectangle(screen, (c * cell_size, r * cell_size),
                        ((c + 1) * cell_size, (r + 1) * cell_size), (128, 128, 128), -1)

      # Draw pellets (while)
      for r, c in self.pellets:
         cv2.circle(screen, (c * cell_size + cell_size // 2, r * cell_size + cell_size // 2), cell_size // 4, (255, 255, 255), -1)

      # Draw ghosts (red)
      for ghost in self.ghosts:
         gr, gc = ghost['position']
         cx = gc * cell_size + cell_size // 2
         cy = gr * cell_size + cell_size // 2
         cv2.circle(screen, (cx, cy), cell_size // 2 - 2, (0, 0, 255), -1)

      # Draw Pac-Man (yellow)
      pr, pc = self.pacman
      cx = pc * cell_size + cell_size // 2
      cy = pr * cell_size + cell_size // 2
      cv2.circle(screen, (cx, cy), cell_size // 2 - 2, (0, 255, 255), -1)

      try:
         cv2.imshow('Pac-Man', screen)
         key = cv2.waitKey(ms) & 0xFF
         if key == 27 or key == ord('q'):
               self.terminal = True
      except Exception:
         pass




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
