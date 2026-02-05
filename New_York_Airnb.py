#!/usr/bin/env python
# coding: utf-8

# In[219]:


import pandas as pd

data=pd.read_csv( r"C:/Users/DELL LATITUDE E7450/Desktop/data_airnb_New_York/datasets.csv")


# In[220]:


data


# In[221]:


# command give us the last 5 rows
data.tail


# In[223]:


data.shape


# In[225]:


data.info()


# In[226]:


 # statistical summary
data.describe()


# # Data Cleaning 
# 

# In[228]:


# to look how namy missing values we got 
data.isnull().sum()


# In[230]:


# dropping a missing value
data.dropna(inplace=True)


# In[231]:


# to check if all value has been drop off
data.isnull().sum()


# In[232]:


data.shape


# In[ ]:


#data.fillna (inplace=true)


# In[237]:


# to chech the duplicate columns
data.duplicated().sum()
# we have 12 lines duplicates 


# In[242]:


# to see the duplicate record
#  data.duplicated() it works too
data[ data.duplicated()]


# In[244]:


# deleted all duplicated complicated
data.drop_duplicates( inplace= True)


# In[245]:


# to visualize if all duplicated columns have been dropped 
data.duplicated().sum()
# We have zero duplicated np.int(zero duplicated)


# In[250]:


# type  Casting 
# to change the type 
data.dtypes
data['id'] =data['id']  .astype(object)
data ['host_id ']= data[ 'host_id'].astype ( object)
data.dtypes


# # Data Analysis

# ** Univariable Analysis**

# In[252]:


# price distribution 
data ['price']


# In[ ]:





# In[257]:


import matplotlib.pyplot as plt
import seaborn as sns
sns.histplot( data=data , x='price')


# In[259]:


#identify outliners in price
sns.boxplot( data= data , x='price')


# In[262]:


df =  data[data[ 'price']< 1500]
sns.boxplot( data= df , x='price')


# In[265]:


plt.figure( figsize=(8,5))
sns.histplot( data=df, x='price')
plt.ylabel( "frequency")


# In[272]:


plt.figure( figsize=(8,5))
sns.histplot( data=df, x='price', bins = 100)
plt.title(" Price Distribution")
plt.ylabel( "frequency")


# In[267]:


df.columns


# In[271]:


data.dtypes


# # Distribution of Availability

# In[274]:


plt.figure( figsize=(6,3))
sns.histplot( data=df, x='price', bins = 100)
plt.title(" availability_365 distribution")
plt.ylabel( "frequency")


# In[276]:


data.dtypes


# In[278]:


df.groupby(by='neighbourhood_group')['price'].mean()


# In[279]:


df.head()


# features Engineering

# In[281]:


# ['price by bed']
df['price per bed'] = df['price']/ df['beds']


# In[282]:


df.head()


# In[284]:


#price per bed 

df.groupby(by='neighbourhood_group')['price'].mean()


# In[285]:


df.groupby(by='neighbourhood_group')['price per bed'].mean()


# # BI Variable analysis

# In[ ]:


# one variable depenency in another variable 


# In[287]:


df.columns


# In[289]:


sns.barplot ( data=df , x= 'neighbourhood_group', y ='price')


# In[290]:


# Price depenency on neighborhood
sns.barplot ( data=df , x= 'neighbourhood_group', y ='price', hue = 'room_type')


# In[294]:


# number reviews and price 

plt.figure(figsize= (10,8))
sns.scatterplot ( data=df , x= 'number_of_reviews_ltm', y ='price', hue = 'neighbourhood_group')
plt.title(" locality and review depenency")


# In[301]:


# different depenency between many variables 
import matplotlib.pyplot as plt
import seaborn as sns

sns.pairplot(
    data=df,
    vars=['price', 'minimum_nights', 'number_of_reviews', 'availability_365'],
    hue='room_type'
)
plt.show()


# In[302]:


data.dtypes


# In[308]:


# geographic Distributions 
import matplotlib.pyplot as plt
import seaborn as sns
sns.scatterplot ( data= df , x = 'longitude', y= 'latitude' , hue = 'room_type')
plt.title ("Geographical distribution of Airnb


# In[ ]:


#-- heat.map- Correlation of one varibale with others numberical variable


# In[309]:


data.dtypes


# In[315]:


corr= df[['latitude','longitude', 'price', 'minimum_nights','number_of_reviews','availability_365','beds']].corr()
corr


# In[316]:


import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize=(10, 8))
sns.heatmap(corr, annot=True, cmap='coolwarm', fmt=".2f")
plt.show()


# In[318]:


# 2 second meth0d 
corr= df[['latitude','longitude', 'price', 'minimum_nights','number_of_reviews','availability_365','beds']].corr()
corr
sns.heatmap(data=corr, annot=True)


# In[ ]:




