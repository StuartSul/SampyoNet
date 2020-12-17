import pandas as pd
import numpy as np

#modify file name you want to split into train and test set
data = pd.read_csv('./gravel_clay_class3_total.csv')

#modify how you want to split your data in train set
class0 = data[data['class'] == 0]
class0_sample = class0.sample(n=600)
class1 = data[data['class'] == 1]
class1_sample = class1.sample(n=600)
class2 = data[data['class'] == 2]
class2_sample = class2.sample(n=600)
allData = [class0_sample, class1_sample, class2_sample]
trainData = pd.concat(allData, axis=0, ignore_index=True)

#modify file name of your traing set
trainData.to_csv('./gravel_clay_class3_total_balanced_train.csv',index=False)

bothData = [data,trainData]
testData = pd.concat(bothData, axis=0, ignore_index=True)
testData.drop_duplicates(keep=False,inplace=True)

#modify file name of your test set
testData.to_csv('./gravel_clay_class3_total_balanced_test.csv',index=False)
