from bitarray import bitarray


class Sieve:

    """
    A simple sieve to obtain prime numbers
    """

    def __init__(self, n):
        self.n = n
        self.s = bitarray(n)
        self.s.setall(False)
        self.find_primes()

    def find_primes(self):
        for i in range(2, self.n):
            if not self.s[i]:
                #self.primes.append(i)
                self.fill(i)

    def fill(self, j):
        i = j + j

        while i < self.n:
            self.s[i] = True
            i += j

    def isPrime(self, i):
        return not self.s[i]
