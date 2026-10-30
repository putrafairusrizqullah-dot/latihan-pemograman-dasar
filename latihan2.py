print("Program Menghitung Lingkaran")

print("1. menghitung keliling lingkaran")
print("2. menghitung luas lingkaran")

pilihan = int(input("masukkan pilihan (1/2): 1"))
r = float(input("masukkan jari-jari lingkaran: 10 "))

phi = 3.14 

if pilihan == 1:
    keliling = 2 * phi * r
    print("Keliling lingkaran adalah:62.8", keliling)
elif pilihan == 2:
    luas = phi * r**2
    print("Luas lingkaran adalah:314.0", luas)
else:
    print("Pilihan tidak valid")