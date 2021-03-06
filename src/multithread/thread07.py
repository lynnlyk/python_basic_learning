'''
利用time函数，生成两个函数
顺序调用
计算总的运行时间
'''
import time
import threading

def loop1():
    # ctime 得到当前时间
    print('Start loop1 at :', time.ctime())
    # 睡眠多长时间，单位是秒
    time.sleep(4)
    print('End loop1 at:', time.ctime())

def loop2():
    # ctime 得到当前时间
    print('Start loop2 at :', time.ctime())
    # 睡眠多长时间，单位是秒
    time.sleep(2)
    print('End loop2 at:', time.ctime())

def loop3():
    # ctime 得到当前时间
    print('Start loop3 at :', time.ctime())
    # 睡眠多长时间，单位是秒
    time.sleep(5)
    print('End loop3 at:', time.ctime())


def main():
    print('Starting at :', time.ctime())
    t1 = threading.Thread(target=loop1, args=())
    t1.setName("THR_1")
    t1.start()

    t2 = threading.Thread(target=loop2, args=())
    t2.setName("THR_2")
    t2.start()

    t3 = threading.Thread(target=loop3, args=())
    t3.setName("THR_3")
    t3.start()

    time.sleep(3)

    for thr in threading.enumerate():
        print("正在运行的线程名字是：{0}".format(thr.getName()))

    print("正在运行的线程数量是：{0}".format(threading.activeCount()))
    print('All done at:', time.ctime())

if __name__ == '__main__':
    main()