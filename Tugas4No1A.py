A=10

def Kirim():
    B=15
    global C
    C=25
    print("1. Modul kirim: Nilai A, B, C : ",A,B,C)

def Terima():
    print("2. Modul terima: Nilai A, B, C : ", A, B, C)



Kirim()
Terima()
B = 10
print("Diluar Modul: Nilai A, B, C : ", A, B, C)
