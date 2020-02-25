from multiprocessing import Process
import os
import time

def info():
    global b
    a=time.time()
    cc=0
    for i in range(100000000):
        cc=cc+1
    b=time.time()-a
    print("2nd",b)
   
def f():
    global bb
    a=time.time()
    c=0
    for i in range(100000000):
        c=c+1
    bb=time.time()-a
    print("1st",bb)

if __name__ == '__main__':
   
    p1 = Process(target=f)
    p2 = Process(target=info)
    p1.start()
    p2.start()
