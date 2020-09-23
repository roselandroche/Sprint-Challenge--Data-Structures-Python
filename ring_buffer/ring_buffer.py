class RingBuffer():
    def __init__(self, capacity):
        # capacity is fixed
        # when capacity is reached, oldest element
            # is overwritten by new element
        self.capacity = capacity
        self.storage = []
        self.length = 0
        self.oldest = 0

    def append(self, item):
        if self.oldest is self.capacity:
            self.oldest = 0
        if len(self.storage) <= self.oldest:
            self.storage.append(item)
        else:
            self.storage[self.oldest] = item
        self.oldest += 1

    def get(self):
        return self.storage

example = RingBuffer(3)
example.append(1)
example.append(2)
example.append(3)
example.get()

example.append(4)
example.append(5)
example.append(6)
example.get()

example.append(None)
example.append(7)
example.append(8)
example.get()