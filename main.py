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
        
    def __str__(self):
        return '{}'.format(self.board)
    
    def __repr__(self):
        return '{}'.format(self.board)
        
    def get_row(self, rn):
        return self.board[rn]
    
    def get_column(self, cn):
        return self.board[:, cn]
        
    def input_number(self, i, j, v):
        if v in range(1,10):
            self._board[i][j] = v
        else:
            print('Invalid number')
 
# check all numbers are unique and not equal to 0
    def is_board_correct(self):   
        return len(np.unique(self.board)) == 9 and 0 not in np.unique(self.board)
        
        
class WholeBoard(object):
    def __init__(self, board=[[SmallBoard(), SmallBoard(), SmallBoard()] for _ in range(3)]):
        self.board = board
        
    def get_smallboard(self, i, j):
        return self.board[i][j]

    # rn: row_number 0-8    
    def is_row_correct(self, rn):
        row = np.array([], dtype=int)
        for col in range(3):
            row = np.append(row, self.get_smallboard(rn // 3 , col).get_row(rn % 3))
        return len(np.unique(row)) == 9 and 0 not in np.unique(row)        
        
    def is_column_correct(self, cn):
        col = np.array([], dtype=int)
        for row in range(3):
            col = np.append(col, self.get_smallboard(row, cn // 3).get_column(cn % 3))
        return len(np.unique(col)) == 9 and 0 not in np.unique(col)          
        
    def is_wholeboard_correct(self):
        for a in range(9):
            if not self.is_row_correct(a) or not self.is_column_correct(a):
                return False
        for i in range(3):
            for j in range(3):
                if not self.get_smallboard(i,j).is_board_correct():
                    return False
        return True
            
        
    

if __name__ == "__main__":
    sb = SmallBoard(np.array([[1,2,3], [4,5,6],[7,8,9]], dtype=int))
    b = WholeBoard([[sb, sb, sb] for _ in range(3)])
    print(b.is_wholeboard_correct())
    
    