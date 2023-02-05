# Predicting-work
Simple linear regression model regarding data as to when my brother works. Still pretty
far from having enough data to make it any useful. When the data is usable, though, I
will be sure to add visualization methods to the model.

## Abstract
My brother has a very unpredictable schedule. He claims that it, in no way, could be
predicted. I disagree, to the extent that I intend to prove him wrong as a project I
could work on before school starts.

## Method
Using Python's `tensorflow` library, I took the time to learn and apply linear regression
techniques in order to analyze and predict my brother's schedule. My linear regression
model is stored in `model.ipynb`

## Results
I don't have an incredible amount of data, so I'm not running too many epochs as to not
overfit the model to the data. All in all, though, it's looking pretty good. Note: the
amount of the testing data is half of the input data.

Accuracy as of this week's data:

![Accuracy is at 90% after only 10 epochs.](https://github.com/R-Rothrock/Predicting-work/blob/b43649df8e3de0199c56c4c0726bc58639ccb0b0/assets/this_week_accuracy.png)

NOTE
---
I used `tf.estimator.LinearClassifier` which doesn't have a method of getting data for
every epoch, unless, of course, you used it the way I did, which isn't very pretty.
I also couldn't seem to find a working method for suppressing the output.

### info
- author: Roan Rothrock
- email: roan.rothrock@hotmail.com
