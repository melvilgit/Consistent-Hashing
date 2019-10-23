from consistentHashing import ConsistentHashing
import random
import string
import unittest

def randomString(stringLength=10):
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))


class ConsistentHashingtest(unittest.TestCase):
    def testStandardDeviation(self):
        obj = ConsistentHashing()
        noOfKeys = 1000
        noOfNodes = 100
        nodes = ["node{}".format(i) for i in range(0, noOfNodes)]
        obj.set_nodes(nodes)
        distributions = {}
        for i in range(noOfKeys):
            s = randomString()
            node = obj.get_node(s)
            distributions[node] = distributions.get(node,0)+1
        self.assertEquals(sum(distributions.values()), noOfKeys)

if __name__ == '__main__':
    unittest.main()