from multiprocessing import Process, Pipe
import random
import time
from random import randint

DataSensor = [[600,300,15],[600,300,15],[600,300,15],[600,300,15],['Merah','Kuning','Hijau']]
L=[ 'Terus','Terus','Belok Kiri','Terus','Belok Kanan', 'Terus', 'Belok Kanan']

V = 60

# definisi fungsi lampu lalu lintas
def LampuLalin(Koneksi):
    n=0
    while n < 5:
        #mengisi nilai variabel lampu dengan 2 parameter (nama, jenis lampu, jarak lampu)
        acak = randint(0,2)
        jarak = randint(1, 2)
        lampu = ['lampu lalin', DataSensor[4][acak], DataSensor[0][jarak]]
        #mengirim data ke pipa
        Koneksi.send(lampu)
        n += 1
        time.sleep(1)

# definisi fungsi sensor depan
def Depan(Koneksi):
    n = 0
    while n < 5:
        #mengisi nilai variabel depan dengan 2 parameter (nama, jarak)
        acak = randint(0, 2)
        depan = ['depan', DataSensor[0][acak]]
        #mengirim data ke pipa
        Koneksi.send(depan)
        # Koneksi.close()
        n += 1
        time.sleep(2)

# definisi fungsi sensor belakang
def Belakang(Koneksi):
    n = 0
    while n < 5:
        #mengisi nilai variabel dengan 2 parameter (nama, jarak)
        acak = randint(0, 2)
        belakang = ['belakang', DataSensor[1][acak]]
        #mengirim data ke pipa
        Koneksi.send(belakang)
        # Koneksi.close()
        n += 1
        time.sleep(2)

# definisi fungsi sensor kiri
def Kiri(Koneksi):
    n = 0
    while n < 5:
        #mengisi nilai variabel dengan 2 parameter (nama, jarak)
        acak = randint(0, 2)
        kiri = ['kiri', DataSensor[2][acak]]
        #mengirim data ke pipa
        Koneksi.send(kiri)
        # Koneksi.close()
        n += 1
        time.sleep(2)
    
# definisi fungsi sensor kanan
def Kanan(Koneksi):
    n = 0
    while n < 5:
        #mengisi nilai variabel dengan 2 parameter (nama, jarak)
        acak = randint(0, 2)
        kanan = ['kanan', DataSensor[3][acak]]
        #mengirim data ke pipa
        Koneksi.send(kanan)
        # Koneksi.close()
        n += 1
        time.sleep(2)

# definisi fungsi berhenti
def berhenti():
    global V
    t = 10
    while t:
        mins, secs = divmod(t, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(timeformat,', kecepatan : ',V)
        time.sleep(1)
        t -= 1
        if(V > 0):
            V -= 20
    print('Mobil Jalan!\n\n\n\n\n')
    while (V < 60):
        V = V + 20
        print('Kecepatan : ', V)
    V = 60


def MasterControl(Koneksi):
    while(1):
        #menerima nilai dari pipa
        terima = Koneksi.recv()
        sensor = terima[0]
        nilai = terima[1]
        jarak = 0
        V = 60
        jAmanKanan = 30
        jAmanKiri = 20
        jAmanDepan = 400
        
        if(sensor=='lampu lalin'):
            jarak = terima[2]
            if(nilai == 'Merah'):
                print('Lampu merah yang diterima dengan jarak depan : ',jarak, 'cm')
            elif(nilai == 'Kuning'):
                print('Lampu kuning yang diterima dengan jarak depan : ',jarak, 'cm')
            elif(nilai == 'Hijau'):
                print('Lampu hijau yang diterima dengan jarak depan : ',jarak, 'cm')
        else:
            print('Nilai jarak ', sensor, ' yang diterima : ', nilai, ' cm')
        
        if(sensor == 'lampu lalin'):
            if(nilai == 'Merah' and jarak <= jAmanDepan):
                print('Berhenti di trafik...')
                berhenti()
            elif(nilai == 'Merah' and jarak <= 200):
                print('Sebaiknya berhenti di trafik...')
                berhenti()
            elif(nilai == 'Kuning'):
                print('Kurangi kecepatan | Kecepatan : ', V-20)
            elif(nilai == 'Hijau'):
                print('Jalan terus..')
        elif(sensor == 'depan'):
            if(nilai <= 200):
                print('Rem mobil | Kecepatan : ', V-40)
            elif(nilai <= jAmanDepan):
                print('Kurangi kecepatan | Kecepatan : ', V-20)
            else:
                print('Jarak aman | Kecepatan : ', V)
        elif(sensor == 'belakang'):
            if(nilai <= 200):
                print('Rem mobil | Kecepatan : ', V-40)
            elif(nilai <= 500):
                print('Tambah kecepatan | Kecepatan : ', V)
            else:
                print('Jarak aman | Kecepatan : ', V)
        elif(sensor == 'kiri'):
            if(nilai <= jAmanKiri):
                print('Geser kanan | kira kira : ', 200-nilai,' cm')
            else:
                print('Jarak aman | Kecepatan : ', V)
        elif(sensor == 'kanan'):
            if(nilai <= jAmanKanan):
                print('Geser kiri | kira kira: ', 200-nilai,' cm')
            else:
                print('Jarak aman | Kecepatan : ', V)

        print('')
        time.sleep(1)

if __name__ == '__main__':
    PipaIN, PipaOUT = Pipe()
    ProsesDepan = Process(target=Depan,args=(PipaIN,))
    ProsesBelakang = Process(target=Belakang, args=(PipaIN,))
    ProsesKiri = Process(target=Kiri, args=(PipaIN,))
    ProsesKanan = Process(target=Kanan, args=(PipaIN,))
    ProsesLalin = Process(target=LampuLalin, args=(PipaIN,))
    ProsesKendali = Process(target=Kendali, args=(PipaIN,))
    ProsesMasterControl = Process(target=MasterControl, args=(PipaOUT,))

    ProsesDepan.start()
    ProsesBelakang.start()
    ProsesKiri.start()
    ProsesKanan.start()
    ProsesLalin.start()
    ProsesKendali.start()
    ProsesMasterControl.start()

    ProsesDepan.join()
    ProsesBelakang.join()
    ProsesKiri.join()
    ProsesKanan.join()
    ProsesLalin.join()
    ProsesKendali.join()
    ProsesMasterControl.join()

