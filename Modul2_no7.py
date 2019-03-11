##  NAMA : ARLIN WIDYA RAHAYU
##  NIM : L200170014
##  KELAS : A
##
##  Lanjutan file Modul2.py

import Modul2
class MhsTIF(Modul2.Mahasiswa):
    """Class MhsTIF yang dibangun dari class Mahasiswa"""
    def katakanPy(self):
        print('Python is cool.')


##  Pertanyaan :
##  Apakah metode / state itu berasal dari class Manusia, Mahasiswa, atau MhsTIF?
##  Jawab :
##  Metode atau state berasal dari class Manusia, class Mahasiswa, atau class MhsTIF.
##  class MhsTIF merupakan turunan dari class Mahasiswa, dan class Mahasiswa merupakan turunan dari class Manusia.
##  Sehingga class MhsTIF mewarisi sifat dari class Mahasiswa dan class Manusia.
