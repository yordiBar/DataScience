import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv('Data.csv')

# matrix of features -> x
# iloc function = locate indexes, : = range (all rows), :-1 all columns except last one
# features in first column and dependant variable vector in last column
x = dataset.iloc[:, :-1].values

# dependant variable vector -> y
y = dataset.iloc[:, -1].values
print(x)
print(y)
