import multiprocessing
from traceback import print_tb
from playsound2 import playsound
import time
def error_question(message):
    print(message)
    time.sleep(2)
    p = multiprocessing.Process(target=playsound, args=("14.mp3",))
    p.start()
    ret = int
    while True:
        inp = input("Again: y Continues: n")
        if inp == 'y':
            ret = 1
            break
        elif inp == 'n':
            ret = 0
            break
        else:
            print('type n or y')
    p.terminate()
    return ret
def error_warning(message):
    print(message)
    time.sleep(2)
    p = multiprocessing.Process(target=playsound, args=("14.mp3",))
    p.start()
    ret = int
    while True:
        inp = input("Turn off the warning enter:")
        if inp == 'y':
            ret = 1
            break
        elif inp == 'n':
            ret = 0
            break
        else:
            break
    p.terminate()
    return ret
def error_request(message):
    print(message)
    time.sleep(2)
    p = multiprocessing.Process(target=playsound, args=("14.mp3",))
    p.start()
    ret = int
    while True:
        inp = input("plise enter var to input")
        p.terminate()
        return inp
        

    
