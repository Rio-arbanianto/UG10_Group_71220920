print("selamat datang di kalkulator sederhana")
print("1. penjumlahan")
print("2. pengurangan")
print("3. perkalian")
print("4. pembagian")
print("5. sisa hasil modulus")
print("6. menghitung pemangkatan")


b=int(input("bilangan pertama:"))
c=int(input("masukan bilanagn kedua:"))
a=int(input("masukan pilihan anda:"))

penjumlahan = b+c
pengurangan= b-c
perkalian= b*c
pembagian= b/c
sisahasilmodulus=b
pemangkatan=b**2

if c == 1:
  print("hasil penjumlahan:",penjumlahan)
elif operasi == 2:
  print("hasil penjumlahan:",pengurangan)
elif operasi == 3:
  print("hasil penjumlahan:",perkalian)
elif operasi == 4:
  print("hasil penjumlahan:",pembagian)
  elif operasi == 5:
  print("sisa hasil modulus",sisahasilmodulus)
elif operasi == 6:
  print("hasil penjumlahan:",pemangkatan)
else:
  print('Tidak valid')
