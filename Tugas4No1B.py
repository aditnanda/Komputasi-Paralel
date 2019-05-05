from multiprocessing import Process, Pipe

A=10
B=10

def Kirim(Koneksi):
    A=[15,25,35]
    Koneksi.send(A)
    print('nilai yang dikirim : ',A,B)
    Koneksi.close()

def Terima(Koneksi):
    print('Nilai yag diterima : ',Koneksi.recv(),B)

if __name__ == '__main__':
    PipaIN, PipaOUT = Pipe()
    ProsesKirim=Process(target=Kirim,args=(PipaIN,))
    ProsesTerima=Process(target=Terima, args=(PipaOUT,))

    ProsesKirim.start()
    ProsesTerima.start()

    ProsesKirim.join()
    ProsesTerima.join()