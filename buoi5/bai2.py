a=[]
n = int(input("Nhap so phan tu list : "))
for i in range (n):
    n1=str(input("Nhap phan tu so "+str(i+1)+":"))
    for b in n1 :
        a.append(b)
print(list(a),sep=" ,", end="\n")