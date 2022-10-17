#!/usr/bin/env python
# coding: utf-8

# In[54]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go


# In[55]:


data = pd.read_csv('C:/Users/Rakesh/Datasets/apple_products.csv')


# In[56]:


data.head()


# In[57]:


data.isnull().sum()


# In[58]:


data.describe()


# # Highest rated iphones in India(Flipkart)

# In[59]:


highest_rated= data.sort_values(by=['Star Rating'], ascending=False)


# In[60]:


highest_rated.head(10)


# # Number of ratings for iphones for the top 10

# In[61]:


highest_rated= highest_rated.head(10)


# In[62]:


iphones=highest_rated['Product Name'].value_counts()


# In[63]:


label=iphones.index


# In[64]:


counts=highest_rated['Number Of Ratings']


# In[65]:


figure=px.bar(highest_rated,x=label,y=counts, title= 'Number of ratings of highest rated iphones')
figure.show()


# APPLE iPhone 8 Plus (Gold, 64 GB) has the most ratings on Flipkart

# # Number of reviews of the highest-rated iPhones on Flipkart

# In[66]:


iphones= highest_rated['Product Name'].value_counts()


# In[67]:


label=iphones.index


# In[68]:


counts=highest_rated['Number Of Reviews']


# In[69]:


figure=px.bar(highest_rated,x=label,y=counts)


# In[70]:


figure.show()


# # Finding a relationship between sale price of iphones and their ratings in flipkart

# In[71]:


figure=px.scatter(data,x='Number Of Ratings',y='Sale Price',size='Discount Percentage', trendline='ols', title='Relationship between saleprice and number of ratings in flipkart')


# In[72]:


figure.show()


#  Here there is a negative linear relationship which means iphones with lower price are sold in India

# # Relationship between discount percentage and number of ratings for iphones

# In[73]:


figure= px.scatter(data,x='Number Of Ratings', y='Discount Percentage',size='Sale Price',  trendline='ols', title='Relationship between discount percentage and number of ratings for iphones')


# In[74]:


figure.show()


# In[75]:


data.head()

