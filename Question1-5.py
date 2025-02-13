# Question1-5.py
# 1. Write a Python program to sum all the items in a list.
# a=[10,20,30,40,50]
# sum=0
# for i in a:
#     sum=sum+i
# print("Sum={}".format(sum))
from itertools import count

#print("-------------------------------------------------------------------------------------------------")
# 2. Write a Python program to multiply all the items in a list.
# a=[1,2,3,4,5]
# mul=1
# for i in a:
#     mul=mul*i
# print("Multipy all the item in list={}".format(mul))

#print("-------------------------------------------------------------------------------------------------")
# 3. Write a Python program to get the largest number from a list.
#Approach-1
#a=[10,-1,0,-90,34,-86]
#a.sort(reverse=False)
#print(a[-1])
#Approach-2
# a=[10,-1,0,-90,34,-86]
# print(max(a))

#print("-------------------------------------------------------------------------------------------------")
# 4. Write a Python program to get the smallest number from a list.
#Approach-1
# a=[10,-1,0,-90,34,-86,78]
# a.sort(reverse=True)
# print(a[-1])
#Approach-1
# a=[10,-1,0,-9,34,-86,78]
# print(min(a))

#print("-------------------------------------------------------------------------------------------------")
# 5. Write a Python program to count the number of strings where the string length
# is 2 or more and the first and last character are same from a given list of strings.
# 		Sample List : ['abc', 'xyz', 'aba', '1221']
# 		Expected Result : 2
#Apporach-1
# def sample(strings):
#     count = 0
#     for s in strings:
#         if len(s) >= 2 and s[0] == s[-1]:
#             count += 1
#     return count
# # Sample List
# sample_list = ['abc', 'xyz', 'aba', '1221','madam','78787',]
# # Calling the function and printing the result
# print("Expected Result:", sample(sample_list))
#Apporach-2
# def sample(string):
#     return sum(1 for s in string if len(s) >=2 and s[0]==s[-1])
# sample_list=['abc', 'xyz', 'aba', '1221','madam','78787',]
# print("Expected Result:", sample(sample_list))