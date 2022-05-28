#!/usr/bin/env python
# coding: utf-8

# In[53]:


user_input=str(input("Enter a Phrase:"))
#user_input="Machine Learning"
inputlist= user_input.split()
fl=""
for i in inputlist:
    fl=fl+str(i[0])
    
print("Acronym of ",user_input, " is: ", fl)


# In[ ]:




