#!/usr/bin/env python
# coding: utf-8

# In[1]:


a=input('enter an integer:')
b=int(a)+100
print(a,b)


# In[7]:


import math
a=math.fabs(-123.45)
print(a)

b=math.ceil(8.8)
print(b)

c=math.floor(8.8)
print(c)

d=math.exp(1)
print(d)

e=math.log(100)
print(e)

f=math.log(100,10)
print(f)

g=math.sqrt(1000000)
print(g)


# In[9]:


str1='hello,'+    'python,let\slearning'
str2="python now"
str3=str1+str2
print(str3)


# In[10]:


print(format('department','12s'))
print(format('of','12s'))
print(format('computer','12s'))
print(format('science','12s'))
print()


# In[11]:


print(format('department','>12s'))
print(format('of','>12s'))
print(format('computer','>12s'))
print(format('science','>12s'))


# In[12]:


print(format('department','>12s'))
print(format('of','>12s'))
print(format('computer','>12s'))
print(format('science','>12s'))


# In[13]:


print('i=%d'%(100))
print('i=%d,j=%d'%(100,200))


# In[14]:


a=100
b=200
c,d=a,b
print(c,d)
print(c)
print(d)
print()


# In[15]:


a=100
b=200
c,d=a,b
print(c,d)
print(c,end='')
print(d,end='***')
print('over')


# In[16]:


a=100
b=200
c,d=a,b
print(c,d)
print(c,end='$')
print('and')
print(d,end='***')
print('over')


# In[17]:


x=100
y=3
print(x*y)
print(x/y)
print(x//y)
print(x%y)
print(x**y)
print(x**0.5)


# In[18]:


str1='hello,'
str2="python"
str3=str1+str2
print(str3)
a=100
b=200
c=a+b
print(c)


# In[19]:


a=100
b=3
a//=b
print(a)

a=100
a%=b
print(a)

a=100
a/=b
print(a)


# In[20]:


a=100
b=200
print(a,b)

b,a=a,b
print(a,b)


# In[21]:


a=100
b=200
print(a,b)

temp=a


# In[22]:


a=b
b=temp
print(a,b)


# In[ ]:




