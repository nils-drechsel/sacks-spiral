from sieve import Sieve
import math

class Spiral:

    """
    Represents an Archimedean spiral 
    """

    def __init__(self, r, n):
        self.r = r
        self.offset = self.estimate_max_radius(n)

    def estimate_max_radius(self, x):
        i = math.floor(math.sqrt(x))
        return self.r * (i+1)

    def get_coordinate(self, x):
        """
        Given a distance from the origin, returns the x,y coordinates of that point
        """
        i = math.floor(math.sqrt(x))
        start = i * i
        end = (i + 1) * (i + 1)
        n = end - start
        step = 2 * math.pi / n
        j = x - start
        t = j * step
        s = self.r * i + t / (2 * math.pi)
        return [self.offset + s * math.cos(t), self.offset + s * math.sin(t)]
