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














