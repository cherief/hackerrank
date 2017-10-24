#!/bin/python3

import sys
import numpy as np
from datetime import datetime as dt

# n = int(input().strip())
# scores = [int(scores_temp) for scores_temp in input().strip().split(' ')]
# m = int(input().strip())
# alice = [int(alice_temp) for alice_temp in input().strip().split(' ')]
# your code goes here

# TEST CASE 1
n = 7
scores = [100, 100, 50, 40, 40, 20, 10]
m = 4
alice = [5, 25, 50, 100]

# TEST CASE 2
f = open('test07.dat','r+')
lines = f.readlines()
n = int(lines[0])
scores = np.array(lines[1].split(' '),dtype='int')
m = int(lines[2])
alice = np.array(lines[3].split(' '),dtype='int')

# ------------------------------
# ------------------------------
# ------------------------------ 

rank_list = [1]  # initialise rank list

for j in range(1,n):
    if scores[j-1] == scores[j]:
        rank_list.append(rank_list[j-1])
    else: 
        rank_list.append(rank_list[j-1]+1)

max_score = max(scores)

scores = list(scores)
rank_list = list(rank_list)


alice_rank = []

start = dt.now()   

j = len(scores)-1

for i,alice_score in enumerate(alice):

    if alice_score < max_score:
        while alice_score >= scores[j]:
            j = j - 1

        alice_rank.append(str(rank_list[j]+1))

    else:
        alice_rank.append('1')

save_results = '\n'.join(alice_rank)

# ------------------------------
# ------------------------------
# ------------------------------

print(dt.now() - start)

f = open('results.txt','w+')
f.write(save_results)
f.close()
