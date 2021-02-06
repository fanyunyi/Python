# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 22:00:43 2020

@author: 23168
"""

import csv
import pandas as pd
import matplotlib.pyplot as plt
import time
#此处输入原始数据路径
filename = 'C:/Users/23168/Desktop/Book1.csv'
filename2 = 'C:/Users/23168/Desktop/tensile1.csv'
today = time.strftime("%y-%m-%d",time.localtime(time.time()))
with open(filename,'r') as f:
    reader = csv.reader(f)
with open(filename2,'r') as f2:
    reader2 = csv.reader(f2)
#读取特定列
x100 = pd.read_csv(filename2,usecols=['x_100'])
y100 = pd.read_csv(filename2,usecols=['y_100'])
x120 = pd.read_csv(filename2,usecols=['x_120'])
y120 = pd.read_csv(filename2,usecols=['y_120'])
x150 = pd.read_csv(filename2,usecols=['x_150'])
y150 = pd.read_csv(filename2,usecols=['y_150'])
x120_2 = pd.read_csv(filename2,usecols=['x_120_2'])
y120_2 = pd.read_csv(filename2,usecols=['y_120_2'])
x1 = pd.read_csv(filename, usecols=['x1'])
y1 = pd.read_csv(filename, usecols=['y1'])
x2 = pd.read_csv(filename, usecols=['x2'])
y2 = pd.read_csv(filename, usecols=['y2'])
x4 = pd.read_csv(filename, usecols=['x4'])
y4 = pd.read_csv(filename, usecols=['y4'])
x3 = pd.read_csv(filename, usecols=['x3'])
y3 = pd.read_csv(filename, usecols=['y3'])
plt.plot(x1, y1,'k',label='100%',linewidth = 3)
plt.plot(x2, y2,'y',label='120%',linewidth = 3)
plt.plot(x3, y3,'b',label='150%',linewidth = 3)
plt.plot(x4, y4,'g',label='170%',linewidth = 3)
plt.xlabel('Strain(%)',fontdict={'family':'Arial','size':18})
plt.ylabel('Stress(Mpa)',fontdict={'family':'Arial','size':18})
plt.legend()
plt.tick_params(direction='in')
plt.xlim(0,14)
plt.ylim(0,17.5)
plt.savefig(today+'_TensileTest2_PCLPLA.png',dpi=400)
plt.show()
