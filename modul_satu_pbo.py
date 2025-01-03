# modul projek bersama PBO untuk latihan Mahasiswa
# Mata Kulaih Pemrograman Berorientasi Objek (BPO)
# Semua Mahasiswa diharuskan berkontribusi pada modul ini
# Kontribusi berupa membuat class dan fungsi (lihat arahan lengkap di : https://infoummu.github.io/pbo/
# .
# ini class test dari elyas: 
class test:
    def __init__(self, m):
        self.__m=m
    
    def mes(self):
        return self.__m;
        
# ini Kontribusi dari Ikhwan 
def batas():
    print("-"*35)

# silahkan lanjutkan dengan fungsi dan calss anda dibawah
# pastikan untuk menguji class dan fungsi yang sudah di buat disini

#modul_satu_pbo.py
class prodak:
    def __init__(self, nama, harga, diskon=0, pajak=0):
        self.nama = nama
        self.harga = harga
        self.diskon = diskon
        self.pajak = pajak

    def harga_setelah_diskon(self):
        """Menghitung harga setelah diskon"""
        harga_diskon = self.harga * (self.diskon / 100)
        return self.harga - harga_diskon

    def harga_setelah_pajak(self):
        """Menghitung harga setelah pajak"""
        harga_diskon = self.harga_setelah_diskon()
        harga_pajak = harga_diskon * (self.pajak / 100)
        return harga_diskon + harga_pajak

    def total_harga(self):
        """Menghitung total harga setelah diskon dan pajak"""
        return self.harga_setelah_pajak()


