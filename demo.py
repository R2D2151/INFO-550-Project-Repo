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
# layout=DEBUG_LAYOUT, 
pacman_env = prb.PacMan(max_idle_ticks=30, max_ticks=50)
game = prb.Game(pacman_env, pZero=alg.RandomAgent(), verbose=True)
game.playGame()

# catch_env = prb.BallCatch(height=10, width=10, paddle_width=5, num_balls=5,ball_speed=1, max_misses=3, max_ticks=100)
# game = prb.Game(catch_env, pZero=alg.RandomAgent(), verbose=True)
# game.playGame()