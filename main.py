import numpy as np
from kaggle_environments import evaluate, make, utils


def get_win_percentages(agent1, agent2, n_rounds=100):
    # Use default Connect Four setup
    config = {'rows': 6, 'columns': 7, 'inarow': 4}
    # Agent 1 goes first (roughly) half the time
    outcomes = evaluate("connectx", [agent1, agent2], config, [], n_rounds//2)
    # Agent 2 goes first (roughly) half the time
    outcomes += [[b,a] for [a,b] in evaluate("connectx", [agent2, agent1], config, [], n_rounds-n_rounds//2)]
    print("Agent 1 Win Percentage:", np.round(outcomes.count([1,-1])/len(outcomes), 2))
    print("Agent 2 Win Percentage:", np.round(outcomes.count([-1,1])/len(outcomes), 2))
    print("Number of Invalid Plays by Agent 1:", outcomes.count([None, 0]))
    print("Number of Invalid Plays by Agent 2:", outcomes.count([0, None]))


# 
# test built in agents ("random", "negamax")
#
# env = make("connectx", debug=True)
# get_win_percentages(agent1=env.agents['negamax'], agent2="random")



#
# test custom agents
#
import random_agent
import simple_agent
import one_step_heuristic
import minimax
import negamax

# env = make("connectx", debug=True)
# env.play([simple_agent.my_agent, None], width=500, height=450)

# get_win_percentages(agent1=simple_agent.my_agent, agent2=random_agent.agent_random)
# get_win_percentages(agent1=simple_agent.my_agent, agent2=one_step_heuristic.my_agent)

# get_win_percentages(agent1=minimax.my_agent, agent2=one_step_heuristic.my_agent)
# get_win_percentages(agent1=minimax.my_agent, agent2=random_agent.agent_random)

get_win_percentages(agent1=negamax.my_agent, agent2=minimax.my_agent)




#
# validate agent - uncomment below to test agent for errors
#
# env = make("connectx", debug=True)
# env.run([negamax.my_agent, random_agent.agent_random])
# print("Success!" if env.state[0].status == env.state[1].status == "DONE" else "Failed...")

