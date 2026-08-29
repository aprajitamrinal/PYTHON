#print("helloww!")
#strings
'''
mystring = "hello"
print(mystring)
'''
#for new line we musst use \n
'''
str1 = "what are you doing,\nbruh"

print(str1)
'''

#same for tab we can use \t
'''
str2 = "what are you doing,\tbruh"
print(str2)
'''

#basic operations (1.concatination)
'''
str1 = "hello"
str2 = "world"
str3 = str1 + str2
print(str3)
'''
# (2. length of str)
'''
str1 = "hello"
print(len(str1))

str2 = "world"
len1 = len(str2)
print(len1)
'''
#(3.INDEXING)
'''
s1 = 'hi lol'
print(s1[0])
print(s1[1])
print(s1[2])
''' 
#(4. slicing) accessing a range of characters in a string
"""
str = "Apnaclass"
print(str[0:3]) #output Apn
print(str[3:]) #output aclass
print(str[:5]) #output Apnac
"""
#negative indexing
'''
str = "Apnaclass"
print(str[-1:len(str)]) #output s
print(str[-3:-1]) #output as
'''
#string functions
'''
str.endswith() #check if the string ends with a specific character
str.capitalze() #capitalize the first character of the string
str.lower() #convert the string to lowercase
str.upper() #convert the string to uppercase
str.replace() #replace a specific character in the string with another character
str.find() #find the index of a specific character in the string
str.count() #count the number of occurrences of a specific character in the string
str.split() #split the string into a list of substrings based on a specific character
'''
"""
example of string functions
str = 'HELLO WORLD'
print(str.endswith('D')) #output True
print(str.capitalize()) #output Hello world
print(str.lower()) #output hello world
print(str.upper()) #output HELLO WORLD
print(str.replace('H', 'i')) #output iELLO WORLD
print(str.find('W')) #output 6
print(str.count('L')) #output 3
print(str.split(' ')) #output ['HELLO', 'WORLD']
"""
# Q. WAP TO INPUT USER'S FIRST NAME & PRINT IT'S LENGTH
'''
str = "aman"
print(len(str)) #output 4
'''

# WAP TO FIND THE OCCURANCE OF 'S' IN A STRING
'''
str = "hi is this phone is of samsung company"
print(str.count('s')) #output 5
'''
# 5. conditional statements ( SYNTAX IF, ELIF, ELSE)
'''
if condition:
    #code to be executed if condition is true
elif condition:
    #code to be executed if condition is true
else:
    #code to be executed if condition is false
'''
# example of conditional statements
"""
age = int(input("enter your age:"))
if age>=18:
    print("you are eligible to vote")
elif age>=19:
    print("you are also eligible to vote")
else:
    print("you are not eligible to vote")
"""
# grades students based on marks
'''
mark = int(input("enter marks out of 100:"))
if mark >=90:
    print("A'")
elif mark >=80:
    print("B")
else:
    print("C")
'''
# nesting of if else statements
'''
age = int(input("enter your age:"))
if age>=18:
    if age>=80:
        print("can't drive")
    else:
        print("can drive")
else:
    print("can't drive")
'''
#WAP TO CHECK WHETHER A NUMBER IS EVEN OR ODD
"""
a = int(input("enter a number:"))
if a%2==0:
 print("even")
else :
    print("odd")
"""
# WAP TO FIND GREATEST OF 3 NUMBERS ENTERED BY USER
"""
a = int(input("enter first number:"))
b = int(input("enter second number:"))
c = int(input("enter third number:"))
if a>b and a>c:
    print("a is greatest")
elif b>a and b>c:
    print("b is greatest")
else:
    print("c is greatest")
"""
# WAP TO CHECK IF A NUMBER IS A MULTIPLE OF 7 OR NOT
a=int(input("enter a number:"))
if a%7==0:
    print("multiple of 7")
else:
    print("not a multiple of 7")
#LISTS AND TUPLES
"""
 marks =[90,80,70,66,50]
 print(marks[0]) #output 90
 print(marks[1]) #output 80
 print(type(marks)) #output <class 'list'>
 print(len(marks)) #output 5
 """
#strings are immutable but lists are mutable
'''
str = 'HELLO'
print(str[0]) #output H
str[0] = 'h' #output error

student = ["karan" , 74.5 ,15 , "male"]
student[0] = "aman"
print(student) #output ['aman', 74.5, 15, 'male']
'''
#list slicing 
'''
marks =[84,64,74,90,50]
marks[1:4] #output [64, 74, 90]
marks[2:] #output [74, 90, 50]
marks[:3] #output [84, 64, 74]
marks[-3:-1] #output [74, 90]
'''
#list methods
'''
list = [1,2,3,4,5]
list.append(6) #add 6 to the end of the list
list.sort() #sorts in ascending order [1,2,3,4,5,6]
list.sort(reverse=True) #sorts in descending order [6,5,4,3,2,1]
list.reverse() #reverses the list [5,4,3,2,1]
list.insert(2, 10) #inserts 10 at index 2 [1,2,10,3,4,5]
list.remove(3) #removes 3 from the list [1,2,10,4,5]
list.pop(idx) #removes the element at index 2 from the list [1,2,4,5]
list.pop(2) #removes the element at index 2 from the list [1,2,4,5]

list = [2,1,3]
print(list.append(4)) #output None
print(list) #output [2, 1, 3, 4]
print(list.sort()) #output None
print(list) #output [1, 2, 3, 4]
print(list.sort(reverse=True)) #output None
print(list) #output [4, 3, 2, 1]

list = ["banana", "apple", "cherry"]
list.sort() #sorts in ascending order ['apple', 'banana', 'cherry']
list.sort(reverse=True) #sorts in descending order ['cherry', 'banana', 'apple']
'''
#TUPLES
#tuples are immutable
'''
tup = (1,2,3,4,5)
print(tup[0]) #output 1
print(tup)
print(type(tup)) #output <class 'tuple'>
a = (1)
print(type(a)) #output <class 'int'>
b = (1,)
print(type(b)) #output <class 'tuple'>
'''
#TUPLE METHODS
'''
tup = (2,1,3)
tup.index(element) #returns the index of the first occurrence of the element
tup.index(2) #output 0
tup.count(element) #returns the number of occurrences of the element
tup.count(2) #output 1
'''
#WAP TO ASK THE USER TO ENTER NAMES OF THEIR 3 FAVORITE MOVIES N STORE THEM IN A LIST
'''
movies = []
mov1 = input("enter 1st movie:")
mov2 = input ("enter 2nd movie:")
mov3 = input("enter 3rd movie:")
movies.append(mov1)
movies.append(mov2)
movies.append(mov3)
print(movies) #output ['movie1', 'movie2', 'movie3']
'''
#WAP TO CHECK IF A LIST CONTAINS A PALINDROME OF ELEMENTS.
'''
list1 = [1,2,3]
list2 = [1,2,1]
list3 = list1.copy()
list3.reverse()
if(list3 == list1):
    print("list is a palindrome")
else:
    print("list is not a palindrome") #output list is not a palindrome
'''

#WAP TO COUNT THE NUMBER OF STUDENTS WITH THE "A" GRADE IN THE FOLLOWING TUPLE
'''
grades = ("A" , "B" , "C" , "A" , "B" , "A")
print(grades.count("A")) #output 3
# STORE THE ABOVE VALUES IN A LIST & STORE THEM FROM "A" T "C"
gradesinlist = list(grades)
gradesinlist.sort()
print(gradesinlist) #output ['A', 'A', 'A', 'B', 'B', 'C']
'''

#DICTIONARIES
#dictionaries are mutable "key": value 
info = { 
    "key" : "value" , 
    "name" : "mahi",
    "age" : 20 , 
    "subjects" : ["maths" , "science" , "english"] , 
    "topics" : ("algebra" , "geometry" , "trigonometry") ,
    12.99 : 94.45 

}
info["name"] = "aprajita" #updating the value of the key "name" 
info["surname"] = "sharma" #adding a new key-value pair to the dictionary   
print(info) #output {'key': 'value', 'name': 'aprajita', 'age': 20, 'subjects': ['maths', 'science', 'english'], 'topics': ('algebra', 'geometry', 'trigonometry'), 12.99: 94.45, 'surname': 'sharma'}  

print(info) #not updated value of the key "name"
print(type(info)) #output <class 'dict'>
print(info["name"]) #output mahi (not updated value of the key "name")
print(info["surname"]) #output sharma
print(info["age"]) #output 20

null_dict = {} #empty dictionary




 











