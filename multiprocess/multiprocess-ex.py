import multiprocessing
import time

start = time.perf_counter()


def do_something(times):
    print(f'Execution {times} times')
    resp = 0
    for i in range(0, times):
        resp = resp + i
    print(resp)


processes = []

if __name__ == '__main__':
    for _ in range(5):
        p = multiprocessing.Process(target=do_something, args=[100000000])
        p.start()
        processes.append(p)

    for process in processes:
        process.join()

    finish = time.perf_counter()

    print(f'Finished in {round(finish - start, 2)} second(s)')
