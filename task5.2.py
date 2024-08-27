#b=int(input("enter beggining"))
num=int(input("enter num"))


for num in range(num):
    for i in range(2,num):
                if num%i==0:
                    break
    else:
                print(num)