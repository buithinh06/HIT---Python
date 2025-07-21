a= int(input("Nhap nam ban muon biet: "))
while a<1582:
        print("Khong hop le, hay nhap lai ")
        a= int(input("Nhap vao nam muon biet: "))
b= int(input("Nhap thang cua nam do: "))
while b<1 or b>12:
        print(" khong hop le, hay nhap lai")
        b=int(input("Nhap vao thang cua nam do: "))
if a%400==0 and b==2:
        print("Thang",b,"nam nhuan",a,"co 29 ngay")
elif (b<=7 and b%2==1) or (b>8 and b%2==0) :
        print("Thang",b,"nam",a,"co 31 ngay")
else:
        print("Thang",b,"nam",a,"co 30 ngay")