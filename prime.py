n=int(input("Enter a no:"))
f=0
for i in range(2,int(n/2+1)):
    if n%i==0:
        f=1
    break
if f==0:
    print("prime")
else:
    print("not prime")