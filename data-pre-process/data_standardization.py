import pandas as pd
import numpy as np
import matplotlib as plt

coffee = pd.read_csv('test.csv')
ages = coffee['age']

## add code below
mean_age = np.mean(ages)
std_dev_age = np.std(ages)
ages_standardized = (ages - mean_age)/std_dev_age
print(np.mean(ages_standardized))
print(np.std(ages_standardized))


