import pandas
df=pandas.read_excel("IDENTIFICATION.xlsx",header=1)
print(df)
num1=2
num2=3
sum=num1+num2
print(sum)

def welcome(name):
    value=("welcome" +name+ "here")
    return value
print(welcome('louise'))

def greeting():
    value=('hello louise')
    return value
print(greeting())

def addition():
    a=2
    b=3
    sum=a+b
    return sum
print(addition())

num1= input()
num2= input()
sum= int (num1)+ int (num2)

print(sum)

days=["mon",'tue','wedn','thus','frid','satur','sun']
for n in days:
 print(n)
