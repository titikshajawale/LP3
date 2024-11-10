class SimpleNQueens:
    def __init__(self, N, initial_row, initial_col):
        self.N = N
        self.board = [[0] * N for _ in range(N)]
        self.initial_row = initial_row
        self.initial_col = initial_col
        self.board[initial_row][initial_col] = 1  # Place the first queen

    def is_safe(self, row, col):
        # Check row on the left
        for i in range(col):
            if self.board[row][i] == 1:
                return False

        # Check upper diagonal on left
        for i, j in zip(range(row, -1, -1), range(col, -1, -1)): # decreasing by -1 and not include -1 and zip function create co-ordinate pairs of i and j 
            if self.board[i][j] == 1:
                return False

        # Check lower diagonal on left
        for i, j in zip(range(row, self.N), range(col, -1, -1)): # starts from row and goes up to self.N-1
            if self.board[i][j] == 1:
                return False
            return True

    def solve_from_column(self, col):
        # Skip the initial column of the fixed queen
        if col == self.initial_col:
            return self.solve_from_column(col + 1)

        # Base case: if all columns are filled
        if col >= self.N:
            return True

        # Try placing a queen in each row of this column
        for row in range(self.N):
            # Skip the initial row of the fixed queen
            if col == self.initial_col or row == self.initial_row:
                continue
            if self.is_safe(row, col):
                self.board[row][col] = 1

                if self.solve_from_column(col + 1):
                    return True

                # Backtrack
                self.board[row][col] = 0

        return False

    def solve(self):
        if self.solve_from_column(0):
            self.print_board()
        else:
            print("No solution exists.")

    def print_board(self):
        print("Solution:")
        for row in self.board:
            print(" ".join(str(cell) for cell in row))

# Usage example
N = 8
initial_row, initial_col = 3, 2
nq = SimpleNQueens(N, initial_row, initial_col)
nq.solve()



#tc :- O(N!)

