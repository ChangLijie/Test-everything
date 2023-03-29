
from multiprocessing.pool import ThreadPool
import os, time
from multiprocessing import Process , Pool
import os, time 
import  numpy as np  
import random

def main_map(i, o):
    result = i*o
    print("thread 1 :",result , '\n')
    return result

def main_map2(i , o):
    result = i*o
    
    print("thread 2 :",result , '\n')
    return result 

if __name__ == '__main__':
    x , y , z= random.random()+1,random.random()+1,random.random()+1
    img = np.full([1080,1920, 3],127).astype(np.uint8)
    

    #multi process
    pool = Pool(15)

    # #multi thread
    # pool = ThreadPool(15)

    while(True):
        # multi process
        pool.map_async(main_map, (img.copy(),[x,y,z]))
        pool.map_async(main_map2, (img.copy(),[x,y,z]))

        # #multi thread
        # pool.apply_async(main_map, (img.copy(),[x,y,z]))
        # pool.apply_async(main_map2, (img.copy(),[x,y,z]))
        


        time.sleep(1e-3)