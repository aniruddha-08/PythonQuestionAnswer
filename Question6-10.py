# Question6-10.py

# 6. Write a Python program to get a list, sorted in increasing order by the last element
# in each tuple from a given list of non-empty tuples.
# 	Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
# 	Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]
# def sort_by_last_element(tuples_list):
#     return sorted(tuples_list, key=lambda x: x[-1])
# # Sample List
# sample_list = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
# # Sorting the list
# sorted_list = sort_by_last_element(sample_list)
# # Printing the result
# print("Expected Result=",sorted_list)

#print("-------------------------------------------------------------------------------------------------")
# 7. Write a Python program to remove duplicates from a list.
#Approche-1
# a=input("Enter value separated by comma(,):").split(",")
# lst=[]
# for i in a:
#     if i not in lst:
#         lst.append(i)
# print(lst)
#Approche-2
# a=[1,2,4,5,7,2,1,5,6,7,10]
# print(a,type(a))
# b=set(a)
# print(b,type(b))
# c=list(b)
# print(c,type(c))
#Apporach-3
# def remove_duplicates(lst):
#     seen = set()
#     return [x for x in lst if not (x in seen or seen.add(x))]
# # Sample List
# sample_list = [1, 2, 3, 4, 2, 3, 5, 6, 1]
# # Removing duplicates
# unique_list = remove_duplicates(sample_list)
# # Printing the result
# print(unique_list)

#print("-------------------------------------------------------------------------------------------------")
# 8. Write a Python program to check a list is empty or not.
#Approach-1
# value=[]
# if value:
#     print("Not Empty")
# else:
#     print("Empty")
#Approach-2
# class demo:
#     def check(self,value):
#          if not value:
#             print("List is Empty")
#          else:
#             print("List is not Empty")
# d1=demo()
# d1.check([])
# d2=demo()
# d2.check([1,2,3])
# Approach-3
# class demo:
#     def check(self,value):
#          if len(value)==0:
#             print("List is Empty")
#          else:
#             print("List is not Empty")
# d1=demo()
# d1.check([1,2,3])
# d2=demo()
# d2.check([])

#print("-------------------------------------------------------------------------------------------------")
# 9. Write a Python program to clone or copy a list.
# Approach-1
# lst1=[10,20,30,40,50]
# print("Original list=",lst1,type(lst1),id(lst1))
# lst2=lst1.copy() #shallow copy
# print("Copy List=",lst2,type(lst2),id(lst2))

# Approach-2
# lst1=[10,20,30,40,50]
# print("Original list=",lst1,type(lst1),id(lst1))
# lst2=lst1 #Deep Copy
# print("Copy List=",lst2,type(lst2),id(lst2))

# Approach-3
# lst1=[10,20,30,40,50]
# print("Original list=",lst1,type(lst1),id(lst1))
# lst2=lst1[:] #Slicing
# print("Copy List=",lst2,type(lst2),id(lst2))

# Approach-4
# lst1=[10,20,30,40,50]
# print("Original list=",lst1,type(lst1),id(lst1))
# lst2=list(lst1) #using list
# print("Copy List=",lst2,type(lst2),id(lst2))

# 10. Write a Python program to find the list of words that are longer than n from a given list of words.
# def sample(word_list,n):
#     result=[word for word in word_list if len(word)>n]
#     return result
# a=["python","is","an","oop","language"]
# n=2
# long_word=sample(a,n)
# print("The Word Longer than",n,":",long_word)
