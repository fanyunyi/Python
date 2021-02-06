# -*- coding: utf-8 -*-
"""
Created on Fri Oct 30 23:02:26 2020

@author: 23168
"""

import csv
import pandas as pd
import matplotlib.pyplot as plt
import time
from matplotlib.ticker import MultipleLocator,FormatStrFormatter #副刻度
#此处输入原始数据路径
filename = 'C:/Users/23168/Desktop/tensiledata/YoungModuls.csv'
today = time.strftime("%y-%m-%d",time.localtime(time.time()))
with open(filename,'r') as f:
    reader = csv.reader(f)
#读取特定
x1 = pd.read_csv(filename, usecols=['Sample'])
y1 = pd.read_csv(filename, usecols=['YoungModuls'])
x1['Sample'] = x1['Sample'].str.strip('%').astype(float)
plt.plot(x1, y1,'b',marker ='^',label='100%',linewidth = 1)
#标题栏设置
plt.xlabel('Sample(%)',fontdict={'family':'Arial','size':18,'style':'oblique'})
plt.ylabel('Young\'s Modulus(Mpa)',fontdict={'family':'Arial','size':15,'style':'oblique'})
ax =plt.subplot(111) #仅可在子图中进行刻度设置
xmajorLocator = MultipleLocator(25) #设置单位主刻度
ax.xaxis.set_major_locator(xmajorLocator)
ax.xaxis.grid(False, which='major')
plt.legend()
plt.tick_params(direction='in')
plt.xlim(-10,100)
plt.savefig(today+'_YoungModuls_PCLPLA.png',dpi=400)
plt.show()