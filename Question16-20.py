# # Question16-20.py
# 16. Write a Python program to generate and print a
# list of first and last 5 elements where the values are square of numbers between 1 and 30 (both included).
#Approach-1
# squares=[x**2 for x in range(1,30+1)]
# First_five=squares[:5]
# Second_five=squares[-5:]
#
# print("First 5 Elements:",First_five)
# print("Last 5 Elements:",Second_five)

#Approach-2
# x=[]
# for i in range(1,30+1):
#     x.append(i**2)
# print(x)
# print("First 5 Element:{}".format(x[0:5]))
# print("Second 5 Element:{}".format(x[-5:]))

#Approach-3 This approach concatenate
# x=[]
# for i in range(1,30+1):
#     x.append(i**2)
# print(x)
# print("First 5 Element and Second 5 Element:{}".format(x[:5]+x[-5:]))

#print("-------------------------------------------------------------------------------------------------")
# 17. Write a Python program to generate and print a
# # list except for the first 5 elements, where the values are square of numbers between 1 and 30 (both included).
#Approach-1
# squares=[x**2 for x in range(1,30+1)]
# First_Five=squares[0:5]
# print("First Five Element:{}".format(First_Five))

#Approach-2
# x=[]
# for i in range(1,30+1):
#     x.append(i**2)
# print(x)
# print("First 5 Element={}".format(x[:5]))


#print("-------------------------------------------------------------------------------------------------")
# 18. Write a Python program to generate all permutations of a list in Python.
# def permute(lst,path=[]):
#     if not lst:
#         print(tuple(path))
#         return
#     for i in range(len(lst)):
#         permute(lst[:i]+lst[i+1:],path+[lst[i]])
# my_list=[1,2,3]
# permute(my_list)


# #print("-------------------------------------------------------------------------------------------------")
# 19. Write a Python program to get the difference between the two lists.
# lst1=[]
# lst2=[]
# n=int(input("Enter How Many Value u want From list1:"))
# for i in range(n):
#     val=input("Enter {} value:".format(i))
#     lst1.append(val)
# print("-"*30)
# print("\tlist1=",lst1)
# print("-"*30)
# nn=int(input("Enter How Many Value u want From list2:"))
# for j in range(nn):
#     val=input("Enter {} value:".format(j))
#     lst2.append(val)
# print("-"*30)
# print("\tlist2=",lst2)
# print("-"*30)
# set1=set(lst1)
# set2=set(lst2)
# difference=list(set1.symmetric_difference(set2))
# print("Difference={}".format(difference))


#print("-------------------------------------------------------------------------------------------------")
# 20. Write a Python program access the index of a list.
# a=[10,20,30,40,50,60,70,80,90,100]
# for key,value in enumerate(a):
#     print(key,"--->",value)

