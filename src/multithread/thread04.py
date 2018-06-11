'''
利用time函数，生成两个函数
顺序调用
计算总的运行时间
'''
import time
import threading

def loop1(in1):
    # ctime 得到当前时间
    print('Start loop1 at :', time.ctime())
    # 打印参数
    print("我是参数 ", in1)
    # 睡眠多长时间，单位是秒
    time.sleep(4)
    print('End loop1 at:', time.ctime())

def loop2(in1, in2):
    # ctime 得到当前时间
    print('Start loop2 at :', time.ctime())
    # 打印参数
    print("我是参数 ", in1, "和参数 ", in2)
    # 睡眠多长时间，单位是秒
    time.sleep(2)
    print('End loop2 at:', time.ctime())

def main():
    print('Starting at :', time.ctime())
    t1 = threading.Thread(target=loop1, args=("wanglaoda",))
    t1.start()
    t2 = threading.Thread(target=loop2, args=("wangdapeng", "wangxiaopeng"))
    t2.start()

    t1.join()
    t2.join()
    print('All done at:', time.ctime())

if __name__ == '__main__':
    main()