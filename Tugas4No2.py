from multiprocessing import Process, Pipe
import random
import time

def Depan(Koneksi):
    n = 0
    while n < 5:
        depan=['depan',random.randrange(1,1000)]
        Koneksi.send(depan)
        # Koneksi.close()
        n += 1
        time.sleep(2)


def Belakang(Koneksi):
    n = 0
    while n < 5:
        belakang = ['belakang',random.randrange(1, 1000)]
        Koneksi.send(belakang)
        # Koneksi.close()
        n += 1
        time.sleep(2)


def Kiri(Koneksi):
    n = 0
    while n < 5:
        kiri = ['kiri', random.randrange(1, 1000)]
        Koneksi.send(kiri)
        # Koneksi.close()
        n += 1
        time.sleep(2)
    
def Kanan(Koneksi):
    n = 0
    while n < 5:
        kanan = ['kanan', random.randrange(1, 1000)]
        Koneksi.send(kanan)
        # Koneksi.close()
        n += 1
        time.sleep(2)

def MasterControl(Koneksi):
    while(1):
        terima = Koneksi.recv()
        sensor = terima[0]
        nilai = terima[1]
        print('Nilai jarak ',sensor,' yang diterima : ', nilai,' cm')
        
        if(sensor == 'depan'):
            if(nilai <= 200):
                print('Rem mobil')
            elif(nilai <= 500):
                print('Kurangi kecepatan')
            else:
                print('Jarak aman')
        elif(sensor == 'belakang'):
            if(nilai <= 200):
                print('Rem mobil')
            elif(nilai <= 500):
                print('Tambah kecepatan')
            else:
                print('Jarak aman')
        elif(sensor == 'kiri'):
            if(nilai <= 200):
                print('Geser kanan')
            else:
                print('Jarak aman')
        elif(sensor == 'kanan'):
            if(nilai <= 200):
                print('Geser kiri')
            else:
                print('Jarak aman')

        print('')
        time.sleep(1)

if __name__ == '__main__':
    PipaIN, PipaOUT = Pipe()
    ProsesDepan = Process(target=Depan,args=(PipaIN,))
    ProsesBelakang = Process(target=Belakang, args=(PipaIN,))
    ProsesKiri = Process(target=Kiri, args=(PipaIN,))
    ProsesKanan = Process(target=Kanan, args=(PipaIN,))
    ProsesMasterControl = Process(target=MasterControl, args=(PipaOUT,))

    ProsesDepan.start()
    ProsesBelakang.start()
    ProsesKiri.start()
    ProsesKanan.start()
    ProsesMasterControl.start()

    ProsesDepan.join()
    ProsesBelakang.join()
    ProsesKiri.join()
    ProsesKanan.join()
    ProsesMasterControl.join()

