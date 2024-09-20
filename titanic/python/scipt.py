import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns 

#load data
train = pd.read_csv(r'titanic\train.csv')
test = pd.read_csv(r'titanic\test.csv')


# train.head()
train.info()
# train.describe()

#null values
print(train.isnull().sum())


sns.countplot(x='Survived', data=train)
plt.title('Distribution of Survival')
plt.show()


sns.countplot(x='Survived', hue='Sex', data=train)
plt.title('Survival by Gender')
plt.show()

sns.countplot(x='Survived', hue='Pclass', data=train)
plt.title('Survival by Gender')
plt.show()