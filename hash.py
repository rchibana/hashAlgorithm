__author__ = 'rchibana'

from node import Node

EMPTY = 0
REMOVED = 1
BUSY = 2


class Hash():

    hash_list = None
    table_size = 10

    def create_hash_list(self):
        """
        Create the hash table
        :return: return a list with nodes
        """

        hash = []
        for i in range(self.table_size):
            node = Node()
            node.state = EMPTY

            hash.append(node)

        self.hash_list = hash

    def hash_function(self, k, i):
        """
        Hash Algorithm
        :param k: represent the key
        :param i: collision counter
        :return: return the hash algorithm result
        """
        return (k+i) % self.table_size

    def insert(self, k):
        """
        Add a new element in the hash table
        :param k: the new element
        :return: True if the element find a
        """

        j, i = (0,) * 2

        while i < self.table_size:
            j = self.hash_function(k, i)
            node = self.hash_list[j]

            if node and node.state in [EMPTY, REMOVED]:
                node.data = k
                node.state = BUSY

                self.hash_list[j] = node

                return True

            else:
                i += 1

        return False

    def search(self, k, i):
        """
        Search method
        :param k: element to be searched
        :param i: colision counter
        :return: integer value
        """

        j = 0

        if i < self.table_size:
            j = self.hash_function(k, i)
            node = self.hash_list[j]
            if node.state == EMPTY:
                return -1
            elif node.state == REMOVED:
                return self.search(i+1)
            elif node.data == self.table_size:
                return j
            else:
                return self.search(i+1)

    def remove(self, k):
        """
        Remove method
        :param k: element to be removed
        :return:
        """

        i = self.search(k, 0)

        if i == -1:
            return -1
        else:
            self.hash_list[i].state = REMOVED
            return 1


if __name__ == '__main__':

    h = Hash()
    h.create_hash_list()
    h.insert(5)
    h.insert(7)
    h.remove(3)




