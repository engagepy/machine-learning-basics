import pandas as pd
import numpy as np

coffee = pd.read_csv('test.csv')

## add code below
## get spent feature
spent = coffee['spent']
print(spent)
print("___")

#find the max spent
max_spent = np.max(spent)
print(f'Max spend : {max_spent}')
#find the min spent
min_spent = np.min(spent)
print(f'Min spend : {min_spent}')
print("____")
#find the difference
spent_range = max_spent - min_spent

#normalize your spent feature
spent_normalized = (spent - min_spent)/(max_spent - min_spent)

#print your results
print(spent_normalized)