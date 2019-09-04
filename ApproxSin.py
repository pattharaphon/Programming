#!/usr/bin/env python
# coding: utf-8

# In[6]:


import math
X = float(input())
X = math.radians(x%360)
S = F = X
K = 1
while f != 0:
    F *= (-1)*X**2/((2*K)*(2*K+1))
    S += F
    K += 1
print(S)


# In[ ]:





# In[ ]:




