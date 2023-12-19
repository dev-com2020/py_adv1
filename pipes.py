from multiprocessing import Process, Pipe


class CustomClass:
    pass


def worker(connection):
    while True:
        instance = connection.recv()
        if instance:
            print(f"CHLD: recv: {instance}")
        if instance is None:
            break


def main():
    parent_conn, child_conn = Pipe()
    child = Process(target=worker, args=(child_conn,))

    for item in (
            42,
            "jakiś string",
            {"jeden": 1},
            CustomClass(),
            None,
    ):
        print(f"PRINT: send: {item}")
        parent_conn.send(item)

    child.start()
    child.join()


if __name__ == '__main__':
    main()
