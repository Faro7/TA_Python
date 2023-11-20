import module_banguundatar

print("Pilih bangun ruang yang akan dipilih")
print("1. Lingkaran")
print("2. Segitiga")

opsi = int(input("\nKetik Pilih: "))

if opsi == 1:
    print("Hitung Lingkaran ")
    r = int(input("Masukkan Nilai Jari-jari: "))
    module_banguundatar.lingkaran(r)
elif opsi == 2:
    print("Hitung Segitiga ")
    a = int(input("Masukkan Nilai Alas: "))
    t = int(input("Masukkan Nilai Tinggi: "))
    module_banguundatar.segitiga(a, t)