import numpy as np

class SmallBoard(object):
    def __init__(self, board=np.zeros((3,3), dtype=int)):
        self.board = board
    
    @property
    def board(self):
        return self._board
    
    @board.setter
    def board(self, matrix):
        self._board = matrix
        
    def input_number(self, i, j, v):
        if v in range(1,10):
            self._board[i][j] = v
        else:
            print('Invalid number')
 
# check all numbers are unique and not equal to 0
    def is_board_correct(self):   
        return len(np.unique(self.board)) == 9 and 0 not in np.unique(self.board)
        
        
class WholeBoard(object):
    def __init__(self, board=np.zeros((3,3), dtype=SmallBoard)):
        self.board = board

# rn: row_number 0-8    
    def is_row_valid(self, rn):
        pass
        
    def is_column_valid(self, cn):
        pass
            
        
    

if __name__ == "__main__":
    b = WholeBoard()