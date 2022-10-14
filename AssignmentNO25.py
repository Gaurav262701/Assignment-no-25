#!/usr/bin/env python
# coding: utf-8

# # Assignment 25 Solutions

# 1.Create a function that takes three integer arguments (a, b, c) and returns the amount of integers which are of equal value.
# Examples:

# In[1]:


def equal(a,b,c):
    if a==b==c:
        print(f'{a,b,c}-->{3}')
    elif a==b or b==c:
        print(f'{a,b,c}-->{2}')
    else:
        print(f'{a,b,c}-->{0}')
        
equal(3,4,3)
equal(1,1,1)
equal(3,4,1)


# 2..Write a function that converts a dictionary into a list of keys-values tuples.

# In[3]:


def dict_to_list(in_dict):
    out_list = []
    for keys,values in in_dict.items():
        out_list.append((keys,values))
    print(f'{in_dict}-->{out_list}')
    
dict_to_list({"D":1,"B":2,"c":3})
dict_to_list({"likes":2,"dislikes":3,"followers":10})


# 3.Write a function that creates a dictionary with each (key, value) pair being the (lower case, upper case) versions of a letter, respectively.

# In[4]:


def mapping(in_list):
    out_dict={}
    for i in in_list:
        out_dict[i] = i.upper()
    print(f'{in_list}-->{out_dict}')

mapping(["p","s"])
mapping(["a","b","c"])
mapping(["a","v","y","z"])


# 4.Write a function, that replaces all vowels in a string with a specified vowel.

# In[5]:


def vow_replace(in_string,vow_char):
    vowels = ['a','e','i','o','u']
    out_string =''
    for i in in_string:
        if i in vowels:
            out_string += vow_char
        else:
            out_string += i
    print(f'{in_string}--> {out_string}')
    
vow_replace("apple and bananas","u")
vow_replace("cheese caserol","o")
vow_replace("stuffed jalapeno poppers","e")


# 5.Create a function that takes a string as input and capitalizes a letter if its ASCII code is even and returns its lower case version if its ASCII code is odd.

# In[7]:


def ascii_cap(in_string):
    out_string= ''
    for i in in_string.lower():
        if(ord(i)%2==0):
            out_string += i.upper()
        else:
            out_string += i
    print(f'{in_string}-->{out_string}')

ascii_cap("to be or not to be!")
ascii_cap("THE LITTLE MERMAID")
ascii_cap("Oh what a beautiful morning")


# In[ ]:




