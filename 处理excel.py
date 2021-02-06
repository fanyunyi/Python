# -*- coding: utf-8 -*-
"""
Created on Fri Oct 23 19:37:44 2020

@author: 23168
"""

import xlrd
book1 = xlrd.open_workbook('C:/Users/23168/Desktop/20201022tensile.xlsx')


for sheet in book1.sheets():
    print(sheet.name)
sheet = book1.sheet_by_name('20201020fan')
print(sheet)
for i in range(sheet.nrows):
    print(sheet.row_values(i))