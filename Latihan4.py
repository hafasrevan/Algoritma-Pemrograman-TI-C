import math

while True:
    try:
        r = input("Masukkan jari-jari lingkaran: ")

        # Validasi input kosong
        if r.strip() == "":
            raise ValueError("Input tidak boleh kosong!")

        # Konversi ke angka
        r = float(r)

        # Validasi angka negatif
        if r < 0:
            raise ValueError("Jari-jari tidak boleh negatif!")

        luas = math.pi * r * r
        print("Luas lingkaran adalah:", luas)
        break

    except ValueError as e:
        print("Terjadi kesalahan:", e)
        print("Silakan masukkan angka yang benar!\n")