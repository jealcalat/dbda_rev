#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 21:39:14 2019

@author: jemanj
"""

from matplotlib import pyplot as plt
import numpy as np
import matplotlib

x = np.arange(0.0, 50.0, 2.0)
y = x ** 1.3 + np.random.rand(*x.shape) * 30.0
s = np.random.rand(*x.shape) * 800 + 500

plt.plot(x, y, "go", alpha=0.5, marker=r'$\otimes$', markersize=22)
plt.xlabel("Leprechauns")
plt.ylabel("Gold")
plt.show()