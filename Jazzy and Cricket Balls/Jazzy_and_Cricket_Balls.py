#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import math

def primefactors(n):
    
    ans=n
    while(n%2==0):
        n=n//2
        ans+=n
    for i in range(3, int(math.sqrt(n))+2, 2):
        while(n%i==0):
            n=n//i
            ans+=n
    if n>2:
        ans+=1
    return ans

n=int(input())
l=list(map(int, input().strip().split(" ")))
op=0
for d in l:
    op+=primefactors(d)
print(op)

