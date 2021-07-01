#!/usr/bin/env python
# coding: utf-8

# In[ ]:


"""
coronavirus
3
abcde
crnas
onarous

"""
# Iterative Python program to check if a
# string is a subsequence of another string

# Returns true if str1 is a subsequence of str2

def main(str1, str2):
    m = len(str1)
    n = len(str2)

    j = 0 # Index of str1
    i = 0 # Index of str2

    # Traverse both str1 and str2
    # Compare the current character of str2 with
    # first unmatched character of str1
    # If matched, then move ahead in str1

    while j < m and i < n:
        if str1[j] == str2[i]:
            j = j+1
        i = i + 1

    # If all characters of str1 matched,
    # then j is equal to m
    return j == m

# Driver Program
str2 = str(input())
N = int(input())

for i in range(N):
    str1 = str(input())
    if main(str1, str2):
        print("POSITIVE") 
    else:
        print( "NEGATIVE")

