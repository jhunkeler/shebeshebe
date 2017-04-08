#!/usr/bin/env python
from __future__ import division
import time


def tps(samples):
    values = []
    x = 1000000
    for _ in range(samples):
        start = time.time()
        for i in range(x):
            pass
        stop = time.time() - start
    ops = 60 / (stop / 1)
    values.append(ops)
    return sum(values) / len(values)

def mps(samples):
    values = []
    barr = bytearray(1)
    x = 1000000

    for _ in range(samples):
        start = time.time()
        for i in range(x):
            barr[0] = 1
        stop = time.time() - start
    ops = 60 / (stop / 1)
    values.append(ops)
    return sum(values) / len(values)

def dps(samples, buffering=1):
    values = []
    barr = bytearray(1)
    x = 1000000

    with open('bloat.dat', 'wb+', buffering) as fp:
        for _ in range(samples):
            start = time.time()
            for i in range(x):
                fp.write(b'\0')
            stop = time.time() - start
            fp.seek(0, 0)
        ops = 60 / (stop / 1)
        values.append(ops)
    return sum(values) / len(values)


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--samples', '-s', default=100, type=int)
    args = parser.parse_args()

    t = int(tps(args.samples))
    print('cpu: {0} mHz'.format(t))

    m = int(mps(args.samples))
    print('ram: {0} mHz'.format(m))

    db = int(dps(args.samples))
    print('iop (buffered): {0}'.format(db))

    du = int(dps(args.samples, 0))
    print('iop (unbuffered): {0}'.format(du))




