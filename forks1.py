import os

pid_list = []

def main():
    pid_list.append(os.getpid())
    child_pid = os.fork()

    if child_pid == 0:
        pid_list.append(os.getpid())
        print()
        print("CHILD: jestem procesem dzieckiem")
        print("CHILD: wszystkie pidy jakie znam to %s: " % pid_list)
    else:
        pid_list.append(os.getpid())
        print()
        print("PARENT: jestem rodziciem")
        print("PARENT: pid dziecka %d" % child_pid)
        print("PARENT: wszystkie pidy jakie znam to: %s" % pid_list)

if __name__ == '__main__':
    main()