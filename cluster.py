# -*- coding: utf-8 -*-
"""
Created on Thu Sep 13 11:55:58 2018

@author: Diego
"""

import csv
#import numpy as np
import datetime
from dateutil.relativedelta import relativedelta

from utils.dataclass import Quality, RD, Sex, Laterality

path = 'C:/Users/Diego/Dropbox/INESC/SCREEN-DR/Data/Tables/'
csv_file = 'BigTable.csv';

bigtable = []

with open(path + csv_file) as csvfile:
    readCSV = csv.reader(csvfile, delimiter=';')
    for row in readCSV:
        bigtable.append(row)

header = bigtable[0]
eye_data = bigtable[1:]

params = []
grading = []

for data in eye_data:
    
    rid = data[0]    # id
    
    if Quality.BAD != Quality[data[18]]:
        # Age
        acq_date = data[3]    # acquisition_datetime
        acq_date = datetime.date(int(acq_date[:4]), int(acq_date[5:7]), int(acq_date[8:10]))
        birth = data[13]   # patient_birthdate
        birth = datetime.date(int(birth[:4]), int(birth[5:7]), int(birth[8:10]))
        age = relativedelta(acq_date, birth).years
            
        lat = Laterality[data[5]].value   # laterality
        sex = Sex[data[12]].value   # patient_sex
        
        # Append parameters  
        params.append([rid, age, lat, sex])
        
        # Grading
        str_rd = data[21]
        str_rd = str_rd[:2]
        rd_grad = RD[str_rd].value   # retinopathy
        grading.append(rd_grad)
        
