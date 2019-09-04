#!/usr/bin/env python
# coding: utf-8

# In[1]:


nums = [8,10]
utmost = int(input("number: "))
fruit = 0
for i in range(0,utmost):
    if i %8 == 0 or i%10 == 0:
        fruit += i
print(fruit)


# In[ ]:




