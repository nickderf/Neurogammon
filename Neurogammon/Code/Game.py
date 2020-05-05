
import Player
import Checker
#//UNFINISHED//
class Game:

    def __init__():

        #backgammon board has a total of 24 spaces, each being represented by a list
        self.board = [[] for i in range(24)]
        #the current turn will be represented by the players ID
        self.turn = -1
        self.players = [Player(1), Player(2)]

        initialize_board()

    #initialize the board for play, all 30 checkers for both players must be set up
    #RETRURN: None or TBD
    def initialize_board():

        start()
    
    #start the game
    #RETRURN: None or TBD
    def start():
        #roll dice to determine who goes first
        pass

    #Roll a 6 sided die or dice
    #PARAMETERS: n - number of dice being rolled
    #RETURN: list size of n with the results results
    def roll_dice(n):
        pass

    #Make a move for a player based on the results of the dice
    #RETRURN: None or TBD
    def make_move(player,dice_results):
        pass

    #for each player, check to see if they have won
    #RETURN: Player that has won
    def check_win_condition():
        pass



