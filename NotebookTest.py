
# coding: utf-8

# ### the notebook

# In[4]:


import pandas as pd
import numpy as np
from pandas import Series, DataFrame


# In[16]:


data_path = "d:/Server.xlsx"
data = pd.read_excel(data_path)
print(data)

