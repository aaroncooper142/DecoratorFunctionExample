'''using a decorator function to test run times for multiple functions'''

import time
current_time = time.time()
print(current_time)

def speed_calc_decorator(function):
    def speed_time():
      start = time.time()
      function()
      end = time.time()
      run_time = end - start
      print(f"{function.__name__} ran in {run_time} seconds")
    return speed_time


@speed_calc_decorator
def fast_function():
    for i in range(10000000):
        i * i

@speed_calc_decorator
def slow_function():
    for i in range(100000000):
        i * i

fast_function()
slow_function()
