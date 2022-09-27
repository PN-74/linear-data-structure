#!/usr/bin/env python
# coding: utf-8

# # Q1. Write a program to find all pairs of an integer array whose sum is equal to a given number?
# 
# 

# In[4]:


def find(array, len, summ):
    print("Pairs whose sum is : ", summ)
    for i in range(len):
        for j in range(i, len):
            if (array[i] + array[j]) == summ:
                print(array[i], array[j])


array = [5, 2, 3, 4, 1, 6, 7]
summ = 7
print("Array= ", array)
find(array, len(array), summ)


# # Q2. Write a program to reverse an array in place? In place means you cannot create a new array. You have to update the original array.

# In[22]:


#The original array
arr = [1,2,3,4,5]
print("Array is :",arr)
 
res = arr[::-1] 
print("Resultant new reversed array:",res)


# # Q3. Write a program to check if two strings are a rotation of each other?

# In[32]:


def areRotations(string1, string2):
    size1 = len(string1)
    size2 = len(string2)
    temp = ''
    if size1 != size2:
        return 0
    temp = string1 + string1
    if (temp.count(string2)> 0):
        return 1
    else:
        return 0
    
string1 = "ABCD"
string2 = "ABCD"
 
if areRotations(string1, string2):
    print("Strings are rotations of each other")
else:
    print("Strings are not rotations of each other")
     


# # Q4. Write a program to print the first non-repeated character from a string?

# In[38]:


from collections import Counter

def repeatFunc(myStr):
    freq = Counter(myStr)
    for i in myStr:
        if(freq[i] == 1):
            print(i)
            break
myStr = "uhhugfjwdkoj"

repeatFunc(myStr)


# # Q5. Read about the Tower of Hanoi algorithm. Write a program to implement it.

# In[39]:


def TowerOfHanoi(n , from_rod, to_rod, aux_rod):
   if n == 1:
      print ("Move disk 1 from rod",from_rod,"to rod",to_rod)
      return
   TowerOfHanoi(n-1, from_rod, aux_rod, to_rod)
   print ("Move disk",n,"from rod",from_rod,"to rod",to_rod)
   TowerOfHanoi(n-1, aux_rod, to_rod, from_rod)
# main
n = 3
TowerOfHanoi(n, 'A', 'C', 'B')
# A, B, C are the rod
print ("Sorted array is:")
for i in range(n):
   print (arr[i],end=" ")


# # Q6. Read about infix, prefix, and postfix expressions. Write a program to convert postfix to prefix expression.

# In[40]:


def isOperator(x):
 
    if x == "+":
        return True
 
    if x == "-":
        return True
 
    if x == "/":
        return True
 
    if x == "*":
        return True
 
    return False
 
# Convert postfix to Prefix expression
 
 
def postToPre(post_exp):
 
    s = []
    length = len(post_exp)
    for i in range(length):
        if (isOperator(post_exp[i])):
            op1 = s[-1]
            s.pop()
            op2 = s[-1]
            s.pop()
 
            # concat the operands and operator
            temp = post_exp[i] + op2 + op1
 
            # Push string temp back to stack
            s.append(temp)
 
        # if symbol is an operand
        else:
 
            # push the operand to the stack
            s.append(post_exp[i])
 
    
    ans = ""
    for i in s:
        ans += i
    return ans
 
 
# Driver Code
if __name__ == "__main__":
 
    post_exp = "AB+CD-"
     
    # Function call
    print("Prefix : ", postToPre(post_exp))


# # Q7. Write a program to convert prefix expression to infix expression.

# In[41]:


s = "*-A/BC-/AKL"
 
# Stack for storing operands
stack = []
 
operators = set(['+', '-', '*', '/', '^'])
 
# Reversing the order
s = s[::-1]
 
# iterating through individual tokens
for i in s:
 
    # if token is operator
    if i in operators:
 
        # pop 2 elements from stack
        a = stack.pop()
        b = stack.pop()
 
        # concatenate them as operand1 +
        # operand2 + operator
        temp = a+b+i
        stack.append(temp)
 
    # else if operand
    else:
        stack.append(i)
 
# printing final output
print(*stack)


# # Q8. Write a program to check if all the brackets are closed in a given code snippet.

# In[42]:


def areBracketsBalanced(expr):
    stack = []

    for char in expr:
        if char in ["(", "{", "["]:

            stack.append(char)
        else:

            if not stack:
                return False
            current_char = stack.pop()
            if current_char == '(':
                if char != ")":
                    return False
            if current_char == '{':
                if char != "}":
                    return False
            if current_char == '[':
                if char != "]":
                    return False

    if stack:
        return False
    return True

if __name__ == "__main__":
    expr = "{()}[]"

    if areBracketsBalanced(expr):
        print("Balanced")
    else:
        print("Not Balanced")


# # Q9. Write a program to reverse a stack.

# In[2]:


class Stack:
 
    # create empty list
    def __init__(self):
        self.Elements = []
         
    # push() for insert an element
    def push(self, value):
        self.Elements.append(value)
       
    # pop() for remove an element
    def pop(self):
        return self.Elements.pop()
     
    # empty() check the stack is empty of not
    def empty(self):
        return self.Elements == []
     
    # show() display stack
    def show(self):
        for value in reversed(self.Elements):
            print(value)
 
# Insert_Bottom() insert value at bottom
def BottomInsert(s, value):
   
    # check the stack is empty or not
    if s.empty():
        s.push(value)
    else:
        popped = s.pop()
        BottomInsert(s, value)
        s.push(popped)
 
# Reverse() reverse the stack
def Reverse(s):
    if s.empty():
        pass
    else:
        popped = s.pop()
        Reverse(s)
        BottomInsert(s, popped)
 
 
# create object of stack class
stk = Stack()
 
stk.push(1)
stk.push(2)
stk.push(3)
stk.push(4)
stk.push(5)
 
print("Original Stack")
stk.show()
 
print("\nStack after Reversing")
Reverse(stk)
stk.show()


# # Q10. Write a program to find the smallest number using a stack.

# In[1]:


First = []
num = int(input('How many numbers: '))

for n in range(num):
    numbers = int(input('Enter number: '))
    First.append(numbers)
    
print("Smallest number in the list is :  ", min(First))


# In[ ]:




