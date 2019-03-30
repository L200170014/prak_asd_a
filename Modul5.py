##   Nama : Arlin Widya Rahayu
##   NIM  : L200170014
##   Kelas: A

##-------------------------------NO. 1-------------------------------
class Mahasiswa(object):
    """Class Mahasiswa yang dibangun dari class Manusia."""
    def __init__(self, nama, NIM, kota, us):
        """Metode inisiasi ini menutupi metode inisiasi di class Manusia"""
        self.nama = nama
        self.NIM = NIM
        self.kotaTinggal = kota
        self.uangSaku = us


class MhsTIF (Mahasiswa):
    """Class MhsTIF yang dibangun dari class Mahasiswa"""
    def katakanPy(self):
        print('Python is cool.')

c0 = MhsTIF('Ika', 10, 'Sukoharjo', 240000)
c1 = MhsTIF('Budi', 51, 'Sragen', 230000)
c2 = MhsTIF('Ahmad', 2, 'Surakarta', 250000)
c3 = MhsTIF('Chandra', 18, 'Surakarta', 235000)
c4 = MhsTIF('Eka', 4, 'Boyolali', 240000)
c5 = MhsTIF('Fandi', 31, 'Salatiga', 250000)
c6 = MhsTIF('Deni', 13, 'Klaten', 245000)
c7 = MhsTIF('Galuh', 5, 'Wonogiri', 245000)
c8 = MhsTIF('Janto', 23, 'Klaten', 245000)
c9 = MhsTIF('Hasan', 64, 'Karanganyar', 270000)
c10 = MhsTIF('Khalid', 29, 'Purwodadi', 265000)

Daftar = [c0, c1, c2, c3, c4, c5, c6, c7, c8, c9, c10]

def swap(A, p, q):
    tmp = A[p]
    A[p] = A[q]
    A[q] = tmp

def nimnya(daftar):
    for i in daftar:
        print(i.NIM)
        
def bubblesort(daftar):
    n = len(daftar)
    for i in range (n-1):
        for j in range(n-i-1):
            if daftar[j].NIM > daftar[j+1].NIM:
                swap(daftar,j,j+1)
                
bubblesort(Daftar)
print("-------------------------------NO. 1-------------------------------")
print(nimnya(Daftar))


##-------------------------------NO. 2-------------------------------
X = [1,3,6,10,11,20]
Y = [7,8,9,12,13,100]
C = X + Y

def urut(a):
    n = len(a)
    for i in range (n-1):
        for j in range(n-i-1):
            if a[j]> a[j+1]:
                swap(a,j,j+1)
urut(C)
print("\n-------------------------------NO. 2-------------------------------")
print (C)


##-------------------------------NO. 3-------------------------------
def bubbleSort(A):
    n = len(A)
    for i in range (n-1):
        for j in range (n-i-1):
            if A[j] > A[j+1]:
                swap(A,j,j+1)

def cariPosisiYangTerkecil(A, dariSini, sampaiSini):
    posisiYangTerkecil = dariSini
    for i in range (dariSini+1, sampaiSini):
        if A[i] < A[posisiYangTerkecil]:
            posisiYangTerkecil = i
    return posisiYangTerkecil
    
def selectionSort(A):
    n = len(A)
    for i in range (n-1):
        indexKecil = cariPosisiYangTerkecil(A, i, n)
        if indexKecil != i:
            swap(A, i, indexKecil)

def insertionSort(A):
    n = len(A)
    for i in range(1, n):
        nilai = A[i]
        pos = i
        while pos > 0 and nilai < A[pos - 1]:
            A[pos] = A[pos - 1]
            pos = pos - 1
        A[pos] = nilai

from time import time as detak
from random import shuffle as kocok
k = []
for i in range (1, 6001):
    k.append(i)
kocok(k)
u_bub = k[:]
u_sel = k[:]
u_ins = k[:]

print("\n-------------------------------NO. 3-------------------------------")
aw=detak();bubbleSort(u_bub);ak=detak();print('bubble: %g detik' %(ak-aw) );
aw=detak();selectionSort(u_sel);ak=detak();print('selection: %g detik' %(ak-aw) );
aw=detak();insertionSort(u_ins);ak=detak();print('insertion: %g detik' %(ak-aw) );
