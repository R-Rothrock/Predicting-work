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
As it currently stands, I still have very little data, and I have two training data columns for every testing data column. I'm confused, though, how I managed to be 120% incorrect on the second epoch. If I had you guess a number I had thought of between 1 and 10 on 11 different occasions, you _should_ get about 1, maybe 0. How, though, would you get 120% of the guesses wrong?

Below is the total loss per epoch.

![Total loss graph](https://github.com/R-Rothrock/Predicting-work/blob/f8c8c7f970d19d033a62a0fc8097dc8970bb31d0/assets/asset2.png)

Before the last week of data had been added to the model, this was my loss calculation by epoch.

![Previous loss graph](https://raw.githubusercontent.com/R-Rothrock/Predicting-work/408abbda67e4577b7d6352b3279c0336814d44e6/assets/asset1.png)

I will be sure to continue adding data as time passes.

### info
- author: Roan Rothrock
- email: roan.rothrock@hotmail.com