from functools import partial
from threading import Thread
import multiprocessing


def singleCount(cnt, name):
    for i in range(1, 1000001):
        cnt += 1

# single process start
@profile
def single_process(lists):
    cnt = 0
    for each in lists:
        singleCount(cnt, each)

# multi process start
@profile
def multi_process(lists):
    cnt = 0
    pool = multiprocessing.Pool(processes=4)
    func = partial(singleCount, cnt)
    pool.map_async(func, lists)
    pool.close()
    pool.join()

# multi threading start
@profile
def multi_thread():
    cnt = 0
    th1 = Thread(target=singleCount, args=(cnt, "1"))
    th1.start()
    th1.join()
    th2 = Thread(target=singleCount, args=(cnt, "2"))
    th2.start()
    th2.join()
    th3 = Thread(target=singleCount, args=(cnt, "3"))
    th3.start()
    th3.join()
    th4 = Thread(target=singleCount, args=(cnt, "4"))
    th4.start()
    th4.join()

lists = ['1', '2', '3', '4']
single_process(lists)
multi_process(lists)
multi_thread()
