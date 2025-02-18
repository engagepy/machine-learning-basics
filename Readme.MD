# Machine Learning Basics For All - W.I.P

> Instruction on Using This Repository Are At The Bottom

> Github Page Site: [Machine Learning Basics](https://engagepy.github.io/machine-learning-basics/)

## Table of Contents

## Introduction To Machine Learning Basics

Machine learning is a subset of artificial intelligence that focuses on the development of computer programs that can teach themselves to grow and change when exposed to new data. The process of machine learning is similar to that of data mining. Both systems search through data to look for patterns. However, instead of extracting data for human comprehension - as is the case in data mining applications machine learning uses that data to detect patterns in data and adjust program actions accordingly.

## Types of Machine Learning

There are three types of machine learning:

1. Supervised Learning
2. Unsupervised Learning
3. Reinforcement Learning

### Supervised Learning

Supervised learning is the most common type of machine learning. It is the method of teaching the machine by example. The algorithm is trained on a labeled dataset, which means some input data is already tagged with the correct output. The algorithm learns to map the input to the output and makes predictions based on the input data. The goal of supervised learning is to approximate the mapping function so well that when you have new input data, you can predict the output variables for that data.

### Unsupervised Learning

Unsupervised learning is a type of machine learning that looks for previously undetected patterns in a data set with no pre-existing labels. The system is not told the "right answer." The algorithm must figure out what is being shown. The goal is to explore the data and find some structure within it. Unsupervised learning is used for clustering population in different groups.

### Reinforcement Learning

Reinforcement learning is a type of machine learning that is about taking suitable action to maximize reward in a particular situation. It is employed by various software and machines to find the best possible behavior or path it should take in a specific situation. Reinforcement learning differs from the supervised learning in a way that in supervised learning the training data has the answer key with it so the model is trained with the correct answer itself whereas in reinforcement learning, there is no answer but the reinforcement agent decides what to do to perform the given task.


## Machine Learning Algorithms

There are several machine learning algorithms, and they can be broadly classified into three categories:

1. Supervised Learning Algorithms

- Linear Regression
- Logistic Regression
- Decision Trees
- Random Forest
- Gradient Boosting
- Support Vector Machines
- Neural Networks

2. Unsupervised Learning Algorithms

- K-Means Clustering
- Hierarchical Clustering
- Principal Component Analysis
- Independent Component Analysis
- Singular Value Decomposition
- Apriori Algorithm
- Expectation-Maximization Algorithm

3. Reinforcement Learning Algorithms

- Q-Learning
- SARSA
- Deep Adversarial Networks
- Deep Deterministic Policy Gradient
- Asynchronous Advantage Actor-Critic

## Machine Learning Models

Machine learning models are used to make predictions based on data. There are several types of machine learning models, including:

1. Linear Regression
2. Logistic Regression
3. Decision Trees
4. Random Forest
5. Gradient Boosting
6. Support Vector Machines
7. Neural Networks
8. K-Means Clustering
9. Hierarchical Clustering
10. Principal Component Analysis
11. Independent Component Analysis
12. Singular Value Decomposition
13. Apriori Algorithm
14. Expectation-Maximization Algorithm
15. Q-Learning
16. SARSA
17. Deep Adversarial Networks
18. Deep Deterministic Policy Gradient
19. Asynchronous Advantage Actor-Critic

## Data Preprocessing

Data preprocessing is an important step in machine learning. It involves transforming raw data into a format that is suitable for analysis. Data preprocessing can include several steps, such as:

1. Data Cleaning
2. Data Transformation
3. Data Reduction
4. Data Discretization
5. Data Normalization
6. Data Binning

Data preprocessing is essential because it helps to improve the quality of the data and make it easier to analyze. It also helps to reduce the time and effort required to train machine learning models.


## Conclusion

Machine learning is a powerful tool that can be used to make predictions based on data. It is a subset of artificial intelligence that focuses on the development of computer programs that can teach themselves to grow and change when exposed to new data. There are three types of machine learning: supervised learning, unsupervised learning, and reinforcement learning. Each type of machine learning has its own set of algorithms that can be used to make predictions based on data. Machine learning algorithms can be broadly classified into three categories: supervised learning algorithms, unsupervised learning algorithms, and reinforcement learning algorithms.

## References

1. [Fundamentals of Machine Learning](https://codecademy.com) 
2. [Machine Learning Basics](https://www.geeksforgeeks.org/machine-learning-basics/)
3. [Machine Learning](https://en.wikipedia.org/wiki/Machine_learning) 


# To use this repository, you can clone and run it using the following commands:

```bash\n
git clone https://github.com/engagepy/machine-learning-basics.git
```
```bash\n
python3 -m venv env
```
```bash\n
source env/bin/activate
```
```bash\n
pip install -r requirements.txt
```
```bash\n
python3 <filename>.py
```

## Project File Structure

> Each `folder` is a Topic, each `file.py` therein a lesson covering a specific subject pertinent to machine learning.

### data-pre-process

- data_centereing.py - Data Centering in Machine Learning

> 🔑`centered_data = data - mean`

- data_standardization.py - Data Standardization in Machine Learning

> 🔑`standardized_data = (data - mean)/std_dev`

- standard_scaler.py - Standardization in Machine Learning

> 🔑`sklearn.preprocessing import StandardScaler`

- mix_max_normalization.py - Min-Max Normalization 

> 🔑`spent_normalized = (spent - min_spent)/(max_spent - min_spent)`

- min_max_scaler.py - MinMaxScaler in Machine Learning 

> 🔑`sklearn.preprocessing import MinMaxScaler`

- binning.py - Binning Data in Machine Learning 

> 🔑`pd.cut(ages,age_bins, right=False)`




### pre-training

> W.I.P

### model-training

> W.I.P

### post-training

> W.I.P

### model-evaluation

> W.I.P

### model-deployment

> W.I.P

### model-monitoring

> W.I.P

### model-optimization

> W.I.P

### model-interpretation

> W.I.P

### model-visualization

> W.I.P

### model-automation

> W.I.P