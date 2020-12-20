class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = [None] * capacity
        self.oldest = -1

    def append(self, value):
        self.oldest = (self.oldest + 1) % self.capacity
        self.storage[self.oldest] = value

    def get(self):
        return [element for element in self.storage if element is not None]
