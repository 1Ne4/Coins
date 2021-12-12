from hashlib import md5
from random import choice
import concurrent.futures


def get_coin(i):
    counter = 0
    while counter < i:
        s = "".join([choice("0123456789") for i in range(50)])
        h = md5(s.encode('utf8')).hexdigest()

        if h.endswith("00000"):
            print(s, h)
            counter += 1


def main():
    with concurrent.futures.ProcessPoolExecutor(max_workers=4) as executor:
        executor.submit(get_coin, 1)
        executor.submit(get_coin, 1)
        executor.submit(get_coin, 1)
        executor.submit(get_coin, 1)


if __name__ == '__main__':
    main()
