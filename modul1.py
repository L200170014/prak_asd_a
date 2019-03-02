##--------------------------------------------------NO. 1-----------------------------------------------------##
def cetakSiku(x):
    for i in range (1, x+1):
       print (i * "*")

cetakSiku(5)


##--------------------------------------------------NO. 2-----------------------------------------------------##
def persegiEmpat (x, y) :
    for i in range (x) :
        if i == 0 or i == x-1 :
            print ("@" *y )
        else :
            print ("@" + " " * (y-2) + "@")


##--------------------------------------------------NO. 3 (a)-----------------------------------------------------##
def jumlahHurufVokal (s) :
    vok = 'aiueo'
    jumlah = 0
    for i in s:
        if i.lower() in vok:
            jumlah += 1
    return (len(s), jumlah)

print (jumlahHurufVokal('surakarta'))


##--------------------------------------------------NO. 3 (b)-----------------------------------------------------##
def jumlahHurufKonsonan (s) :
    vok = 'aiueo'
    jumlah = 0
    for i in s:
        if i.lower() not in vok:
            jumlah += 1
    return (len(s),jumlah)
print (jumlahHurufKonsonan('surakarta'))


##--------------------------------------------------NO. 4-----------------------------------------------------##
def rerata(b):
    jumlah = 0
    for i in b:
        jumlah += i
    return jumlah/len(b)
print (rerata([1,2,3,4,5]))
g = [3,4,5,4,3,5,2,2,10,11,23]
print (rerata(g))


##--------------------------------------------------NO. 5-----------------------------------------------------##
from math import sqrt as sq
def apakahPrima(n):
    n = int (n)
    assert n>=0
    primaKecil = [2,3,5,7,11]
    bukanPrKecil = [0,1,4,6,8,9,10]
    if n in primaKecil:
        return True
    elif n in bukanPrKecil:
        return False
    else:
        for i in range(2, int(sq(n))+1):
            if (n % 2) == 1:
                if (n % 3) != 0:
                    if (n % 5) != 0:
                        return True
                else:
                    return False


##--------------------------------------------------NO. 6-----------------------------------------------------##
k = [2, 3, 5]
for n in range (2, 1000):
    if n in k:
        print(n)
    elif (n% 2) == 1:
        if (n % 3) != 0:
            if (n % 5) != 0:
                print(n)


##--------------------------------------------------NO. 7-----------------------------------------------------##
def faktorPrima(n):
    list = []
    loop = 2
    while loop <= n:
        if (n % loop) == 0:
            n /= loop
            list.append(loop)
        else:
            loop += 1
    return list
print(list)


##--------------------------------------------------NO. 8-----------------------------------------------------##
h = input("h = ")
k = input("k = ")
def apakahTerkandung(h, k):
    if h in k:
        return True
    else:
        return False


##--------------------------------------------------NO. 9-----------------------------------------------------##
for i in range (1, 100):
    if (i % 3) == 0 and (i % 5) == 0:
        i = "Python UMS"
    elif (i % 3) == 0:
        i = "Python"
    elif (i % 5) == 0:
        i = "UMS"
    print(i)


##--------------------------------------------------NO. 10-----------------------------------------------------##
from math import sqrt as akar
def selesaikanABC (a, b, c):
    a = float(a)
    b = float(b)
    c = float(c)
    D = b**2 - 4*a*c
    if (D < 0):
        print("Determinannya negatif. Persamaan tidak mempunyai akar real.")
    else:
        x1 = (-b + akar(D))/(2*a)
        x2 = (-b + akar(D))/(2*a)
        hasil = (x1, x2)
        return hasil


##--------------------------------------------------NO. 11-----------------------------------------------------##
def apakahKabisat(n):
    b = int(n)
    if (n % 4) == 0:
        if (n % 100) == 0:
            if (n % 400) == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


##--------------------------------------------------NO. 12-----------------------------------------------------##
import random
r = random.randint(1, 100)
print("""Permainan tebak angka.\nSaya menyimpan sebuah angka bulat antara 1 sampai 100. Coba tebak.""")
b = "Masukkan tebakan ke-"
f = ":> "
c = 1
d = str(c)
for i in range (1, 100):
    e = (b+d+f)
    a = int(input(e))
    c+=1
    d = str(c)
    if (a < r):
        print("Itu terlalu kecil. Coba lagi.")
    elif (a > r):
        print("Itu terlalu besar. Coba lagi.")
    elif (a == r):
        print("Ya. Anda benar")
        break


##--------------------------------------------------NO. 13-----------------------------------------------------##
angka = {1:"satu " , 2:"dua " , 3:"tiga " , 4:"empat " , 5:"lima " , 6:"enam " , 7:"tujuh " , 8:"delapan " , 9:"sembilan "}

b = "puluh "
c = "ratus "
d = "ribu "
e = "juta "
f = "milyar "
g = "triliun"

def katakan(x):
    y = str(x)
    n = len(y)
    if n <= 3:
        if n == 1:
            if y == "0":
                return ""
            else:
                return angka[int(y)]
        elif n == 2:
            if y[0] == "1":
                if y[1] == "1":
                    return "sebelas"
                elif y[0] == "0":
                    x = y[1]
                    return katakan(x)
                elif y[1] == "0":
                    return "sepuluh"
                else:
                    return angka[int(y[1])]+ "belas"
            elif y[0] == "0":
                x = y[1]
                return katakan(x)
            else:
                x = y[1]
                return angka[int(y[0])]+ b + katakan(x)
        else:
            if y[0] == "1":
                x = y[1:]
                return "seratus "+ katakan(x)
            elif y[0] == "0":
                x = y[1:]
                return katakan(x)
            else:
                x = y[1:]
                return angka[int(y[0])]+ c + katakan(x)
    elif 3 < n <= 6:
        p = y[-3:]
        q = y[:-3]
        if q == "1":
            return "seribu " + katakan(p)
        elif q == "000":
            return katakan(p)
        else:
            return katakan(q) + d + katakan(p)
    elif 6 < n <=9:
        r = y[-6:]
        s = y[:-6]
        return katakan(s) + e + katakan(r)
    elif 9 < n <=12:
        t = y[-9:]
        u = y[:-9]
        return katakan(u) + f + katakan(t)
    else:
        v = y[-12:]
        w = y[:-12]
        return katakan(w) + g + katakan(v)


##--------------------------------------------------NO. 14-----------------------------------------------------##
def formatRupiah(n):
    a = str(n)
    if len(a) <= 3:
        return "Rp " + a
    else:
        p = a[-3:]
        q = a[:-3]
        return formatRupiah(q) + "." + p
        print ("Rp " + formatRupiah(q) + "." + p)
