# -*- coding: utf-8 -*-
# model.py
"""
Linear regression model for the prediction of field
`work` in `input_data.csv`
"""

import numpy as np
import pandas as pd
import tensorflow as tf
import tensorflow.compat.v2.feature_column as fc

def input_fn(data_df, label_df, *, nr_epochs=10,
             shuffle=True, batch_size=32):
    data = tf.data.Dataset.from_tensor_slices(
    (dict(data_df), label_df))
    if shuffle: data = data.shuffle(512)
    data = data.batch(batch_size).repeat(nr_epochs)
    return data

def get_feature_column(categorigals: list, numerics: list, df):
    feature_columns_ret = list()
    for feature_name in categorigals:
        vocab = df[feature_name].unique()
        feature_columns_ret.append(
            tf.feature_column.categorical_column_with_vocabulary_list(
                feature_name, vocab))

    for feature_name in numerics:
        feature_columns_ret.append(
            tf.feature_column.numeric_column(
                feature_name, dtype=tf.float32))
    return feature_columns_ret

dftrain = pd.read_csv('./input_data.csv')
dfeval  = pd.read_csv('./test_data.csv')

y_train = dftrain.pop('work')
y_eval  = dfeval.pop('work')

#print(dftrain.shape)

# columns
CATEGORICAL_COLUMNS = ["day_of_week"]
NUMERIC_COLUMNS    = [
    "work",
    "month",
    "day",
    "holiday"
]

feature_columns = get_feature_column(CATEGORICAL_COLUMNS,
                                     NUMERIC_COLUMNS, dftrain)

train_input_fn = lambda: input_fn(dftrain, y_train)
eval_input_fn  = lambda: input_fn(dfeval, y_eval, nr_epochs=1, shuffle=False)

linear_est = tf.estimator.LinearClassifier(feature_columns=feature_columns)

linear_est.train(train_input_fn)
result = linear_est.evaluate(eval_input_fn)

# data visualization
result = list(linear_est.predict(eval_input_fn))

