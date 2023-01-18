

from random import*
from math import*


#1

print(" -----")
print()
print("|  0  |")
print()
print("!  -  !")
print()
print(" -----")

#2
n = int(input("sisestage number: "))
while True:
   k = int(input("sisestage kraad: "))
   if k>3:
       break
for i in range(1,n+1):

   print(i**k,end=" ")

  
#3
u=randint(1,20)
o=0
for i in range(u):
    a=randint(1,5)
    o=o+a
print(f"keskmine hinne on {o/a}")

#4
r=1
a=1
while r<100:
    a+=1
    r+=a
    print(a,"Aasta vana",r,"raha")

#5
n = int(input("Sisestage Fibonacci number: "))
num, k, b = 1, 1, 1
while k!= n:
    k += 1
    print(b, end = ' ')
    b += num 
    num, b = b, num

    print()



