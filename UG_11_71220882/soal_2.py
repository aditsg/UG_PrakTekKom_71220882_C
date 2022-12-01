print ("pemeriksa kelipatan9")
kel9 = int(input("masukan kelipatan 9 yang ingin diperiksa :"))

def kelipatan_9(kel9):
    hasil = kel9 % 9
    return hasil
if kelipatan_9(kel9)==0:
    print("benar")
else :
    print("salah")
