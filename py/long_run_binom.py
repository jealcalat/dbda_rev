
"""
Example of binomial rv: flipping a coin. We will simulate the long-run relative
frequency as the sum of #heads/trials from 0 to N trials
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

plt.rcParams["font.family"] = "serif"
plt.rcParams["mathtext.fontset"] = "cm"

N = 500
p_theta=np.zeros(N)

for i in range(N):
    ki = np.random.binomial(1,0.5,i+1)
    p_theta[i] = np.sum(ki)/(i+1)

fig, ax = plt.subplots(1, 1)
ax.plot(np.arange(1,N+1,1),p_theta,lw=0.5)
ax.scatter(500,p_theta[-1],c='red',s=10)
ax.set_xscale('log')
ax.tick_params(direction='in',which='both')
ax.get_xaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())
ax.get_xaxis().set_minor_formatter(matplotlib.ticker.NullFormatter())
ax.set_xticks([1,10,100,500])
ax.annotate('End prop = {}'.format(p_theta[-1]),
           xy=(500,p_theta[-1]),xytext=(-90, 40), textcoords='offset points',
           arrowprops=dict(arrowstyle="->"))
plt.xlabel('$\log N$')
plt.ylabel('Proportion of Heads')
plt.axhline(y=0.5,ls=':',c='red')
fig.savefig('long_run_coin.pdf',dpi=120)