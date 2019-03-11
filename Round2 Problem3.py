#ECOO2018 round2 Problem 3

k = int(input("K:"))
m = int(input("M:"))
km = k**m

#creat a loop to count factorial numbers
running = True
n = 1
while running == True:
    n += 1
    f = 1
    for i in range(1,n+1):
        f = f*i
        #print("The factorial of",n,"is",f)
        if f % km == 0:
            print("K=",k,"M=",m,"N=",n,"N!=",f)
            running = False
