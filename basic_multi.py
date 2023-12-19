from multiprocessing import Process
import os


def work(identyfier):
    print(f"Cześć, jestem procesem " f"{identyfier}, pid: {os.getpid()}")


def main():
    processes = [Process(target=work, args=(number,)) for number in range(5)]
    for process in processes:
        process.start()
    while processes:
        processes.pop().join()


if __name__ == '__main__':
    main()
