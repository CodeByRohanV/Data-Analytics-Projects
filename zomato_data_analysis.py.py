import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb
dataframe = pd.read_csv("Zomato-data-.csv")
# print(dataSet.head())

def handleRate(value): #takes only numinator
  value = str(value).split("/")
  value = value[0]
  return float(value)
# this function helps us take data and clean it because that colunm contains datas like str nan int 

dataframe['rate'] = dataframe['rate'].apply(handleRate)
dataframe.info()
# Checking for missing or null values to identify any data gaps.
print(dataframe.isnull().sum())

# use seaborn to check the Comparasion between groups 
sb.countplot(x=dataframe['listed_in(type)'])
plt.xlabel("Type of restaurant")
# plt.show()

# need to rate restaurant as per vote 
holdVotes = dataframe.groupby('listed_in(type)')['votes'].sum()
result = pd.DataFrame({'votes': holdVotes})
plt.plot(result, c="green", marker='*')
plt.xlabel("Type of restaruant")
plt.ylabel("votes")
plt.show()

sb.countplot(x=dataframe['online_order'])
plt.show()

# histogram
plt.hist(dataframe['rate'], bins=5)
plt.show()

sb.countplot(x= dataframe['approx_cost(for two people)'])
plt.xlabel("cost")
plt.show()

plt.figure(figsize=(6,6))
sb.boxplot(x="online_order",y="rate", data=dataframe)
plt.show()