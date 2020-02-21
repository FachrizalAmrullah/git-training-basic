#!/usr/bin/env python
# coding: utf-8

# ## Project Euler 31

# 
# In the United Kingdom the currency is made up of pound (£) and pence (p). There are eight coins in general circulation:
# 
#     1p, 2p, 5p, 10p, 20p, 50p, £1 (100p), and £2 (200p).
# 
# It is possible to make £2 in the following way:
# 
#     1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
# 
# How many different ways can £2 be made using any number of coins?
# 

# ### 100a + 50b + 20c + 10d + 5e + 2f + g = 200
# 
# ##### Mencari Kombinasi (a,b,c,d,e,f,g) yang mungkin

# In[2]:


#counter for couting number of possibilities
counter = 0

# number of 100p coins
for a in range(0,3):
    if 100*a==200:
        counter=counter+1
        # print (a,"0 0 0 0 0 0")
    else:
        # number of 50p coins
        for b in range(0, int(1+(200-100*a)/50)):
            if 100*a+50*b==200:
                counter=counter+1
                # print (a,b,"0 0 0 0 0")
            else:
                # number of 20p coins
                for c in range(0, int(1+(200-100*a-50*b)/20)):
                    if 100*a+50*b+20*c==200:
                        counter=counter+1
                        # print (a,b,c,"0 0 0 0")
                    else:
                        # number of 10p coins
                        for d in range(0, int(1+(200-100*a-50*b-20*c)/10)):
                            if 100*a+50*b+20*c+10*d==200:
                                counter=counter+1
                                # print (a,b,c,d,"0 0 0")
                            else:
                                # number of 5p coins
                                for e in range(0, int(1+(200-100*a-50*b-20*c-10*d)/5)):
                                    if 100*a+50*b+20*c+10*d+5*e==200:
                                        counter=counter+1
                                        # print (a,b,c,d,e,"0 0")
                                    else:
                                        # number of 2p coins
                                        for f in range(0, int(1+(200-100*a-50*b-20*c-10*d-5*e)/2)):
                                            if 100*a+50*b+20*c+10*d+5*e+2*f==200:
                                                counter=counter+1
                                                # print (a,b,c,d,e,f,"0")
                                            else:
                                                # number of p coins
                                                for g in range(0, int(1+(200-100*a-50*b-20*c-10*d-5*e-2*f))):
                                                    if 100*a+50*b+20*c+10*d+5*e+2*f+g==200:
                                                        counter=counter+1
                                                        # print (a,b,c,d,e,f,g)
# Total number of ways we can form the 200p
print("Total number of ways we can form the 200p")
# Added 1 for 200p case
print (counter+1)

