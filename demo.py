import problems as prb
import algorithms as alg

'''
This file will contain the code needed to run a demonstration of your project. 

For the progress report, it should contain code that shows a brief demonstration of random agents attempting to solve each problem. 

For the final report, it should contain code that shows a brief demonstration of each algorithm attempting to solve each problem. 

In both cases, to make sure we can grade these all in time, please ensure that each demonstration is just long enough to show some
meaningful behavior. If your problem is chess playing, for example, you might show 5 moves from each player, where one player uses one 
algorithm and one player uses another. If your problem is snake, you might show game long enough for the player to eat two apples or die
(whichever comes first).
'''

#demoGame = prb.Game(prb.TicTacToe(),alg.RandomAgent(),alg.RandomAgent())
#demoGame.playGame()

# snake_env = prb.Snake(height=8, width=8, num_apples=30, max_idle_ticks=30, max_ticks=40)
# game = prb.Game(snake_env, alg.RandomAgent(), verbose=True)
# game.playGame()

# Smaller than default and trying to force collision
DEBUG_LAYOUT = [
        "#####",
        "#...#",
        "#.#.#",
        "#.G.#",
        "#.#.#",
        "#...#",
        "#.#.#",
        "#.P.#",
        "#####"
    ]

pacman_env = prb.PacMan(layout=DEBUG_LAYOUT, ghost=alg.RandomAgentGhost(), max_idle_ticks=30, max_ticks=50)
game = prb.Game(pacman_env, pZero=alg.RandomAgent(), pOne=alg.RandomAgentGhost(), verbose=True)
game.playGame()