import bisect
import math
import hashlib
import random
import string
import md5


class ConsistentHashing(object):
    """ Consistent hashing algorith , We used python bisect
        (https://docs.python.org/2/library/bisect.html)
        to find index of an element to be added in a sorted list """

    def __init__(self):
        self.nodes = {}
        self.keys = []

    def randomString(stringLength=10):
        """Function to generate random string
        (we assume the randome string are hostname ) """
        letters = string.ascii_lowercase
        return ''.join(random.choice(letters) for i in range(stringLength))

    def create_hash(self, s):
        """ Generic hash function to hash a hostname to a hash value """
        # return long(md5.md5(s).hexdigest(), 16)
        return int(hashlib.md5(s.encode()).hexdigest(), 16)

    def set_nodes(self, nodes):
        """ Function does 2 things
            1) Create node hash and add to nodes ({"hashxxxx":node1..})
            2) Append the node_hash to key list """
        for node in nodes:
            node_hash = self.create_hash(node)
            self.nodes[node_hash] = node
            bisect.insort(self.keys, node_hash)

    def get_item(self, item):
        """ select a host from the list by finding the index
            of item to be inserted into sorted list """
        start = bisect.bisect(self.keys, self.create_hash(item))
        if start == len(self.keys):
            start = 0
        return self.nodes[self.keys[start]]


nodes = ["node{}".format(i) for i in range(0, 10)]
obj = ConsistentHashing()
obj.set_nodes(nodes)
print obj.get_item("test1")
print obj.get_item("test2")
total = {}
"""
for i in range(0, 100):
    s = randomString()

    node = obj.get_item(s)
    total[node] = total.get(node, 0) + 1
print _pop_std_dev(total.values())
print total
"""