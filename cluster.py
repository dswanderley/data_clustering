# -*- coding: utf-8 -*-
"""
Created on Thu Sep 13 11:55:58 2018

@author: Diego
"""

import csv
#import numpy as np


path = 'C:/Users/Diego/Dropbox/INESC/SCREEN-DR/Data/Tables/'
csv_file = 'BigTable.csv';

bigtable = []

with open(path + csv_file) as csvfile:
    readCSV = csv.reader(csvfile, delimiter=';')
    for row in readCSV:
        bigtable.append(row)

header = bigtable[0]
eye_data = bigtable[1:]