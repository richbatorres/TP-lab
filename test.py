from random import expovariate
import time


# list = [1, 2, 3, 5, 8, 47, 9]
# print(list[:2])
# print(list[2:])
# print(expovariate(0.96))

i=0
max_time = 5.798
start_time = time.time()  # remember when we started
while (time.time() - start_time) < max_time:
    i+=1
print(i)