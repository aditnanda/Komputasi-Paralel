import time
import random
import multiprocessing
from random import randint

def bilGanjil():
    for i in range(1,10):
        if(i%2==1):
            print("ganjil ",i)
            time.sleep(randint(1,3))
	
def bilGenap():
    for i in range(50,60):
        if(i%2==0):
            print("genap ",i)
            time.sleep(randint(1,3))

def bilAcak():
    for i in range(0,5):
        print("random ",random.randrange(100,500))
        time.sleep(randint(1,3))

if __name__ == '__main__':
    worker1=multiprocessing.Process(target=bilGanjil)
    worker2=multiprocessing.Process(target=bilGenap)
    worker3=multiprocessing.Process(target=bilAcak)

    worker1.start()
    worker2.start()
    worker3.start()

    worker1.join()
    worker2.join()
    worker3.join()
