n=int(input("Nhap vao so luong xu: "))
while n<28:
    print("So xu khong hop le.")
    n=int(input("Nhap vao so luong xu: "))
sc=n//28
vo=sc
tong=sc
while vo>=3:
    doi=vo//3
    tong+=doi
    vo=vo%3+doi
print("Tien thua:",n-sc*28)
print("So chai bia co the mua duoc la: ",tong)
