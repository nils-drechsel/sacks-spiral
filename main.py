from sieve import Sieve
from sacks_spiral import Spiral
from hex import hex_histogram

# number range to explore for primes
n = 500000

# create spiral that is n units long
sp = Spiral(1, n)
d = sp.estimate_max_radius(n) * 2
h = hex_histogram(d, d,400)
s = Sieve(n)

# bin every prime on the spiral into a hexagonal bins
for i in range(0, n):
    if s.isPrime(i):
        h.bin(sp.get_coordinate(i))


h.make_svg("sacks.svg")
