import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv("D:\py\student_exam\Expanded_data_with_more_features.csv")
print(df.head())

print(df.describe())
print(df.info())
print(df.isnull().sum())
df=df.drop("Unnamed: 0",axis=1)
print(df.head())

#gender distribution
a=sns.countplot(data=df,x= "Gender")
plt.title("Gender distribution")
plt.show()



#check results based on parent education
group_by=df.groupby("ParentEduc").agg({"MathScore":'mean',"ReadingScore" :'mean', "WritingScore":'mean'})
print(group_by)


sns.heatmap(group_by,annot=True)
plt.title("Relation between parent education and student score")
plt.show()



#check results based on parent's marital status
group_by1 =df.groupby("ParentMaritalStatus").agg({"MathScore":'mean',"ReadingScore" :'mean', "WritingScore":'mean'})
print(group_by1)

sns.heatmap(group_by1,annot=True)
plt.title("Relation between parent marital status and student score")
plt.show()


sns.boxplot(data=df, x="MathScore")
plt.show()


print(df['EthnicGroup'].unique())

#percent distribution of ethnic group
grpA=df.loc[(df['EthnicGroup'] == 'group A')].count()
grpB=df.loc[(df['EthnicGroup'] == 'group B')].count()
grpC=df.loc[(df['EthnicGroup'] == 'group C')].count()
grpD=df.loc[(df['EthnicGroup'] == 'group D')].count()
grpE=df.loc[(df['EthnicGroup'] == 'group E')].count()

lbl=['Group A', 'Group B', 'Group C', 'Group D', 'Group E' ]
lst=[grpA['EthnicGroup'], grpB['EthnicGroup'], grpC['EthnicGroup'], grpD['EthnicGroup'], grpE['EthnicGroup']]
plt.pie(lst, labels=lbl, autopct="%1.2f%%")
plt.title("Distribution of ethnic groups")
plt.show()

