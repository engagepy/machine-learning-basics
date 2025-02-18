import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler

coffee = pd.read_csv('test.csv')
spent = coffee['spent']
print(spent.head(10))
spent_reshaped = np.array(spent).reshape(-1,1)
mmscaler = MinMaxScaler()
reshaped_scaled = mmscaler.fit_transform(spent_reshaped)
print(np.min(reshaped_scaled))
print(np.max(reshaped_scaled))
val = set(np.unique(reshaped_scaled))

val_counts = pd.Series(list(val)).value_counts()
val_counts.plot(kind='pie')

plt.show()
