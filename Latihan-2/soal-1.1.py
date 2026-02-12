def rata_rata(n):
    if len(n) == 0:
        return "Data Kosong"
    return sum(n) / len(n)

data = [80,75,90,60,85]
hasil = rata_rata(data)

print()
print("Rata-rata", hasil)