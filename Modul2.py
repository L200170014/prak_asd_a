##  NAMA : ARLIN WIDYA RAHAYU
##  NIM : L200170014
##  KELAS : A

##-------------------------------No. 1-------------------------------
class Pesan(object):
    """
    Sebuah class bernama Pesan.
    Untuk memahami konsep Class dan Object.
    """
    def __init__(self, string):
        self.teks = string
    def cetakIni(self):
        print(self.teks)
    def cetakPakaiHurufKapital(self):
        print(str.upper(self.teks))
    def cetakPakaiHurufKecil(self):
        print(str.lower(self.teks))
    def jumKar(self):
        return len(self.teks)
    def cetakJumlahKarakterku(self):
        print('kalimatku mempunyai', len(self.teks), 'karakter')
    def perbarui(self,stringBaru):
        self.teks = stringBaru


##-------------------------------No. 1a-------------------------------
    def apakahTerkandung(self, a):
        if a in self.teks:
            return True
        else:
            return False


##-------------------------------No. 1b-------------------------------
    def hitungKonsonan(self):
        self.vokal = 'aiueoAIUEO'
        jumlah = 0
        for i in self.teks:
            if i.lower() not in self.vokal:
                jumlah +=1
        return jumlah


##-------------------------------No. 1c-------------------------------
    def hitungVokal(self):
        self.vokal = 'aiueoAIUEO'
        jumlah = 0
        for i in self.teks:
            if i.lower() in self.vokal:
                jumlah +=1
        return jumlah


##-------------------------------No. 2-------------------------------
class Manusia(object):
    """Class 'Manusia' dengan inisiasi 'nama' """
    keadaan = 'lapar'
    def __init__(self, nama):
        self.nama = nama
    def ucapkanSalam(self):
        print("Salaam, namaku", self.nama)
    def makan(self, s):
        print("Saya baru saja makan", s)
        self.keadaan = 'kenyang'
    def olahraga(self,k):
        print("Saya baru saja latihan", k)
        self.keadaan = 'lapar'
    def mengalikanDenganDua(self,n):
        return n*2


class Mahasiswa(Manusia):
    """Class Mahasiswa yang dibangun dari kelas Manusia"""
    def __init__(self,nama,NIM,kota,us):
        """Metode inisiasi ini menutupi metode inisiasi di class Manusia."""
        self.nama = nama
        self.NIM = NIM
        self.kotaTinggal = kota
        self.uangSaku = us
    def __str__(self):
        s = self.nama + ', NIM ' + str(self.NIM) \
            + '. Tinggal di ' + self.kotaTinggal \
            + '. Uang saku Rp ' + str(self.uangSaku) \
            +' tiap bulannya.'
        return s
    def ambilNama(self):
        return self.nama
    def ambilNIM(self):
        return self.NIM
    def ambilUangSaku(self):
        return self.uangSaku
    def makan(self, s):
        """Metode ini menutupi 'makan'-nya class Manusia.
        Mahasiswa kalau makan sambil belajar."""
        print("Saya baru saja makan",s,"sambil belajar.")
        self.keadaan = 'kenyang'


##-------------------------------No. 2a-------------------------------
    def ambilKotaTinggal(self):
        return self.KotaTinggal


##-------------------------------No. 2b-------------------------------
    def perbaruiKotaTinggal(self, kotabaru):
        self.KotaTinggal = kotabaru


##-------------------------------No. 2c-------------------------------
    def tambahUangSaku(self, tambahUang):
        self.uangSaku = self.uangSaku + tambahUang


##-------------------------------No. 3-------------------------------
##print("Masukkan data mahasiswa baru!")
##p = input("Masukkan Nama: ")
##q = input("Masukkan NIM: ")
##r = input("Masukkan Uang Saku: ")
##s = input("Masukkan Kota Tinggal: ")
##
##mhs = Mahasiswa (p, q, r, s)


##-------------------------------No. 4-------------------------------
    listKuliah = []
    def ambilKuliah(self, kuliah):
        self.listKuliah.append(kuliah)


#-------------------------------#No. 5-------------------------------
    def hapusKuliah(self, hapus):
        self.listKuliah.remove(hapus)


##-------------------------------No.6-------------------------------
class SiswaSMA(Manusia):
    """Class SiswaSMA yang dibangun dari class Manusia."""
    def __init__(self, nama, nis, kelas, alamat):
        """Metode inisiasi ini menutupi metode inisiasi di class Manusia."""
        self.nama = nama
        self.NIS = nis
        self.kelas = kelas
        self.alamat = alamat
    def __str__(self):
        v = "Nama Siswa: " + self.nama + "\nNomor Induk Siswa: " + self.NIS + "\nKelas: " + self.kelas + "\nAlamat: " + self.alamat
        return v
    def ambilNama(self):
        return self.nama
    def ambilNIS(self):
        return self.NIS
    def ambilKelas(self):
        return self.kelas
    def ambilAlamat(self):
        return self.alamat


##-------------------------------No. 7-------------------------------
## no 7 di file Modul2_no7.py
