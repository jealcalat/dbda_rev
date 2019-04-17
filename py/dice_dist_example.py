#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 19:47:22 2019

@author: jemanj
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

dice1 = np.arange(1,7,1)
dice2 = np.arange(1,7,1)

N = 1000
frq = np.zeros(N)

for i in range(N):
    v1 = np.random.choice(dice1)
    v2 = np.random.choice(dice2)
    frq[i] = np.sum([v1,v2])
    
b, counts = np.unique(frq, return_counts=True)

prop_sum = counts/np.sum(counts)

# np.asarray((b, counts)).T


fig, ax = plt.subplots(1, 1)
plt.stem(b,prop_sum)
plt.ylim(0, np.max(prop_sum)*1.1)
ax.set_xticks(np.arange(2,13,1))
ax.tick_params(direction='in',which='both')
ax.annotate('$p(s = 7) =$ {}'.format(np.max(prop_sum)),
           xy=(7,np.max(prop_sum)),xytext=(-90, 10), textcoords='offset points',
           arrowprops=dict(arrowstyle="->"))