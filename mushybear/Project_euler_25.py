#!/usr/bin/env python
# coding: utf-8

# ## Project Euler 25

# 
# The Fibonacci sequence is defined by the recurrence relation:
# 
#     Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
# 
# Hence the first 12 terms will be:
# 
#     F1 = 1
#     F2 = 1
#     F3 = 2
#     F4 = 3
#     F5 = 5
#     F6 = 8
#     F7 = 13
#     F8 = 21
#     F9 = 34
#     F10 = 55
#     F11 = 89
#     F12 = 144
# 
# The 12th term, F12, is the first term to contain three digits.
# 
# What is the index of the first term in the Fibonacci sequence to contain 1000 digits?
# 

# In[ ]:


def Fibonacci(NthTerm):
    if NthTerm == 1 or NthTerm == 2:
        return 1 # Challenge defines 1st and 2nd term as == 1
    else:  # recursive definition of Fib term
        return Fibonacci(NthTerm-1) + Fibonacci(NthTerm-2)

FirstTerm = 0 # For scope to include Term in scope of print on line 13
for Term in range(1, 1000): # Arbitrary range
    FibValue = str(Fibonacci(Term)) # Convert integer to string for len()
    if len(FibValue) == 1000:
        FirstTerm = Term
        break # Stop there
    else:
        continue # Go to next number
print ("The first term in the\nFibonacci sequence to\ncontain 1000 digits\nis the", FirstTerm, "term.")

