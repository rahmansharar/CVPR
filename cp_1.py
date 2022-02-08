#!/usr/bin/env python
# coding: utf-8

# In[14]:


import matplotlib.pyplot as plt
import numpy as np
import random
import math
from IPython import display

import pandas as pd

df = pd.read_csv('F:\AIUB\11th sem\Computer Vision & Pattern Recognition\cp_1.csv')
df.head()

X1 = df["X"].values.tolist()
X2 = df["Y"].values.tolist()
Y = df["LABEL"].values.tolist()

for i in range(len(Y)):
    if Y[i] == 0:
        plt.plot(X1[i], X2[i], "ro")
    else:
        plt.plot(X1[i], X2[i], "go")


# In[ ]:





# In[ ]:




