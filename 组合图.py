# -*- coding: utf-8 -*-
"""
Created on Fri Oct 30 23:31:51 2020

@author: 23168
"""

import csv
import pandas as pd
import matplotlib.pyplot as plt
import time
import Main
from matplotlib.ticker import MultipleLocator,FormatStrFormatter #副刻度，可选
def plot_combo():
#此处读取数据路径
    filename = Main.path1()
    filename2 = Main.path2()
    today = time.strftime("%y-%m-%d",time.localtime(time.time()))
    with open(filename,'r') as f:
        reader = csv.reader(f)
    with open(filename2,'r') as f2:
        reader = csv.reader(f2)
    #读取特定列，列名为csv文件第一列字符串。
    x1 = pd.read_csv(filename, usecols=['Sample'])
    y1 = pd.read_csv(filename, usecols=['YoungModuls'])
    y2 = pd.read_csv(filename2, usecols=['Tensile Strength'])
    #设置单位主刻度，视样品而定
    xmajorLocator = MultipleLocator(25) 
    #使用subplots创建窗口
    fig, ax1 = plt.subplots(1, 1)  
    #创建第二个坐标轴，本质上是画与子图1重叠的子图2.
    ax2 = ax1.twinx()
    #画子图1模量
    ax1.plot(x1, y1,'b',marker ='^',label='Young\'s Modulus',linewidth = 1)
    ax1.set_xlabel('Sample(%)',fontdict={'family':'Arial','size':18,'style':'oblique'})
    ax1.set_ylabel('Young\'s Modulus(Mpa)',fontdict={'family':'Arial','size':15,'style':'oblique'})
    ax1.legend(loc=2)
    ax1.tick_params(direction='in')
    ax1.xaxis.set_major_locator(xmajorLocator)
    ax1.xaxis.grid(False, which='major')
    
    #画子图2抗拉强度
    ax2.plot(x1, y2,'r',marker ='o',label='TensileStrength',linewidth = 1)
    ax2.set_xlabel('Sample(%)',fontdict={'family':'Arial','size':18,'style':'oblique'})
    ax2.set_ylabel('TensileStrength(Mpa)',fontdict={'family':'Arial','size':15,'style':'oblique'})
    ax2.legend(loc=4)
    ax2.tick_params(direction='in')
    ax2.xaxis.set_major_locator(xmajorLocator)
    ax2.xaxis.grid(False, which='major')
    
    #调整刻度，保存图片
    plt.xlim(-10,90)
    plt.savefig(today+'Combo_PCLPLA.png',dpi=400)
    plt.show()