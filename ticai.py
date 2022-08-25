from easyAI import TwoPlayerGame
from easyAI.Player import Human_Player
class TicTacToe(TwoPlayerGame):
    """the board position are numbered as follows:
    1 2 3
    4 5 6
    7 8 9
    """
    def __init__(self, players):
        self.players = players
        self.board = [0 for i in range(9)]
        self.current_player = 1
        #player 1 starts
    def possible_moves(self):
        return [i+1 for i, e in enumerate(self.board) if e==0]
    def make_move(self, move):
        self.board[int(move)-1] = self.current_player
    def unmake_move(self, move):
        #optional method (speed up the AI)
        self.board [int(move)-1] = 0
    def lose(self):
        """has the opponent three in line ?""" 
        possible_combinations = [[1,2,3], [4,5,6], [7,8,9],
         [1,4,7], [2,5,8], [3,6,9], [1,5,9], [3,5,7]]    
        return any([all([(self.board[c-1]==self.opponent_index) for c in combination])
        for combination in possible_combinations])
      
    def is_over(self):
        return (self.possible_moves()==[]) or self.lose()
    def show(self):
        print (
            "\n"
            + "\n".join(
                [
                    "".join([[".","0","x"][self.board[3*j + 1]]for i in range(3)])
                    for j in range(3)
                ]
            )
        )      
        def scoring(self):
            return -100 if self.lose() else 0
if __name__ == "__main__":
 from easyAI import AI_Player, Negamax
AI_algo = Negamax(7) 
game = TicTacToe([Human_Player(), AI_Player(AI_algo)]) 
game.play()     
            
