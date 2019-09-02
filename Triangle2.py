#!/usr/bin/env python
# coding: utf-8

# In[1]:


import math
A=float(input("A FACET LENGTH : "))
B=float(input("B FACET LENGTH :"))
D=float(input("ANGLE C :"))

C=D*math.pi/180

c=math.sqrt((A**2)+(B**2)-(2*A*B*math.cos(C)))
print("c = ",c, "cm.")


# In[ ]:




