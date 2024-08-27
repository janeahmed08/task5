fib=int(input("enter num"))
a=0
b=1
for i in range(fib):
    c=a+b
    a=b
    b=c
    print(c)