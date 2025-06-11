#!/usr/bin/env python
# coding: utf-8

# # Financial Data Analysis

# #### Importing the pandas library

# In[1]:


import pandas as pd


# #### Reading the csv file and creating a dataframe

# In[2]:


df = pd.read_csv(r"C:\Users\devik\OneDrive\Desktop\BCGdata.csv")


# #### Displaying the dataframe

# In[3]:


print(df)


# #### Removing the commas and spaces & converting the string values to numeric

# In[4]:


cols = ["Total Revenue", "Net Income", "Total Assets", "Total Liabilities", "Cash Flow from Operating Activities"]

for i in cols:
    df[i] = df[i].astype(str).str.replace(",","").str.replace("\xa0","").str.strip()
    df[i] = pd.to_numeric(df[i], errors = "coerce")
    
df["Year"] = df["Year"].astype(int)


# #### Sorting the values in the dataframe by the company and year

# In[5]:


df = df.sort_values(by=["Company","Year"], ascending=[True,True])
print(df)


# #### Adding new columns which contain the year over year change in percentage

# In[6]:


for i in cols:
    df[f"{i} Growth %"] = df.groupby("Company")[f"{i}"].pct_change()*100
print(df)


# #### Plotting graphs 

# In[7]:


import matplotlib.pyplot as plt
import seaborn as sns


# ##### Total Revenue over the years for each company

# In[8]:


plt.figure(figsize=(8,4))
sns.lineplot(data=df, x="Year", y="Total Revenue" ,hue = "Company", marker="o")
plt.title("Total Revenue over the years for each Company")
plt.grid()
plt.tight_layout()
plt.show()


# ##### Net Income over the years for each company

# In[9]:


plt.figure(figsize=(8,4))
sns.lineplot(data=df, x="Year" , y="Net Income" , hue="Company", marker="o")
plt.title("Net Income over the years for each company")
plt.grid()
plt.tight_layout()
plt.show()


# ##### Total Assets over the years for each company

# In[10]:


plt.figure(figsize=(8,4))
sns.lineplot(data=df, x="Year" , y="Total Assets" , hue="Company", marker="o")
plt.title("Total Assets over the years for each company")
plt.grid()
plt.tight_layout()
plt.show()


# ##### Total Liabilities over the years for each company

# In[11]:


plt.figure(figsize=(8,4))
sns.lineplot(data=df, x="Year" , y="Total Liabilities" , hue="Company", marker="o")
plt.title("Total Liabilities over the years for each company")
plt.grid()
plt.tight_layout()
plt.show()


# ##### Cash Flow from Operating Activities over the years for each company

# In[12]:


plt.figure(figsize=(8,4))
sns.lineplot(data=df, x="Year" , y="Cash Flow from Operating Activities" , hue="Company", marker="o")
plt.title("Cash Flow from Operating Activities over the years for each company")
plt.grid()
plt.tight_layout()
plt.show()


# In[13]:


#Average Revenue over the last 3 years for each Company
print(df.groupby("Company")["Total Revenue"].mean())


# In[14]:


#Total sum of Revenue for each Company
print(df.groupby("Company")["Total Revenue"].sum())


# In[15]:


#Maximum Net Income Growth %
max_net_income_growth = df.loc[df['Net Income Growth %'].idxmax()]
print(max_net_income_growth)


# ## Summary:
# 
# ### Revenue Trends
# - **Microsoft** showed consistent revenue growth from 2022 to 2024, with a sharp increase in 2024.
# - **Apple** had steady revenue, with slight year-over-year growth.
# - **Tesla** showed slower revenue growth in recent years.
# 
# ### Net Income Insights
# - **Apple** consistently led in net income but showed a slight dip in growth percentage from 2023 to 2024.
# - **Tesla** experienced a drop in net income growth in 2024, despite growing in 2022 and 2023.
# - **Microsoft** maintained stable income with a strong rise in 2024.
# 
# ### Assets and Liabilities
# - **Microsoft's** total assets increased significantly over 3 years, while liabilities were also growing.
# - **Tesla** had steadily increasing assets and liabilities, showing expansion.
# - **Apple** kept assets stable, but its liabilities jumped in 2024.
# 
# ### Cash Flow
# - Microsoft leads in operating cash flow, with a strong upward trend.
# - Apple saw significant growth in cash flow in 2024.
# - Tesla's cash flow remained relatively flat.
# 
# ---
# 
# ## Key Takeaways
# 
# - Microsoft had the **strongest overall financial growth**, particularly in operating cash flow and revenue.
# - Tesla is in a **growth phase**, with increasing assets and moderate income.
# - Apple is **financially stable**, showing leadership in income but needs to monitor liabilities.
# 
