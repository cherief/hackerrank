#!/bin/python3

import sys
from datetime import datetime as dt



# n = int(input().strip())
# scores = [int(scores_temp) for scores_temp in input().strip().split(' ')]
# m = int(input().strip())
# alice = [int(alice_temp) for alice_temp in input().strip().split(' ')]
# your code goes here

n = 7
scores = [100, 100, 50, 40, 40, 20, 10]
m = 4
alice = [5, 25, 50, 100]

import numpy as np

f = open('test07.dat','r+')
lines = f.readlines()
n = int(lines[0])
scores = np.array(lines[1].split(' '),dtype='int')
m = int(lines[2])
alice = np.array(lines[3].split(' '),dtype='int')



# ------------------------------
# ------------------------------
# ------------------------------ 


# initialise rank list
rank_list = [1]

for j in range(1,n):
    if scores[j-1] == scores[j]:
        rank_list.append(rank_list[j-1])
    else: 
        rank_list.append(rank_list[j-1]+1)

# min_score = min(scores)
max_score = max(scores)


#scores_reverse = sorted(scores,key=int,reverse=True)
#rank_list_reverse = sorted(rank_list,key=int,reverse=True)
#alice_reverse = sorted(alice,reverse=True)



scores_reverse = list(scores)
scores_reverse.reverse()

rank_list_reverse = list(rank_list)
rank_list_reverse.reverse()



min_rank_list_reverse = rank_list_reverse[0]

alice_rank = []

start = dt.now()   

for i,alice_score in enumerate(alice):

    if alice_score >= max_score:
        #alice_rank.append('1')
        pass
        #print(1)

    else:
        j = 0

        while alice_score >= scores_reverse[j]:

            j = j + 1

        #alice_rank.append(str(rank_list_reverse[j]+1))
        #print(rank_list_reverse[j] + 1)


        scores_reverse = scores_reverse[j:]
        rank_list_reverse = rank_list_reverse[j:]

#save_results = '\n'.join(alice_rank)
#print
# ------------------------------
# ------------------------------
# ------------------------------

print(dt.now() - start)



# f = open('results.txt','w+')
# f.write(save_results)
# f.close()
