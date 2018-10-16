#!/usr/bin/env python
# coding: utf-8

# ## Homework 7: Using CensusReporter to Make Geographic Selections
# Hathaway Zhang <br>
# 104369396 <br>
# Oct.11, 2018

# In[1]:


import pandas as pd
import pandas
import requests
import json
import urllib 
from urllib.request import Request, urlopen


# In[2]:


# loaded csv data into a dataframe
dfRaw = pd.read_csv("msas.csv")
dfRaw.head()


# In[3]:


geoid = "31000US" + dfRaw["CBSA"].astype(str)
half = geoid[:len(geoid)//2]
rest = geoid[len(geoid)//2:]
# join list together in a way that the api accepts
half = ','.join(half)
rest = ','.join(rest)


# ### QUESTION 1
# What city has the highest count of the audience you chose for parameter #1?

# In[4]:


# Parameter 1: what average HH income should we choose?
# make a python list of all the table ids you want to download
tableidsQ1 = ['B19001']
# join list together in a way that the api accepts
tableidstringQ1 = ','.join(tableidsQ1)


# In[5]:


# iterate over each of your metro areas and get the right data for each metro
requesturl = 'http://api.censusreporter.org/1.0/data/show/latest?table_ids=%s&geo_ids=%s' % (tableidstringQ1, half)
loadedjson = requests.get(requesturl)
parsedjsonQ11 = json.loads(loadedjson.text)
requesturl = 'http://api.censusreporter.org/1.0/data/show/latest?table_ids=%s&geo_ids=%s' % (tableidstringQ1, rest)
loadedjson = requests.get(requesturl)
parsedjsonQ12 = json.loads(loadedjson.text)


# #### What average HH income should we choose?
# According to http://academic.mintel.com.colorado.idm.oclc.org/display/907340/ <br>
# We could pick columns $50k to S74.9k: 'B19001011' and 'B19001012'

# In[6]:


dfHH = pd.DataFrame(columns=['country', 'population'], index=list(range(1,len(geoid))))


# In[7]:


for i in list(range(1,len(geoid)//2)):
    dfHH['country'][i]=[geoid[i]]
    dfHH['population'][i] = parsedjsonQ11['data'][geoid[i]]['B19001']['estimate']['B19001011'] + parsedjsonQ11['data'][geoid[i]]['B19001']['estimate']['B19001012']


# In[8]:


for i in list(range(192,len(geoid))):
    dfHH['country'][i]=[geoid[i]]
    dfHH['population'][i] = parsedjsonQ12['data'][geoid[i]]['B19001']['estimate']['B19001011'] + parsedjsonQ12['data'][geoid[i]]['B19001']['estimate']['B19001012']


# In[41]:


print(dfHH.loc[dfHH['population'] == max(dfHH['population'])])


# In[42]:


print(dfRaw.loc[dfRaw['CBSA'] == 35620])


# According to the calculation above, New York-Newark-Jersey City has the highest count of average house hold income that ranged between $50K to $70K, which is 1.03819e+06. 

# ### QUESTION 2
# What city has the highest count of the audience you chose for parameter #2?

# In[11]:


# Parameter 2: what age range should we target?
tableidsQ2 = ['B01001']
# join list together in a way that the api accepts
tableidstringQ2 = ','.join(tableidsQ2)


# In[12]:


# iterate over each of your metro areas and get the right data for each metro
requesturl = 'http://api.censusreporter.org/1.0/data/show/latest?table_ids=%s&geo_ids=%s' % (tableidstringQ2, half)
loadedjson = requests.get(requesturl)
parsedjsonQ21 = json.loads(loadedjson.text)
requesturl = 'http://api.censusreporter.org/1.0/data/show/latest?table_ids=%s&geo_ids=%s' % (tableidstringQ2, rest)
loadedjson = requests.get(requesturl)
parsedjsonQ22 = json.loads(loadedjson.text)


# #### What age range should we target?
# According to http://academic.mintel.com.colorado.idm.oclc.org/display/907340/ <br>
# We could age range 18-34: 'B01001003','B01001004','B01001005','B01001006','B01001007','B01001008','B01001009','B01001010','B01001011', and 'B01001012' 

# In[13]:


age_range = ['B01001003','B01001004','B01001005','B01001006','B01001007','B01001008','B01001009','B01001010','B01001011','B01001012']


# In[14]:


dfA = pd.DataFrame(columns=['location', 'population'], index=list(range(1,len(geoid))))


# In[15]:


for i in list(range(1,len(geoid)//2)):
    dfA['location'][i]=[geoid[i]]
    dfA['population'][i] = parsedjsonQ21['data'][geoid[i]]['B01001']['estimate'][age_range[0]] + parsedjsonQ21['data'][geoid[i]]['B01001']['estimate'][age_range[1]] + parsedjsonQ21['data'][geoid[i]]['B01001']['estimate'][age_range[2]] + parsedjsonQ21['data'][geoid[i]]['B01001']['estimate'][age_range[3]] + parsedjsonQ21['data'][geoid[i]]['B01001']['estimate'][age_range[4]] + parsedjsonQ21['data'][geoid[i]]['B01001']['estimate'][age_range[5]] + parsedjsonQ21['data'][geoid[i]]['B01001']['estimate'][age_range[6]] + parsedjsonQ21['data'][geoid[i]]['B01001']['estimate'][age_range[7]] + parsedjsonQ21['data'][geoid[i]]['B01001']['estimate'][age_range[8]] + parsedjsonQ21['data'][geoid[i]]['B01001']['estimate'][age_range[9]]  
    
for i in list(range(192,len(geoid))):
    dfA['location'][i]=[geoid[i]]
    dfA['population'][i] = parsedjsonQ22['data'][geoid[i]]['B01001']['estimate'][age_range[0]] + parsedjsonQ22['data'][geoid[i]]['B01001']['estimate'][age_range[1]] + parsedjsonQ22['data'][geoid[i]]['B01001']['estimate'][age_range[2]] + parsedjsonQ22['data'][geoid[i]]['B01001']['estimate'][age_range[3]] + parsedjsonQ22['data'][geoid[i]]['B01001']['estimate'][age_range[4]] + parsedjsonQ22['data'][geoid[i]]['B01001']['estimate'][age_range[5]] + parsedjsonQ22['data'][geoid[i]]['B01001']['estimate'][age_range[6]] + parsedjsonQ22['data'][geoid[i]]['B01001']['estimate'][age_range[7]] + parsedjsonQ22['data'][geoid[i]]['B01001']['estimate'][age_range[8]] + parsedjsonQ22['data'][geoid[i]]['B01001']['estimate'][age_range[9]]   


# In[39]:


print(dfA.loc[dfA['population'] == max(dfA['population'])])


# In[40]:


print(dfRaw.loc[dfRaw['CBSA'] == 35620])


# According to the calculation above, New York-Newark-Jersey City has the highest count of age range 18-34, which is 4.63682e+06. 

# ### QUESTION 3
# What city has the highest count of the audience you chose for parameter #3?

# In[18]:


# Parameter 3: areas with large Hispanic populations
tableidsQ3 = ['B03003']
# join list together in a way that the api accepts
tableidstringQ3 = ','.join(tableidsQ3)


# In[19]:


# iterate over each of your metro areas and get the right data for each metro
requesturl = 'http://api.censusreporter.org/1.0/data/show/latest?table_ids=%s&geo_ids=%s' % (tableidstringQ3, half)
loadedjson = requests.get(requesturl)
parsedjsonQ31 = json.loads(loadedjson.text)
requesturl = 'http://api.censusreporter.org/1.0/data/show/latest?table_ids=%s&geo_ids=%s' % (tableidstringQ3, rest)
loadedjson = requests.get(requesturl)
parsedjsonQ32 = json.loads(loadedjson.text)


# #### What age range should we target?
# According to http://academic.mintel.com.colorado.idm.oclc.org/display/907340/ <br>
# The Hispanic code would be B03003003.

# In[20]:


dfH = pd.DataFrame(columns=['location', 'population'], index=list(range(1,len(geoid))))


# In[21]:


for i in list(range(1,len(geoid)//2)):
    dfH['location'][i]=[geoid[i]]
    dfH['population'][i] = parsedjsonQ31['data'][geoid[i]]['B03003']['estimate']['B03003003'] 
for i in list(range(192,len(geoid))):
    dfH['location'][i]=[geoid[i]]
    dfH['population'][i] = parsedjsonQ32['data'][geoid[i]]['B03003']['estimate']['B03003003'] 


# In[38]:


print(dfH.loc[dfH['population'] == max(dfH['population'])])


# In[37]:


print(dfRaw.loc[dfRaw['CBSA'] == 31080])


# According to the calculation above, Los Angeles-Long Beach-Anaheim, CA has the highest count of hispanic, which is 	6.03149e+06. 

# ### QUESTION 4
# What city has the highest mean percentage across all three categories?

# In[25]:


HH_Income_Percentage = []
Pop_by_age_Percentage = []
Pop_by_Hispanic_Percentage = []
for i, row in dfHH.iterrows():
    Percentage_Income = dfHH['population'][i]/max(dfHH['population'])
    Percentage_Age = dfA['population'][i]/max(dfA['population'])
    Percentage_Hispanic = dfH['population'][i]/max(dfH['population'])
    HH_Income_Percentage.append(Percentage_Income)
    Pop_by_age_Percentage.append(Percentage_Age)
    Pop_by_Hispanic_Percentage.append(Percentage_Hispanic)


# In[26]:


dfHH['percentage'] = HH_Income_Percentage
dfA['percentage'] = Pop_by_age_Percentage
dfH['percentage'] = Pop_by_Hispanic_Percentage


# In[32]:


Pmean = []
for i, row in dfHH.iterrows():
    Mean = (dfHH['percentage'][i] + dfA['percentage'][i]+ dfH['percentage'][i])/3
    Pmean.append(Mean)
dfHH['percentage mean'] = Pmean


# In[35]:


print(dfHH.loc[dfHH['percentage mean'] == max(dfHH['percentage mean'])])


# In[36]:


print(dfRaw.loc[dfRaw['CBSA'] == 35620])


# New York-Newark-Jersey City, NY-NJ-PA has the highest mean percentage across all three categories, which is 0.942684
