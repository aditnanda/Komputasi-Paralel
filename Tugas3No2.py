from multiprocessing import Pool

data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def pangkat(x):
    return x**2

if __name__=="__main__":
    p=Pool(4)
    hasil = p.map(pangkat, data)
    print(hasil)
