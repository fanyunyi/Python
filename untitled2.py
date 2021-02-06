# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 22:00:43 2020

@author: 23168
"""

import csv
import pandas as pd
import matplotlib.pyplot as plt
import time
filename = 'C:/Users/23168/Desktop/20201022tensile.csv'
today = time.strftime("%y-%m-%d",time.localtime(time.time()))
with open(filename,'r') as f:
    reader = csv.reader(f)
x1 = pd.read_csv(filename, usecols=['X1'])
y1 = pd.read_csv(filename, usecols=['Y1'])
x2 = pd.read_csv(filename, usecols=['X2'])
y2 = pd.read_csv(filename, usecols=['Y2'])
x3 = pd.read_csv(filename, usecols=['X3'])
y3 = pd.read_csv(filename, usecols=['Y3'])
x4 = pd.read_csv(filename, usecols=['X4'])
y4 = pd.read_csv(filename, usecols=['Y4'])
x5 = pd.read_csv(filename, usecols=['X5'])
y5 = pd.read_csv(filename, usecols=['Y5'])
x6 = pd.read_csv(filename, usecols=['X6'])
y6 = pd.read_csv(filename, usecols=['Y6'])
plt.plot(x1, y1,'b',label='150%',linewidth = 2)
plt.plot(x3, y3,'g',label='170%',linewidth = 2)
plt.plot(x5, y5,'c',label='170%',linewidth = 2)
plt.plot(x6, y6,'m',label='170%',linewidth = 2)
plt.xlabel('Strain(%)',fontdict={'family':'Arial','size':18})
plt.ylabel('Stress(Mpa)',fontdict={'family':'Arial','size':18})
plt.legend()
plt.tick_params(direction='in')
plt.xlim(0,12)
plt.ylim(0,17.5)
plt.savefig(today+'_TensileTest_PCLPLA.png',dpi=400)
plt.show()