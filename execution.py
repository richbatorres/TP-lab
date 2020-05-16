import matplotlib
import matplotlib.pyplot as plt
import scipy.stats as st
import numpy as np
import discreteMarkovChain
import random
import math
import csv
from statsmodels.distributions.empirical_distribution import ECDF
import time



def generate_traffic(state, time):
    if state==0:
        #generiraj promet po prvom modelu (forum)
        pass
    elif state==1:
        #generiraj promet po drugom modelu (editing)
        pass
    elif state==2:
        #generiraj promet po trećem modelu (video)
        pass

def sample_from_rate(rate):
    if rate == 0:
        return math.inf
    return random.expovariate(rate)

def simulate_cmc(Q, time):
    Q = list(Q)  # In case a matrix is input
    state_space = range(len(Q))  # Index the state space
    time_spent = {s:0 for s in state_space}  # Set up a dictionary to keep track of time
    clock = 0  # Keep track of the clock
    current_state = random.choice([0, 1, 2])  # First state
    times0=[]
    times1=[]
    times2=[]
    while clock < time:
        # Sample the transitions
        sojourn_times = [sample_from_rate(rate) for rate in Q[current_state][:current_state]]
        sojourn_times += [math.inf]  # An infinite sojourn to the same state
        sojourn_times += [sample_from_rate(rate) for rate in Q[current_state][current_state + 1:]]

        # Identify the next state
        next_state = min(state_space, key=lambda x: sojourn_times[x])
        sojourn = sojourn_times[next_state]
        clock += 1
        # generate_traffic(current_state, sojurn)
        time_spent[current_state] += sojourn
        if current_state==0:
            times0.append(sojourn)
        elif current_state==1:
            times1.append(sojourn)
        else:
            times2.append(sojourn)
        current_state = next_state  # Transition

    pi = [time_spent[state] / sum(time_spent.values()) for state in state_space]  # Calculate probabilities
    return pi, time_spent, times0, times1, times2


#lambda1=117
#labda2=37
#lambda3=29
Q=np.array([[-0.2, 0.2, 0], [0.45, -0.9, 0.45], [0.96, 0.24, -1.2]])
p, time_spent, times0, times1, times2=simulate_cmc(Q, 200)
print("stacionarne vjerojatnosti:\n s1:", p[0], " s2:", p[1], " s3:", p[2])
print("ukupna vremena:\n s1:", time_spent[0], " s2:", time_spent[1], " s3:", time_spent[2])

print("empirijska prosječna trajanja:\n s1:", time_spent[0]/len(times0), " s2:", time_spent[1]/len(times1), " s3:", time_spent[2]/len(times2))


# with open('trajanja.csv', 'w', newline='') as file:
#     writer = csv.writer(file)
#     writer.writerow([time_spent[0], time_spent[1], time_spent[2]])