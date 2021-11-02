import string
import multiprocessing as mp
from hashlib import sha256
import itertools
import time

alphabet = string.ascii_lowercase
with open("sha.txt") as file:
    array = [row.strip() for row in file]


def calculation(first_bits):
    name_proc = mp.current_process().name
    for i in itertools.product(first_bits, alphabet, alphabet, alphabet, alphabet):
        if sha256(''.join(i).encode('utf-8')).hexdigest() in array:
            print(name_proc)
            print(f'Password for the hash function ' + sha256(''.join(i).encode('utf-8')).hexdigest() + ' - ' + ''.join(i))


def inputNumber():
    while True:
        try:
            n = int(input("Specify the number of threads in the range from 1 to 26: "))
        except ValueError:
            print("You didn't enter a number. Try again.")
        else:
            if n >= 1 and n <= 26:
                return n
            print("The entered number is out of range: [%d, %d)" % (1, 26))


if __name__ == "__main__":
    number_of_processes = []
    number_of_parts = inputNumber()
    partition_size = len(alphabet) // number_of_parts
    start = time.perf_counter()
    for i in range(number_of_parts):
        if i == number_of_parts - 1:
            first_bit = alphabet[partition_size * i:]
        else:
            first_bit = alphabet[partition_size * i: partition_size * (i + 1)]
        p = mp.Process(target=calculation, args=(first_bit,))
        number_of_processes.append(p)
        p.start()
    [proc.join() for proc in number_of_processes]
    stop = time.perf_counter()
    print(f"The calculation took {stop - start:0.4f} seconds, used {number_of_parts} streams")