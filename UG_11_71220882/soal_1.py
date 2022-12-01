print("Operasi Matematika")
print("1. jumlah [+]")
print("2. kurang [-]")
print("3. kali [*]")
print("4. bagi [/]")
print("======================")
opsi = int(input("pilih operasi(1/2/3/4):"))
print("======================")
bil1 = int(input("masukan bilangan pertama:"))
bil2 = int(input("masukan bilangan kedua:"))

def jumlah(opsi,bil1,bil2):
    hasil = bil1+bil2
    return hasil
def kurang(opsi,bil1,bil2):
     hasil =  bil1-bil2
    return hasil 
def kali(opsi,bil1,bil2):
     hasil =  bil1*bil2
    return hasil
def bagi(opsi,bil1,bil2):     hasil =  bil1/bil2
    return hasil

if opsi == 1:
    hasil = bil1+bil2
elif opsi == 2:
    hasil = bil1-bil2
elif  opsi == 3:
   hasil = bil1*bil2
elif opsi == 4:
   hasil = bil1/bil2

print("hasil : %d" ,%hasil)
