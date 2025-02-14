# # Question11-15.py
# 11. Write a Python function that takes two lists and returns True if they have at least one common member.
#
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
# print("Set1=",set1)
# print("Set2=",set2)
# if set1.intersection(set2):
#     print(True)
# else:
#     print(False)


#print("-------------------------------------------------------------------------------------------------")
# 12. Write a Python program to print a specified list after removing the 0th, 4th and 5th elements.
# 		Sample List : ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
# 		Expected Output : ['Green', 'White', 'Black']
#
# Approach-1
# sam=['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
# del sam[-2:]
# sam.pop(0)
# print(sam)
#Approach-2
# sam = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
# sam=[sam[i] for i in range(len(sam)) if i not in[0,4,5]]
# print(sam)

#print("-------------------------------------------------------------------------------------------------")
# 13. Write a Python program to generate a 3*4*6 3D array whose each element is *.

# import numpy as np
# a=np.full((3,4,6),"*")
# print(a)

#print("-------------------------------------------------------------------------------------------------")
# 14. Write a Python program to print the numbers of a specified list after removing even numbers from it.
#Approach-1
# n=[1,2,3,4,5,6,7,8,9,10]
# lst=[]
# for i in n:
#     if i%2==1:
#         lst.append(i)
# else:
#     print(lst)

#Approach-2
# n=[1,2,3,4,5,6,7,8,9,10]
# lst=[i for i in n if i%2==1]
# print(lst)

#print("-------------------------------------------------------------------------------------------------")
# 15. Write a Python program to shuffle and print a specified list
# import numpy as np
# lst=[1,2,3,4,5,6,7,8,9,10]
# np.random.shuffle(lst)
# print("Shuffle_List=",lst)
















