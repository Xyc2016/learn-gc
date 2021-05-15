import gc
import random
gc.set_debug(gc.DEBUG_STATS)


def f():
    # "abcdefg" * random.randint(100, 199)
    return [1, 2] * 10000

l1 = []
print("\n" * 2)
for _ in range(1000):
    l = f()
    # print(l)
    l1.append(l)
    # gc.collect()

import os, psutil
process = psutil.Process(os.getpid())
print(process.memory_info().rss / 1024 /1024)


print("\n" * 2)