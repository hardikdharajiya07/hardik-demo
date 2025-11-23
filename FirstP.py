"""print("Hello world 1")
a=10
b=20
sum=a+b
print(sum)
c=2
d=3
e='2'
txt="@"
s=input("name=")
print(s)
a=float(input("a="))
print(a)
print((e+txt)*d)
print(2*txt*3)
print(a//c)

light=input("color=")

if(light=="red"):
    print("stop")
elif(light=="yellow"):
    print("look")
else:
    print("go")     

#ternary opration
food=input("food=")
eat="yes" if food=='APPLE' else "no" 
print(eat) 

a=3
b=2
print(a%b)#remainder
print(a ** b)# power

#type cacsting

v=int('2')
s=4
print("sum=",v+s)

d=2
s=str(d)
print(type(s))
print(s)

str1="hello world. \ni am hardik."
print(str1)
print(len(str1))
# indexing

ch=str1[0]
print(ch)

#slicing not include ending inx
str2="apna college"
print(str2[0:5]) 
print(str2[:5])
print(str2[5:])
print(str2[6:len(str2)])

#slicing negetive 
str="apple"
print(str[-5:-1])

#function

print(str.endswith("ple"))
print(str.endswith("elp"))

str=str.capitalize()
print(str)

str3="apana college"
print(str3.replace("a","h"))
print(str3.find("n"))
print(str3.count("a"))"""

#List -> mutable
"""
mark=[1.2,3.2,4.2,5.2]
print(mark)
print(type(mark))
print(mark[2])
mark1=["hardik",101,"7.5"]
print(mark1)
mark1[0]="jay"
print(mark1)

#list method

mark1.append(21)
print(mark1)

mark.sort()
print(mark)
mark.sort(reverse=True)
print(mark)

mark.insert(1,2000)
print(mark)

mark.remove(1.2)# element remove
print(mark)

mark.pop(3)#pop index
print(mark)"""

#program 
"""
n1=input("n1=")
n2=input("n2=")
n3=input("n3=")
n=[]
n.append(n1)
n.append(n2)
n.append(n3)
print(n)

#pelindrom
list=[1,2,1,2]
list1=list.copy()
list1.reverse()
if(list1 == list):
    print('pelindrom')
else:
    print("not")   """ 




#tuple -> immutable
"""
tup=(1,2,3,4,5)
print(tup)
print(type(tup))
print(tup[0])

#type of tuple
tup1=(1,2,3,4,5)
tup2=(1,) # (,)is fixed
print(tup1)
print(type(tup2))"""

#Dicationary -> obj
"""
dist={
    "name" : "hardik",
    "roll" : [1,2,3,4],
    "spi" : 7.5,
    "location" : "rajkot"
}
print(dist)

print(dist["name"])
dist["surname"]="dharajiya"
print(dist)

#nested dicationary

stu = { 
    "name" : "hardik",
    "sub" : {
        "bio" : 83,
        "che" : 85,
        "phy" : 70
    }
}
print(stu)
print(stu["sub"])
print(stu["sub"]["bio"])

#method
print(stu.keys())

#print(stu("name1"))# error
print(stu.get("name1"))#no error -> none

stu.update({"spi" : 7.5})
print(stu)"""

#set -> unorder or duplicate ingnore
"""
set1={1,2,3,"hardik"}
print(set1)
set={1,2,2,3,"hello",3,3,"hello",4,4,"hello",4,4,4,4}
print(set)"""

# while loop 
"""i=1
while i<=5:
    print("hello")
    i+=1"""

#multiplication table
"""n=int(input("enter n="))

i=1
while i<=10:
    a=n*i
    print(n,"*",i,"=",a)
    i+=1"""

"""num= [1,4,9,16,25,36,49,64,81,100]
x=36
i=0
while i<len(num):
    print(num[i])
    i+=1

"""
"""num= [1,4,9,16,25,36,49,64,81,100]
x=36
i=0
while i<len(num):
    if(num[i] ==  x):
        print("num is found",i)
        break
    else:
        print("not found")    
    i+=1    """

#continue
"""i=0
while i<=5:
    if(i == 3):
        i+=1
    print(i)
    i+=1    
"""

# odd num
"""i=0
while i<10:
    if(i%2 == 0):
        i+=1
    print(i)
    i+=1  """ 

#sum of n
"""
n=5
i=1
sum=0
while i<=n:
    sum+=i
    i+=1
print(sum)"""
#for loop
"""
list= [1,2,3,4,5]

for el in list:
    print(el)
else:
    print("end loop")   """ 

"""list = [1,2,3,4,5,6,7,8]
x=5
i=0
for el in list:
    if(el == x):
        print("found" ,el)
        print('index=',i)
    i+=1    """

#range()

#print(range(5))

"""for i in range(5):
    print(i)"""

"""for i in range(1,10,2):
    print(i)"""

#factorial

"""n=3
fact=1
for el in range(1,n+1):
    fact *=el
print(fact)    """

# function 

"""def calSum(a,b):
    sum= a+b
    print(sum)

calSum(2,3)    

def cal_sum(a,b):
    return a+b

sum1=cal_sum(4,5)
print(sum1)
"""
"""
def pri_hello():
    print("hello")

for el in range(5):
    pri_hello()   """ 
#
"""num= [1,2,3,4,5,6,7]

def lenth(num):
    print(len(num))

lenth(num)   """
#
"""num=[1,2,3,4,5,6,7]

def pri_ele(num):
    for el in num:
        print(el,end=" ")

pri_ele(num)"""

#usd to inr

"""def convert(usd):
    inr=83
    for i in range(1,usd+1):
        inr*=i
    print(inr)

convert(4)"""

#odd even

"""def odd_even(n):
    if(n%2==0):
        print("even")
    else:
        print("odd") 

odd_even(120)
"""

# recurtion

"""def call(n):
    if(n==0):
        return
    print(n)
    call(n-1)

call(5)"""
#
"""def fact(n):
    if(n==0 or n==1):
        return 1
    else:
        return fact(n-1) * n
   
print(fact(3))    """
#
# def naturl(n):
   
#     if(n==0):
#         return 0
#     else:
#      return naturl(n-1) +n
  

# print(naturl(4))     

# class and object
"""
class Student():
    name="hardik"

s1=Student()
print(s1.name)    """

# constructor
"""class Student():
    def __init__(self,name,roll):
        self.name=name
        self.roll=roll

    def display(self):
        print("name=",self.name)
        print("roll=",self.roll)

stu1=Student("hardik",101)
stu1.display()
stu2=Student("jay",102)
stu2.display()"""


