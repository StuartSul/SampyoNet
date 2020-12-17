# Preprocessing Sources

This directory contains source codes used to preprocess gravel images provided by Sampyo.

## Instructions

### Preprocess raw images and make label csv file

1. Using pip download pandas, rename

   `pip install pandas`
   `pip install rename`

2. Make sure unzipped raw-image folder is in this directory (e.g. 1_풍납) and its subdirectory is month. If not, move subdirectories with 'mv * ../'.

    ```bash
    preprocess1 -> 1_풍납 -> 01월 -> 풍납-GXXX -> images.jpg
    ```

3. Modify root directory in preprocess.sh and labeling.py.

4. Modify directory where the processed images and label csv files should be saved.

5. Run the following command to move and rename images. 

   ```bash 
   bash ./preprocess.sh gravel
   ```
6. (By default) Image files will be saved in images folder in home directory. Label csv file will be saved in data folder in home directory.


### Split Training set and Test set

You can split training set and test set by 2 methods : random, rule(for categorical use) 

#### by random

1. Using pip download sklearn

   `pip install sklearn`

2. Modify file directories in splitTrainTest_by_random.py (label csv file you want to split, train csv file, test csv file)

3. Modify test_ratio you want to use.

4. Run the following command to split training set and test set. 

   `python3 splitTrainTest_by_random.py`

#### by rule

1. Modify file directories in splitTrainTest_by_rule.py (label csv file you want to split, train csv file, test csv file)

2. Modify the rule you will constitute train (or test) set. (By default, training set has 600 data each from class 0, class 1, class 2)

3. Run the following command to split training set and test set.

   `python3 splitTrainTest_by_rule.py`
