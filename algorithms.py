'''
This file will contain implementations of each algorithm/agent type.
'''
import random

class RandomAgent:
  def __str__(self):
    return "Random Agent"
  def getMove(self, problem):
    moves = problem.getLegalMoves()
    return moves[random.randrange(len(moves))]

class RandomAgentGhost:
  def __str__(self):
    return "Random Agent for PacMan Ghost"
  def getMove(self, problem):
    moves = problem.getGhostLegalMoves()
    return moves[random.randrange(len(moves))]
