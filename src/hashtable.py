# '''
# Linked List hash table key/value pair
# '''


class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''

    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity
        self.original_capacity = capacity
        self.keys = 0

    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        return hash(key)

    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        '''
        hash = 5381
        for c in key:
            hash = (hash * 33) + ord(c)
        return hash

    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash_djb2(key) % self.capacity

    def insert(self, key, value):
        '''
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Fill this in.
        '''
        # hash the key to get an index
        index = self._hash_mod(key)
        current = self.storage[index]

        while current:
            if current.key == key:
                current.value = value
                return
            elif current.next:
                current = current.next
            else:
                current.next = LinkedPair(key, value)
                self.keys += 1
                self.resize()
                return

        self.storage[index] = LinkedPair(key, value)
        self.keys += 1
        self.resize()

    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        index = self._hash_mod(key)
        current = self.storage[index]

        if current.key == key:
            self.storage[index] = current.next
            self.keys -= 1
            self.resize()
            return

        while current:
            prev = current
            current = current.next
            if current.key == key:
                prev.next = current.next
                self.keys -= 1
                self.resize()
            return

        print("Key was not found")

    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        index = self._hash_mod(key)
        current = self.storage[index]

        if current:
            while current:
                if current.key == key:
                    return current.value
                else:
                    current = current.next
        else:
            return None

    def get_load_factor(self):

        load_factor = self.keys / self.capacity
        return load_factor

    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        load_factor = self.get_load_factor()

        # if load factor past 0.7
        if load_factor > 0.7:
            print("> 0.7", load_factor)
            self.capacity *= 2
            old_storage = self.storage
            self.storage = [None] * self.capacity

            for item in old_storage:
                while item:
                    # using insert method takes care of hashing
                    self.insert(item.key, item.value)
                    item = item.next
            print("storage length", len(self.storage), "keys", self.keys)

        elif load_factor < 0.2 and (self.original_capacity < self.capacity):
            print("< 0.2", load_factor)
            self.capacity //= 2
            old_storage = self.storage
            self.storage = [None] * self.capacity

            for item in old_storage:
                while item:
                    self.insert(item.key, item.value)
                    item = item.next
            print("storage length", len(self.storage), "keys", self.keys)

        else:
            print("No need to resize", load_factor)


if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")
