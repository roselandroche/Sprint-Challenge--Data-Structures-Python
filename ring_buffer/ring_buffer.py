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
        # adds given element to buffer if there is space
        if self.capacity > self.length:
            self.length += 1
            self.storage.append(item)
            self.oldest += 1
        # if no space, rewrite oldest item to new item
        elif self.capacity == self.length:
            self.storage[self.oldest - 1] = item
            if self.oldest == self.capacity:
                self.oldest = 1
            else:
                self.oldest += 1

    def get(self):
        # returns all elements in buffer in a list
            # in their given order
        # DO NOT RETURN ANY NONE VALUES
        output = []
        for item in range(self.length):
            if self.storage[item] != None:
                output += [self.storage[item]]
        print(output)
        return output

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