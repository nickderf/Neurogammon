#Main file - meant to be a 3rd party who handles interactions between the network and the game

import Game
import TDGammon
#//UNFINISHED//
#initialize the game and begin training
def initialize():
    game = Game()
    agent = TDGammon()
    train()

#//UNFINISHED//
#Set up the game loop and run until the game is over and have the agent learn
#Run 'x' amount of games to train repeatedly
#The TDGammon agent will observe a series of game states (Board positions)
#If white wins, the reward signal z = 1, if black wins z = 0
#
def train():

    #Main loop is essentially:
    #Run through the game:
    ##Moves:
    ###We need to calculate all possible moves from this state and then pick the best depending on whose turn it is
    ###TDGammon Network's output is a prediction of white's probability to win (P) from the current state (Given all possible moves)
    ###the move selected at each time step is the move that maximizes (P) when White is to play and minimizes (P) when Black is to play.
    pass
initialize()