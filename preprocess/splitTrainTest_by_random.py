import os
import sys
import csv
import pandas as pd
from sklearn.model_selection import train_test_split

# modify root_dir according to your repo
root_dir = '/home/stuartsul/J6-Sampyo_SediNet'
test_rate = 0.3

# modify file you want to split into training and test set
gd_dir = root_dir+'/data/gravel_clay_class3_all_balanced.csv'
gd_train_dir = root_dir+'/data/gravel_clay_class3_all_balanced_train.csv'
gd_test_dir = root_dir+'/data/gravel_clay_class3_all_balanced_test.csv'

gd_csv = pd.read_csv(gd_dir,encoding='utf-8')
gd_train, gd_test = train_test_split(gd_csv,test_size=test_rate)
gd_train.to_csv(gd_train_dir,na_rep='NaN',encoding='utf-8',index=False)
gd_test.to_csv(gd_test_dir,na_rep='NaN',encoding='utf-8',index=False)

