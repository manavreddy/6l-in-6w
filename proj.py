import time
import threading
x = 0
def increment_num(i):
    global x
    i = i+1
    x = i

endtime = time.time() + 1
while time.time() < endtime:
    t1 = threading.Thread(target = increment_num, args=[x])
    t2 = threading.Thread(target = increment_num, args=[x])
    t1.start()
    t2.start()
    t1.join()
    t2.join()
print(x)
