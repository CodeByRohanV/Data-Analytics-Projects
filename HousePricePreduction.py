import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sb
from sklearn.preprocessing import OneHotEncoder

df = pd.read_excel("HousePricePrediction.xlsx")
# print(df.head())
print(df.shape) # is attribute 

obj = df.dtypes == 'object' 
obj_list = list(obj[obj].index)
print(f"Total objects : {len(obj_list)}" )

integerss = df.dtypes == 'int64'
int_list = list(integerss[integerss].index)
print("int", len(int_list))


decimals = df.dtypes == 'float'
float_list = list(decimals[decimals].index)
print("float" ,len(float_list))

numData = df.select_dtypes(include='number')
plt.figure(figsize=(12,5))
sb.heatmap(numData.corr(),cmap='BrBG', annot=True,fmt='.2f',linewidths=3)
plt.show()  # understood how to read cooleration data and give correct suggestions 

#Bar graph for number of categorial feature in the varibles obj

emptybox = []
for i in obj_list:
    emptybox.append(df[i].unique().size)
plt.figure(figsize=(12,6))
plt.title('No. Unique values of Categorical Features')
plt.xticks(rotation=90)
sb.barplot(x=obj_list,y=emptybox)
# plt.show()

#Bar graph for individual categorial 

plt.figure(figsize=(120,50))
plt.title("lll")
index =1
plt.xticks(rotation=90)

for col in obj_list:
    y = df[col].value_counts()
    plt.subplot(2,2,index)
    plt.xticks(rotation=90)

    sb.barplot( x= y.index, y = y.values)
    index+=1
# plt.show()

df.drop(['Id'],inplace=True,axis=1) # axis target coloums

df['SalePrice'] = df['SalePrice'].fillna(df['SalePrice'].mean())

newDF = df.dropna()
print(newDF.isnull().sum())

newOnj = newDF.dtypes == 'object'  #dtype is attribute not method
realObjects = newOnj[newOnj].index
print(realObjects)
print(len(realObjects))

oh_encoder = OneHotEncoder(sparse_output=False,handle_unknown="ignore")
encoded_df = pd.DataFrame(oh_encoder.fit_transform(newDF[realObjects]))
encoded_df.index = newDF.index
encoded_df.columns = oh_encoder.get_feature_names_out()
finalDf = newDF.drop(realObjects,axis=1)
finalDf = pd.concat([encoded_df,finalDf],axis=1)


from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split

X = finalDf.drop(['SalePrice'], axis=1)
Y = finalDf['SalePrice']
Xtrain,Xtest,Ytrain,Ytest = train_test_split(X,Y,train_size=0.8,test_size=0.2,random_state=0)

# predection from support vector machine
from sklearn import svm
from sklearn.metrics import mean_absolute_percentage_error
from sklearn.ensemble import RandomForestRegressor

model_SVR = svm.SVR()
QA = model_SVR.fit(Xtrain,Ytrain)
predectAns=model_SVR.predict(Xtest)
print("predected answer ", predectAns[:4])
print(Ytest.head(4))

# predection from  random forest 
model_rfr = RandomForestRegressor(n_estimators=10)
learning_pharse = model_rfr.fit(Xtrain,Ytrain)
preduct = model_rfr.predict(Xtest)
print(mean_absolute_percentage_error(Ytest,preduct))





