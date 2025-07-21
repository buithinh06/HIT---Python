n=int(input("Nhap vao 1 so bat ki: "))
n=abs(n)
scs=0
tong=0
if n==0:
    scs=1
    tong=0
else:
    while n>0:
        cs=n%10
        tong+=cs
        scs+=1
        n=n//10
print("So chu so la:",scs)
print("Tong cac chu so la:",tong)

