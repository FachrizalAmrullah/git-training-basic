#!/usr/bin/env python
# coding: utf-8

# ## Project Euler 36

# 
# The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.
# 
# Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.
# 
# (Please note that the palindromic number, in either base, may not include leading zeros.)
# 

# In[2]:


#inisiasi nilai awal jumlahan bilangan double base palindromes
j=0

#Looping range bilangan 1-1.000.000
for i in range (1,1000000):
    #Mencari bilangan palindrome
    if str(i) == str(i)[::-1]:
        #Kalau sudah dapat, akan diubah menjadi bilangan basis 2
        a=(str(bin(i)))[2:]
        #Diuji bilangan basis 2 tersebut Palindrome atau bukan
        if a==a[::-1]:
            #Jika iya, maka bilangan i akan dijumlahkan dan terus berulang
            j=j+i
print ("jumlahan Bilangan Double-Base Palindromes dari 1 sampai 1.000.000 adalah ", j)

