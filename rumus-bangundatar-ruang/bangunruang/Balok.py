panjang = int(input("Panjang : "))
lebar = int(input("Lebar   : "))
tinggi = int(input("Tinggi  : "))

luas = 2 * (panjang*lebar + panjang*tinggi + lebar*tinggi)
volume = panjang * lebar * tinggi

print("Luas    =", luas)
print("Volume  =", volume)