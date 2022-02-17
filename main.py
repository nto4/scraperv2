import get_page
import os
import multiprocessing
import time


with open('data.csv', "r") as d:
    data = d.read().splitlines()

for i in range(len(data)):
    data[i] = "http://" + data[i]



if __name__ == '__main__':
    baslangic =  time.time()

    CPU_COUNT = 8 #int(os.environ['NUMBER_OF_PROCESSORS'])
    pool = multiprocessing.Pool(processes=CPU_COUNT)

    results = pool.map(get_page.runIt,data)
    saniye = time.time() - baslangic
    print("saniye surdu: " + str(saniye))
