from errors import *

class ProdSegTree:
    def __init__(self, size, array=None):
        """
        Initializes the segment tree.

        :param size: The size of the array for the segment tree.
        :param array: The array from which the segment tree is built (optional).
        """
        if not isinstance(size, int) or size <= 0:
            raise ValueError(f"Size must be a positive integer, got {size}.")

        self.size = size
        self.DEFAULT_NUMBER = 1 # Can change from type-to-type
        self.tree = [self.DEFAULT_NUMBER] * (4 * self.size)
        self.bottom_layer = [self.DEFAULT_NUMBER] * self.size
        self.MOD = -1 

        if array is not None:
            if len(array) != self.size:
                raise ArraySizeError(f"Array length ({len(array)}) does not match segment tree size ({self.size}).")
            
            if not all(isinstance(x, (int, float)) for x in array):
                raise TypeError("All elements of the array must be numerical (int or float).")

            self.build_tree(array)

    def set_mod(self, mod):
        """
        Sets modulo for all queries.

        :param mod: Modulo for all queries.
        """

        self.MOD = mod

    def combine(self, node1, node2):
        """
        Combines two nodes (product for this tree).

        :param node1: First node.
        :param node2: Second node.
        """

        def func(a, b): # Can change from type-to-type.
            """
            How the nodes are going to be combined (addition, product, gcd, etc.)

            :param a: First node to be combined.
            :param b: Second node to be combined.
            """

            return a * b

        if self.MOD == -1:
            return func(node1, node2)
        else:
            return (func((node1 % self.MOD), (node2 % self.MOD))) % self.MOD

    def __build(self, array, node, start, end):
        if start == end:
            self.tree[node] = array[start - 1]
        else:
            mid = (start + end) // 2
            left_child = 2 * node
            right_child = 2 * node + 1

            self.__build(array, left_child, start, mid)
            self.__build(array, right_child, mid + 1, end)

            self.tree[node] = self.combine(self.tree[left_child], self.tree[right_child])

    def build_tree(self, array):
        """
        Builds the segment tree recursively (root is 1).

        :param array: The input array (0-indexed).
        """
        if not array:
            raise EmptyArrayError("The input array is empty.")
        if len(array) != self.size:
            raise ArraySizeError(f"Array length ({len(array)}) does not match segment tree size ({self.size}).")

        self.bottom_layer = array
        self.__build(array, 1, 1, self.size)

    def __update(self, index, new_value, node, start, end):
        if start == end:
            self.tree[node] = new_value
        else:
            mid = (start + end) // 2
            left_child = 2 * node
            right_child = 2 * node + 1

            if start <= index <= mid:
                self.__update(index, new_value, left_child, start, mid)
            else:
                self.__update(index, new_value, right_child, mid + 1, end)

            self.tree[node] = self.combine(self.tree[left_child], self.tree[right_child])

    def update(self, index, new_value):
        """
        Updates a certain index to a new value.

        :param index: Index of the value to update (1-indexed).
        :param new_value: Updated value of the node.
        """
        if not (1 <= index <= self.size):
            raise OutOfBoundsError(
                f"Index {index} is out-of-bounds, must be between 1 and {self.size}."
            )
        if not isinstance(new_value, (int, float)):
            raise TypeError("The updated value must be numerical (int or float).")

        self.bottom_layer[index - 1] = new_value
        self.__update(index, new_value, 1, 1, self.size)

    def __query(self, left_bound, right_bound, node, start, end):
        if end < left_bound or start > right_bound:
            return self.DEFAULT_NUMBER
        if left_bound <= start and right_bound >= end:
            return self.tree[node]

        mid = (start + end) // 2
        left_query = self.__query(left_bound, right_bound, 2 * node, start, mid)
        right_query = self.__query(left_bound, right_bound, 2 * node + 1, mid + 1, end)

        return self.combine(left_query, right_query)

    def query(self, left_bound, right_bound):
        """
        Find the product between a range [l, r].

        :param left_bound: Left border of the query range (1-indexed).
        :param right_bound: Right border of the query range (1-indexed).
        """
        if not (1 <= left_bound <= self.size and 1 <= right_bound <= self.size):
            raise InvalidBorderError(
                f"Query bounds must be between 1 and {self.size}."
            )
        if left_bound > right_bound:
            raise InvalidRangeError("Left bound must be less than or equal to right bound.")

        return self.__query(left_bound, right_bound, 1, 1, self.size)

    def print_bottom_layer(self):
        print(f"Bottom Layer: {self.bottom_layer}")