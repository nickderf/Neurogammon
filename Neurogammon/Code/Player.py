#//UNFINISHED//
class Player:
    def __init__(id):
        #id to differentiate between players
        self.id = id

        #a player starts with 15 checkers on the board
        self.checkers_on_board = [Checker() for i in range(15)]
        self.checkers_off_board = []

    #if a player has a checker on the middle bar, then they must prioritize moving that checker
    #RETURN: boolean if player has a checker on middle bar
    def check_middle_bar():
        pass