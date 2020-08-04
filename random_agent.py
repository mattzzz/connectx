# Selects random valid column
def agent_random(obs, config):
    import random

    valid_moves = [col for col in range(config.columns) if obs.board[col] == 0]
    return random.choice(valid_moves)
