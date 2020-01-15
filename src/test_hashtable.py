import unittest

from hashtable import HashTable


class TestHashTable(unittest.TestCase):

    def test_hash_table_insertion_and_retrieval(self):
        ht = HashTable(8)

        ht.insert("key-0", "val-0")
        ht.insert("key-1", "val-1")
        ht.insert("key-2", "val-2")
        ht.insert("key-3", "val-3")
        ht.insert("key-4", "val-4")
        ht.insert("key-5", "val-5")
        ht.insert("key-6", "val-6")
        ht.insert("key-7", "val-7")
        ht.insert("key-8", "val-8")
        ht.insert("key-9", "val-9")

        return_value = ht.retrieve("key-0")
        self.assertTrue(return_value == "val-0")
        return_value = ht.retrieve("key-1")
        self.assertTrue(return_value == "val-1")
        return_value = ht.retrieve("key-2")
        self.assertTrue(return_value == "val-2")
        return_value = ht.retrieve("key-3")
        self.assertTrue(return_value == "val-3")
        return_value = ht.retrieve("key-4")
        self.assertTrue(return_value == "val-4")
        return_value = ht.retrieve("key-5")
        self.assertTrue(return_value == "val-5")
        return_value = ht.retrieve("key-6")
        self.assertTrue(return_value == "val-6")
        return_value = ht.retrieve("key-7")
        self.assertTrue(return_value == "val-7")
        return_value = ht.retrieve("key-8")
        self.assertTrue(return_value == "val-8")
        return_value = ht.retrieve("key-9")
        self.assertTrue(return_value == "val-9")

    def test_hash_table_insertion_overwrites_correctly(self):
        ht = HashTable(8)

        ht.insert("key-0", "val-0")
        ht.insert("key-1", "val-1")
        ht.insert("key-2", "val-2")
        ht.insert("key-3", "val-3")
        ht.insert("key-4", "val-4")
        ht.insert("key-5", "val-5")
        ht.insert("key-6", "val-6")
        ht.insert("key-7", "val-7")
        ht.insert("key-8", "val-8")
        ht.insert("key-9", "val-9")

        ht.insert("key-0", "new-val-0")
        ht.insert("key-1", "new-val-1")
        ht.insert("key-2", "new-val-2")
        ht.insert("key-3", "new-val-3")
        ht.insert("key-4", "new-val-4")
        ht.insert("key-5", "new-val-5")
        ht.insert("key-6", "new-val-6")
        ht.insert("key-7", "new-val-7")
        ht.insert("key-8", "new-val-8")
        ht.insert("key-9", "new-val-9")

        return_value = ht.retrieve("key-0")
        self.assertTrue(return_value == "new-val-0")
        return_value = ht.retrieve("key-1")
        self.assertTrue(return_value == "new-val-1")
        return_value = ht.retrieve("key-2")
        self.assertTrue(return_value == "new-val-2")
        return_value = ht.retrieve("key-3")
        self.assertTrue(return_value == "new-val-3")
        return_value = ht.retrieve("key-4")
        self.assertTrue(return_value == "new-val-4")
        return_value = ht.retrieve("key-5")
        self.assertTrue(return_value == "new-val-5")
        return_value = ht.retrieve("key-6")
        self.assertTrue(return_value == "new-val-6")
        return_value = ht.retrieve("key-7")
        self.assertTrue(return_value == "new-val-7")
        return_value = ht.retrieve("key-8")
        self.assertTrue(return_value == "new-val-8")
        return_value = ht.retrieve("key-9")
        self.assertTrue(return_value == "new-val-9")

    def test_hash_table_removes_correctly(self):
        ht = HashTable(8)

        ht.insert("key-0", "val-0")
        ht.insert("key-1", "val-1")
        ht.insert("key-2", "val-2")
        ht.insert("key-3", "val-3")
        ht.insert("key-4", "val-4")
        ht.insert("key-5", "val-5")
        ht.insert("key-6", "val-6")
        ht.insert("key-7", "val-7")
        ht.insert("key-8", "val-8")
        ht.insert("key-9", "val-9")

        return_value = ht.retrieve("key-0")
        self.assertTrue(return_value == "val-0")
        return_value = ht.retrieve("key-1")
        self.assertTrue(return_value == "val-1")
        return_value = ht.retrieve("key-2")
        self.assertTrue(return_value == "val-2")
        return_value = ht.retrieve("key-3")
        self.assertTrue(return_value == "val-3")
        return_value = ht.retrieve("key-4")
        self.assertTrue(return_value == "val-4")
        return_value = ht.retrieve("key-5")
        self.assertTrue(return_value == "val-5")
        return_value = ht.retrieve("key-6")
        self.assertTrue(return_value == "val-6")
        return_value = ht.retrieve("key-7")
        self.assertTrue(return_value == "val-7")
        return_value = ht.retrieve("key-8")
        self.assertTrue(return_value == "val-8")
        return_value = ht.retrieve("key-9")
        self.assertTrue(return_value == "val-9")

        ht.remove("key-9")
        ht.remove("key-8")
        ht.remove("key-7")
        ht.remove("key-6")
        ht.remove("key-5")
        ht.remove("key-4")
        ht.remove("key-3")
        ht.remove("key-2")
        ht.remove("key-1")
        ht.remove("key-0")

        return_value = ht.retrieve("key-0")
        self.assertTrue(return_value is None)
        return_value = ht.retrieve("key-1")
        self.assertTrue(return_value is None)
        return_value = ht.retrieve("key-2")
        self.assertTrue(return_value is None)
        return_value = ht.retrieve("key-3")
        self.assertTrue(return_value is None)
        return_value = ht.retrieve("key-4")
        self.assertTrue(return_value is None)
        return_value = ht.retrieve("key-5")
        self.assertTrue(return_value is None)
        return_value = ht.retrieve("key-6")
        self.assertTrue(return_value is None)
        return_value = ht.retrieve("key-7")
        self.assertTrue(return_value is None)
        return_value = ht.retrieve("key-8")
        self.assertTrue(return_value is None)
        return_value = ht.retrieve("key-9")
        self.assertTrue(return_value is None)

    def test_hash_table_resize(self):
        print("------RESIZE TEST-------")
        ht = HashTable(8)

        ht.insert("key-0", "val-0")
        ht.insert("key-1", "val-1")
        ht.insert("key-2", "val-2")
        ht.insert("key-3", "val-3")
        ht.insert("key-4", "val-4")
        ht.insert("key-5", "val-5")
        ht.insert("key-6", "val-6")
        ht.insert("key-7", "val-7")
        ht.insert("key-8", "val-8")
        ht.insert("key-9", "val-9")

        self.assertTrue(len(ht.storage) == 16)

        ht.remove("key-3")
        ht.remove("key-4")
        ht.remove("key-5")
        ht.remove("key-6")
        ht.remove("key-7")
        ht.remove("key-8")
        ht.remove("key-9")

        self.assertTrue(len(ht.storage) == 8)

        ht.insert("key-3", "val-3")
        ht.insert("key-4", "val-4")
        ht.insert("key-5", "val-5")
        ht.insert("key-6", "val-6")
        ht.insert("key-7", "val-7")
        ht.insert("key-8", "val-8")
        ht.insert("key-9", "val-9")

        self.assertTrue(len(ht.storage) == 16)

        return_value = ht.retrieve("key-0")
        self.assertTrue(return_value == "val-0")
        return_value = ht.retrieve("key-1")
        self.assertTrue(return_value == "val-1")
        return_value = ht.retrieve("key-2")
        self.assertTrue(return_value == "val-2")
        return_value = ht.retrieve("key-3")
        self.assertTrue(return_value == "val-3")
        return_value = ht.retrieve("key-4")
        self.assertTrue(return_value == "val-4")
        return_value = ht.retrieve("key-5")
        self.assertTrue(return_value == "val-5")
        return_value = ht.retrieve("key-6")
        self.assertTrue(return_value == "val-6")
        return_value = ht.retrieve("key-7")
        self.assertTrue(return_value == "val-7")
        return_value = ht.retrieve("key-8")
        self.assertTrue(return_value == "val-8")
        return_value = ht.retrieve("key-9")
        self.assertTrue(return_value == "val-9")


if __name__ == '__main__':
    unittest.main()
