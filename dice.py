# -*- coding: utf-8 -*-

import numpy as np
import re

dice = np.random.randint(low=1, high=7, size=(12, 5))

filelista = r'..\..\Security\diceware_list_pl.txt'
with open(filelista,'r') as file:
    dobre = [line for line in file if re.match('^[1-6]{5}',line[0:5])]



#%%
d = dict()
for i in range(len(dobre)):
    k,v = dobre[i].split()
    d[k] = v

#%%
print(dice.shape)
y = [''.join([str(x) for x in dice[i]]) for i in range(12)]
#s = ''.join(y)
#print(s,d[s])
print(y)
for k in y:
    print(k,d[k])
