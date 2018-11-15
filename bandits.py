### Simply bandit
print('Simply bandit started.')
print('-'*30)
from time import clock
def rand():
    """
    Generate sample from uniform distribution in range [0, 10)
    """
    a = 546546456567
    b = 546546456
    m = 9499249595
    seed = clock()
    X = round(((seed * a + b) % m / m)*10,3)
    return X

def simply_bandit(r1,r2,r3,capital,stavka):
    remainder = capital - stavka
    if remainder <= 0:
        return None
    else:
        if r1 == r2 == r3:
            win = 3
        elif r1 == r2 or r1 == r3 or r2 == r3:
            win = 2
        else:
            win = 0  
    return win
capital = 10
stavka = 1
print('Your start capital is:', capital)
while capital > 0:
    r1 = rand()
    r2 = rand()
    r3 = rand()
    win = simply_bandit(r1,r2,r3,capital,stavka)
    if win == 3:
        capital = capital - stavka + 3
        print('You are win 3!')       
    elif win == 2:
        capital = capital - stavka + 2
        print('You are win 2!')
    elif win == 0:
        capital = capital - stavka + 0
        print('You are lose!')
    else: 
        capital = 0
        print('Game over!')
    print ('Rate 10','Your capital is:', capital)
print('-'*30)
print('Simply bandit finished.')
print('-'*30)
### Multi-armed bandit 
print('Multi-armed bandit started.')
print('-'*30)
from time import clock
class BernoulliArm():
    def __init__(self, p):
        self.p = p

    def draw(self):
        if random.random() > self.p:
            return 0.0
        else:
            return 1.0

def rand_mlt():
    """
    Generate sample from uniform distribution in range [0, 1)
    """
    a = 546546456567
    b = 546546456
    m = 9499249595
    seed = clock()
    X = round(((seed * a + b) % m / m),2)
    return X

def Random(bandits,iters):
    arm = np.zeros(len(bandits))
    arm_rewards = np.zeros(len(bandits))
    total_reward = 0
    for i in range(iters):
        arms_means = np.zeros(len(arm))
        idx_max = 0
        avg_max = 0
        for j in range(len(bandits)):
            mean = arm_rewards[j] / (arm[j] + .001)
            if mean > avg_max:
                avg_max, idx_max = mean, j
            
        arm_index = idx_max
        choice = bandits[arm_index]
        reward = choice.draw()
        arm[arm_index] += 1
        arm_rewards[arm_index] += reward
        arm_mean = arm_rewards[arm_index] / arm[arm_index]
        total_reward += reward
    return total_reward

def EGreedy(bandits,eps,iters):
    arm = np.zeros(len(bandits))
    arm_rewards = np.zeros(len(bandits))
    total_reward = 0
    for i in range(iters):
        arms_means = np.zeros(len(arm))
        idx_max = 0
        avg_max = 0
        for j in range(len(bandits)):
            mean = arm_rewards[j] / (arm[j] + .001)
            if mean > avg_max:
                avg_max, idx_max = mean, j   
        arm_index = idx_max
        choice = rand_mlt()
        if choice < eps:
            arm_index = random.randint(0, len(bandits) - 1)
        choice = bandits[arm_index]
        reward = choice.draw()
        arm[arm_index] += 1
        arm_rewards[arm_index] += reward
        arm_mean = arm_rewards[arm_index] / arm[arm_index]
        total_reward += reward
    return total_reward

def UCB(bandits,iters):
    arm = np.zeros(len(bandits))
    arm_rewards = np.zeros(len(bandits))
    total_reward = 0  
    for n in range(iters):
        idx_max = 0 
        max_ub = 0
        for i in range(len(bandits)):
            if (arm[i] > 0):
                mean = arm_rewards[i] / (arm[i] + .001)
                delta_i = math.sqrt(2 * math.log(n+1) /arm[i])
                upper_bound = mean + delta_i
            else:
                upper_bound = 1e400
            if upper_bound > max_ub:
                max_ub, idx_max  = upper_bound, i
        arm_index = idx_max
        choice = bandits[arm_index]
        reward = choice.draw()
        arm[arm_index] += 1
        arm_rewards[arm_index] += reward
        arm_mean = arm_rewards[arm_index] / arm[arm_index]
        total_reward += reward
    return total_reward


import numpy as np
import random
import math

iters = 1000
band1 = BernoulliArm(p = rand_mlt())
band2 = BernoulliArm(p = rand_mlt())
band3 = BernoulliArm(p = rand_mlt())
band4 = BernoulliArm(p = rand_mlt())
band5 = BernoulliArm(p = rand_mlt())

mult_band = [band1, band2, band3, band4, band5]
eps = 0.01

print('Random rewards:', Random(mult_band,iters))
print('EGreedy rewards:', EGreedy(mult_band,eps,iters))
print('UCB rewards:', UCB(mult_band,iters))
print('-'*30)
print('Multi-armed bandit finished.')
