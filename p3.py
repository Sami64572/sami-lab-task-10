class ReverseIterator:
    def __init__(self, iterable):
        self.iterable = iterable
        self.index = len(iterable)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index > 0:
            self.index -= 1
            return self.iterable[self.index]
        raise StopIteration

strings_list = ["apple", "banana", "cherry", "date"]

reverse_iterator = ReverseIterator(strings_list)

for reversed_string in reverse_iterator:
    print(reversed_string)