import os
os.system("cls") #windows
#os.system("clear") #linux
print("KALKULATOR SUHU")
'''
while True:
    try:
       suhu = int(input("1.Celsius \n2.Reaumur \n3.Fahrenheit \n4.Kelvin \n\nSilahkan pilih suhu yang anda punya (masukkan nomor): "))
       continue
    except ValueError:
        print("Masukkan nomor!")
        continue
    else:
        break
'''
suhu = int(input("1.Celsius \n2.Reaumur \n3.Fahrenheit \n4.Kelvin \n\nSilahkan pilih suhu yang anda punya (masukkan nomor): "))
if suhu==1:
    os.system("cls")
    c = float(input("Masukkan suhu \nCelsius= "))
    r = (4/5)*c
    f = (9/5)*c+32
    k = c+273
    print("Reamur=",r)
    print("Fahrenheit=",f)
    print("Kelvin=",k)
    print("\n")
if suhu==2:
    os.system("cls")
    r = float(input("Masukkan suhu \nReamur= "))
    c = (5/4)*r
    f = (9/4)*r+32
    k = c+273
    print("Celsius=",c)
    print("Fahrenheit=",f)
    print("Kelvin=",k)
    print("\n")
if suhu==3:
    os.system("cls")
    f = float(input("Masukkan suhu \nFahrenheit= "))
    c = (5/9)*(f-32)
    r = (4/9)*(f-32)
    k = c+273
    print("Celsius=",c)
    print("Reamur=",r)
    print("Kelvin=",k)
    print("\n")
if suhu==4:
    os.system("cls")
    k = float(input("Masukkan suhu \nKelvin= "))
    c = k-273
    r = (4/5)*c
    f = (9/5)*c+32
    print("Celsius=",c)
    print("Reamur=",r)
    print("Fahrenheit=",f)
    print("\n")
