class Node:
    def __init__(self, init_data):
        self.data = init_data
        self.next = None

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def set_data(self, new_data):
        self.data = new_data

    def set_next(self, new_next):
        self.next = new_next


class UnorderedList:
    def __init__(self):
        self.head: Node or None = None

    def is_empty(self):
        return self.head == None

    def add(self, item):
        tmp = Node(item)
        tmp.set_next(self.head)
        self.head = tmp

    def size(self):
        count = 0
        current = self.head
        while current != None:
            current = current.get_next()

            count += 1
        return count

    def search(self, item):
        current = self.head
        found = False
        while current != None and not found:
            if current.get_data() == item:
                found = True
            else:
                current = current.get_next()
        return found

    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while current != None and not found:
            if current.get_data() == item:
                found = True
                if previous == None:
                    self.head = current.get_next()
                else:
                    previous.set_next(current.get_next())
            else:
                previous = current
                current = current.get_next()

    def append(self, item):
        tmp = Node(item)
        current = self.head
        while current != None:
            current = current.get_next()
        if self.head:
            current.set_next(tmp)
        self.head = tmp

    def insert(self, index, item):
        tmp = Node(item)
        previous: Node or None = None
        current = self.head
        count = 0
        while index != count:
            previous = current
            current = current.get_next()
            count += 1
        previous.set_next(tmp)
        tmp.set_next(current)

    def pop(self, index=None):
        previous = None
        current = self.head
        while current != None:
            previous = current
            current = current.get_next()
        previous.set_next(None)


class OrderedList:
    def __init__(self):
        self.head = None

    def search(self, item):
        current = self.head
        found = False
        stop = False
        while current != None and not found and not stop:
            if current:
                if current.get_data() == item:
                    found = True
                elif current.get_data() > item:
                    stop = True
                else:
                    current = current.get_next()
        return found

    def add(self, item):
        previous = None
        current = self.head
        stop = False

        while current != None and not stop:
            if current.get_data > item:
                stop = True
            else:
                previous = current
                current = current.get_next()
        temp = Node(item)
        if current == None:
            self.head = temp
        elif previous == None:
            temp.set_next(current)
            self.head = temp
        else:
            temp.set_next(current)
            previous.set_next(temp)


l = list(range(1, 50, 3))


def binary_search(my_list, num):
    left = 0
    right = len(my_list) - 1

    found = False

    while left <= right and not found:
        middle = (left + right) // 2
        if num == my_list[middle]:
            found = True
        elif num > my_list[middle]:
            left += 1
        else:
            right -= 1
    return found


def binary_search_rec(my_list, item):
    if len(my_list) == 0:
        return False
    else:
        middle_point = len(my_list) // 2
        if item == my_list[middle_point]:
            return True
        elif item < my_list[middle_point]:
            return binary_search_rec(my_list[:middle_point], item)
        else:
            return binary_search_rec(my_list[middle_point + 1:], item)


from random import randint, random
from collections import namedtuple

Color = namedtuple('Color', "red green blue alpha")


def random_color():
    red = randint(0, 255)
    blue = randint(0, 255)
    green = randint(0, 255)
    alpha = round(random(), 2)
    return Color(red, green, blue, alpha)


def hash_(a_string, table_size):
    sum = 0
    for pos in range(len(a_string)):
        sum += ord(a_string[pos])
    return sum % table_size


def my_hash(some_string, table_size):
    sum = 0
    for pos in range(len(some_string)):
        sum += ord(some_string[pos]) * pos
    return sum % table_size


class HashTable:
    def __init__(self):
        self.size = 11
        self.slots = [None] * self.size
        self.data = [None] * self.size

    def put(self, key, data):
        hash_value = self.hash_function(key, len(self.slots))

        if self.slots[hash_value] == None:
            self.slots[hash_value] = key
            self.data[hash_value] = data
        else:
            if self.slots[hash_value] == key:
                self.data[hash_value] = data
            else:
                next_slot = self.rehash(hash_value, len(self.slots))
                while self.slots[next_slot] != None and self.slots[next_slot] != key:
                    next_slot = self.rehash(next_slot, len(self.slots))

                if self.slots[next_slot] == None:
                    self.slots[next_slot] = key
                    self.data[next_slot] = data
                else:
                    self.data[next_slot] = data

    def hash_function(selfself, key, size):
        return key % size

    def rehash(self, old_hash, size):
        return (old_hash+1) % size