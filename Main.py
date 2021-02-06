# -*- coding: utf-8 -*-
"""
Created on Sat Oct 31 10:49:11 2020

@author: 23168
"""
#绘制所有拉伸测试图
import 组合图
import 断裂伸长比
#此处输入杨氏模量csv文件
path1 = lambda :'C:/Users/23168/Desktop/tensiledata/YoungModuls.csv'
#此处输入抗拉强度csv文件
path2 = lambda :'C:/Users/23168/Desktop/tensiledata/tensile.csv'
#此处输入断裂伸长比csv文件
path3 = lambda :'C:/Users/23168/Desktop/tensiledata/Elongation at break ratio.csv'
def main():  
    组合图.plot_combo()
    断裂伸长比.plot_elongation()
if __name__ == '__main__':
    main()