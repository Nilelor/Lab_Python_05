number=int(raw_input("Enter a number"))

def factorial(input):
    sum=1
    for i in range(1,input+1):
        sum=sum*i
    return sum

print "the factorial of", number,"is",factorial(number)

print'-----------------'

number=int(raw_input("Please enter an integer"))


def fibonacci(n):
    list=[1,1]
    for i in range(2,n):
#list=[1,1]
        a =list[i-1]+list[i-2]
        list.append(a)
    return list

print fibonacci(number)
print'----------------------'

number=int(raw_input("Please enter a number"))

def prime(n):
    count=0    
    for i in range(1,n+1):
        if n%i==0:
            count=count+1
    if count==2:
        return True
    else:
        return False

print prime(number)
           
           

