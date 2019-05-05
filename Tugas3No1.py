import time
import random
import multiprocessing
from random import randint

def bilGenap():
    for i in range(11,21):
        if(i%2==0):
            print("Bil genap mulai 11 : ",i)
            time.sleep(randint(1,4))


def bilGenapPrima():
    for i in range(2, 12):
        if(i % 2 == 0):
            print("Bil genap mulai Prima : ", i)
            time.sleep(randint(1, 4))

def bilGanjil():
    for i in range(50,60):
        if(i%2==1):
            print("Bil ganjil mulai 50 : ",i)
            time.sleep(randint(1,4))

def bilAcak():
    for _ in range(0,5):
        print("Bil acak antara 100 sd 200 : ",random.randrange(100,200))
        time.sleep(randint(1,4))

if __name__ == '__main__':
    worker1 = multiprocessing.Process(target=bilGenap)
    worker2 = multiprocessing.Process(target=bilGenapPrima)
    worker3 = multiprocessing.Process(target=bilGanjil)
    worker4 = multiprocessing.Process(target=bilAcak)

    worker1.start()
    worker2.start()
    worker3.start()
    worker4.start()

    worker1.join()
    worker2.join()
    worker3.join()
    worker4.join()
