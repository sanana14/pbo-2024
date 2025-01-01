# For Test using or import modul
# Main code untuk test modul projek bersama

import modul_satu_pbo as msatu

# ini contoh implementasi atau menguji fungsi dan class, versi saya
p = msatu.test("Halo.. This is the MMMMM ");
print ("\nTest Pesan : ", p.mes(), "\n")


# silahkan uji fungsi dan class anda dibawah
# pastikan class dan fungsi sudah anda buat di modul_satu_pbo.py

from modul import Barang
barang1 = Barang(nama="Laptop", harga=10000000, diskon=10, pajak=5)
barang2 = Barang(nama="Smartphone", harga=5000000, diskon=5, pajak=10)

# Menampilkan hasil perhitungan
print(f"Nama Barang: {barang1.nama}")
print(f"Harga Awal: Rp{barang1.harga}")
print(f"Setelah Diskon: Rp{barang1.harga_setelah_diskon()}")
print(f"Setelah Pajak: Rp{barang1.harga_setelah_pajak()}")
print(f"Total Harga: Rp{barang1.total_harga()}")
print()

print(f"Nama Barang: {barang2.nama}")
print(f"Harga Awal: Rp{barang2.harga}")
print(f"Setelah Diskon: Rp{barang2.harga_setelah_diskon()}")
print(f"Setelah Pajak: Rp{barang2.harga_setelah_pajak()}")
print(f"Total Harga: Rp{barang2.total_harga()}")
