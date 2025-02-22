
class random_number_generator():
    def __init__(self, seed):
        self.multiplier = 24693
        self.increment = 3517
        self.modulus = 2**17
        self.seed = seed | 1000

    def next(self):
        self.seed = (self.seed * self.multiplier + self.increment) % self.modulus
        return self.seed / self.modulus

    def random(self, n):
        return [self.next() for _ in range(n)]