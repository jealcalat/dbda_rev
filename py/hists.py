#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 09:57:37 2019

@author: mrrobot
"""

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib import rc
#rc('font',**{'family':'sans-serif','sans-serif':['Helvetica']})
## for Palatino and other serif fonts use:
rc('font',**{'family':'serif','serif':['Palatino']})
rc('text', usetex=True)

plt.style.use('seaborn-ticks')

sds = [2,10,200,1000]
mu = 0

fig = plt.figure()
fig.subplots_adjust(hspace=0.45, wspace=0.2)
fig.suptitle(r'$x \sim \mathcal{N}(\mu,\sigma)$', fontsize=14)
for i in range(0, 4):
    if i == 0:
        xmin = -20
        xmax = 20
    elif i == 1:
        xmin = -200
        xmax = 200
    else:
        xmin = -2500
        xmax = 2500
            
    rv = np.random.normal(mu, sds[i], 1000)
    ax = fig.add_subplot(2, 2, i+1)
    ax.hist(rv, alpha = 0.9, color = 'magenta', edgecolor='none')
    ax.set_xlim(xmin,xmax)
    ax.set_title(r'$\sigma = $ %0.0f' % sds[i])
    ax.set_xlabel(r'$x$')
    ax.axvline(x = 0,color = 'black',ls = '--')
    
fig.savefig('Figure_1.pdf')