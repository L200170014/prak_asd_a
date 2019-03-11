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

a = MhsTIF("a","b","c",67)
