from threading import Thread,Lock

lock1 = Lock()
lock2 = Lock()

def print_num():
    for i in range(1,52,2):
        lock1.acquire()
        print(i)
        print(i+1)
        lock2.release()

def print_char():
    chars = [chr(x) for x in range(65,91)]
    for i in chars:
        lock2.acquire()
        print(i)
        lock1.release()

t1 = Thread(target=print_num)
t2 = Thread(target=print_char)

lock2.acquire() # 先让print_char锁住

t1.start()
t2.start()
t1.join()
t2.join()




