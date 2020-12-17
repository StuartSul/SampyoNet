# **Sampyo & SNU : SampyoNet**

Convolutional neural network developed by Seoul National University for Sampyo Cement to facilitate an automated assessment of gravel quality.



### Instructions

1. Using Python 3, download all the requirements via `requirements.txt`.

   ```bash
   python3 -m pip install -r requirements.txt
   ```

2. Run the following command to predict on single image

   ```bash
   python3 main.py -w models/[WEIGHTS_FILE].hdf5 -i [IMAGE_FILE].jpg
   ```

3. Run the following command to predict on a set of images specified through a CSV file

   ```bash
   python3 main.py -w models/[WEIGHTS_FILE].hdf5 -a [CSV_FILE].csv
   ```

4. Implement into applications using the wrapper function `predict_image` in `main.py`

5. To further train the model, TensorFlow training script must be added. This is just a few more lines of code which can be written very easily. The code is not included here for simplicity.



### Project Structure

`main.py` contains the wrapper functions for running the model and can be initiated directly from the command line.

`model.py` defines the model schema.

`config.py` has all the required import statements and global parameters which should not be modified.

`brightness.py` contains the functions which calculate the brightness of the input image.

`requirements.txt` lists all the dependencies.

`models/` is a directory with all pretrained weights in it. Our main model is `2_largfac.hdf5`

`preprocess/` is a directory with sources used in preprocessing stage.



### Reference

This model was inspired by SediNet, a deep learning convolutional neural network made by Dr. Daniel Buscombe (github repo: https://github.com/MARDAScience/SediNet)
