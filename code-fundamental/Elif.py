print("--selain itu jika--")

print("--contoh 1, negatif, nol dan bulat menggunakan elif--")

d=0
if d <0:
    print("Negatif")
elif d >0:
    print("Positif")
else:
    print("Nol")
print()


print("--Contoh 2, K, BK, Pas--")
nilai=75
if nilai >=75:
    print("Kompeten")
elif nilai <75:
    print("Belum Kompeten")
else:
    print("Pas")
print()


print("--Contoh 3, Nilai A, B, C, D")
n = 100
if n >=80: #80-100
    print("A")
elif n >=75: #75-79
    print("B")
elif n >=70: #70-74
    print("C")
else: #<=69
    print("D")