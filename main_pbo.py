from modul import prodak
prodak1 = prodak(nama="Laptop", harga=10000000, diskon=10, pajak=5)
prodak2 =prodak (nama="Smartphone", harga=5000000, diskon=5, pajak=10)

# Menampilkan hasil perhitungan
print(f"Nama Barang: {prodak1.nama}")
print(f"Harga Awal: Rp{prodak1.harga}")
print(f"Setelah Diskon: Rp{prodak1.harga_setelah_diskon()}")
print(f"Setelah Pajak: Rp{prodak1.harga_setelah_pajak()}")
print(f"Total Harga: Rp{prodak1.total_harga()}")
print()

print(f"Nama Barang: {prodak2.nama}")
print(f"Harga Awal: Rp{prodak2.harga}")
print(f"Setelah Diskon: Rp{prodak2.harga_setelah_diskon()}")
print(f"Setelah Pajak: Rp{prodak2.harga_setelah_pajak()}")
print(f"Total Harga: Rp{prodak2.total_harga()}")
