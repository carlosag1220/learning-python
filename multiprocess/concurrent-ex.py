import concurrent.futures
import time

start = time.perf_counter()


def do_something(times):
    print(f'Execution {times} times')
    resp = 0
    for i in range(0, times):
        resp = resp + i
    return resp


processes = []

if __name__ == '__main__':

    # Executing one by one
    with concurrent.futures.ProcessPoolExecutor() as executor:
        f1 = executor.submit(do_something, 100000000)
        f2 = executor.submit(do_something, 100000000)
        f3 = executor.submit(do_something, 100000000)
        f4 = executor.submit(do_something, 100000000)
        f5 = executor.submit(do_something, 100000000)

        print(f1.result())
        print(f2.result())
        print(f3.result())
        print(f4.result())
        print(f5.result())

    finish = time.perf_counter()
    print(f'Finished in {round(finish - start, 2)} second(s)')
    start = time.perf_counter()

    # Executing with List Comprehensions
    with concurrent.futures.ProcessPoolExecutor() as executor:
        results = [executor.submit(do_something, 100000000) for _ in range(5)]
    for f in concurrent.futures.as_completed(results):
        print(f.result())

    finish = time.perf_counter()
    print(f'Finished in {round(finish - start, 2)} second(s)')
    start = time.perf_counter()

    # Executing with List Comprehensions and list of params
    with concurrent.futures.ProcessPoolExecutor() as executor:
        times = [60000000,70000000,80000000,90000000,100000000]
        results = [executor.submit(do_something, time) for time in times]
    # return the results in the order that they finish
    for f in concurrent.futures.as_completed(results):
        print(f.result())

    finish = time.perf_counter()
    print(f'Finished in {round(finish - start, 2)} second(s)')
    start = time.perf_counter()

    # return the results in the order that they were started
    # you can change ProcessPoolExecutor and put ThreadPoolExecutor
    with concurrent.futures.ProcessPoolExecutor() as executor:
        times = [60000000, 70000000, 80000000, 90000000, 100000000]
        results = executor.map(do_something, times)

    # It's optional; concurrent automatically join the process
    for result in results:
        # Handle exceptions here
        print(result)

    finish = time.perf_counter()

    print(f'Finished in {round(finish - start, 2)} second(s)')
