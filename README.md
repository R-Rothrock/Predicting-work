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
As it currently stands, I still have very little data, and I have two training data
columns for every testing data column.

Below is the total loss per epoch.

![Total loss graph](https://github.com/R-Rothrock/Predicting-work/blob/044b2d1780431059592e31ec455b02b8de1892b2/assets/asset3.png)

Before the last week of data had been added to the model, this was my loss calculation by epoch.

![Previous loss graph](https://github.com/R-Rothrock/Predicting-work/blob/f8c8c7f970d19d033a62a0fc8097dc8970bb31d0/assets/asset2.png)

I will be sure to continue adding data as time passes. In the meantime, though, I seem
to be getting marginally worse results. If you take the time to look in the `./assets`
directory, you can reference `asset1.png` as the results of the first week of data,
`asset2.png` for the next week, etc. This latest week it took over 70 epochs to get a
loss of less than %40.

NOTE
---
I used `tf.estimator.LinearClassifier` which doesn't have a method of getting data for
every epoch, unless, of course, you used it the way I did, which isn't very pretty.
I also couldn't seem to find a working method for suppressing the output.

### info
- author: Roan Rothrock
- email: roan.rothrock@hotmail.com
