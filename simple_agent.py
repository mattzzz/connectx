def my_agent(obs, config):
    import numpy as np

    # Gets board at next step if agent drops piece in selected column
    def drop_piece(grid, col, piece, config):
        next_grid = grid.copy()
        for row in range(config.rows-1, -1, -1):
            if next_grid[row][col] == 0:
                break
        next_grid[row][col] = piece
        return next_grid

    # Returns True if dropping piece in column results in game win
    def check_move(obs, config, col, piece, inrow):
        # Convert the board to a 2D grid
        grid = np.asarray(obs.board).reshape(config.rows, config.columns)
        next_grid = drop_piece(grid, col, piece, config)
        # horizontal
        for row in range(config.rows):
            for col in range(config.columns-(inrow-1)):
                window = list(next_grid[row,col:col+inrow])
                if window.count(piece) == inrow:
                    return True
        # vertical
        for row in range(config.rows-(inrow-1)):
            for col in range(config.columns):
                window = list(next_grid[row:row+inrow,col])
                if window.count(piece) == inrow:
                    return True
        # positive diagonal
        for row in range(config.rows-(inrow-1)):
            for col in range(config.columns-(inrow-1)):
                window = list(next_grid[range(row, row+inrow), range(col, col+inrow)])
                if window.count(piece) == inrow:
                    return True
        # negative diagonal
        for row in range(inrow-1, config.rows):
            for col in range(config.columns-(inrow-1)):
                window = list(next_grid[range(row, row-inrow, -1), range(col, col+inrow)])
                if window.count(piece) == inrow:
                    return True
        return False    
    
    # Your code here: Amend the agent!
    import random
    # Your code here: Amend the agent!
    valid_moves = [col for col in range(config.columns) if obs.board[col] == 0]
    for col in valid_moves:
        if check_move(obs, config, col, obs.mark, config.inarow):
            return col
    for col in valid_moves:
        if check_move(obs, config, col, 1 if obs.mark==2 else 2, config.inarow):
            return col        
    for col in valid_moves:
        if check_move(obs, config, col, obs.mark, config.inarow-1):
            return col        
    for col in valid_moves:
        if check_move(obs, config, col, obs.mark, config.inarow-2):
            return col         
    return random.choice(valid_moves)
