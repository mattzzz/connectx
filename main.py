import numpy as np
from kaggle_environments import evaluate, make, utils

import helpers



# 
# test built in agents ("random", "negamax")
#
# env = make("connectx", debug=True)
# helpers.get_win_percentages(agent1=env.agents['negamax'], agent2="random")



#
# test custom agents
#
import random_agent
import simple_agent
import one_step_heuristic
import minimax
import negamax

# env = make("connectx", debug=True)
# env.play([simple_agent.agent, None], width=500, height=450)

# helpers.get_win_percentages(agent1=simple_agent.agent, agent2=random_agent.agent_random)
# helpers.get_win_percentages(agent1=simple_agent.agent, agent2=one_step_heuristic.agent)

# helpers.get_win_percentages(agent1=minimax.agent, agent2=one_step_heuristic.agent)
# helpers.get_win_percentages(agent1=minimax.agent, agent2=random_agent.agent_random)

helpers.get_win_percentages(agent1=negamax.agent, agent2=minimax.agent)




#
# validate agent - uncomment below to test agent for errors
#
# env = make("connectx", debug=True)
# env.run([negamax.agent, random_agent.agent_random])
# print("Success!" if env.state[0].status == env.state[1].status == "DONE" else "Failed...")

