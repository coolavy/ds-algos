"""
Simple construction of adjacency list. You can use it to store,

Unweighted tree.
Unweighted graph.
Weighted graph.
Weighted tree.

And others.

WARNING: You cannot add a new node, all the nodes will be defined when initalizing AdjList.
"""

class AdjList:
    def __init__(self, number_of_nodes: int):
        """
        Initialization of adjacency list.

        :param number_of_nodes: Number of nodes in the graph.
        """
        if not isinstance(number_of_nodes, int):
            raise ValueError("Number of nodes in the graph must be a positive integer.")
        if number_of_nodes <= 0:
            raise ValueError("Number of nodes must be greater than zero.")

        self.nodes = number_of_nodes
        self.adj = [[] for _ in range(self.nodes + 1)]  # Create adjacency list
        self.non_one_weight = False
        self.negative_weight = False

    def add_edge(self, node1: int, node2: int, one_directional: bool = False, weight: float = 1.0):
        """
        Adds an edge to the graph.

        :param node1: First node.
        :param node2: Second node.
        :param one_directional: If True, creates a one-directional edge. Default is False (bi-directional).
        :param weight: Weight of the edge. Default is 1.0.
        """

        if not isinstance(node1, int) or not isinstance(node2, int):
            raise ValueError("Both nodes must be integers.")
        
        if not (1 <= node1 <= self.nodes) or not (1 <= node2 <= self.nodes):
            raise ValueError(f"Both nodes must be between 1 and {self.nodes}, inclusive.")
        
        if not isinstance(weight, (int, float)):
            raise ValueError("The weight of an edge must be a numerical value (int or float).")

        if weight != 1:
            self.non_one_weight = True
        if weight < 0:
            self.negative_weight = True

        self.adj[node1].append((node2, weight))
        if not one_directional:
            self.adj[node2].append((node1, weight))

    def get_neighbors(self, node: int) -> list:
        """
        Retrieves the neighbors of a given node.

        :param node: Node whose neighbors are to be retrieved.
        :return: List of tuples (neighbor, weight).
        """

        if not (1 <= node <= self.nodes):
            raise ValueError(f"Node must be between 1 and {self.nodes}, inclusive.")
        
        return self.adj[node]

    def stringadj(self) -> str:
        """
        String representation of the adjacency list.

        :return: Adjacency list as a string.
        """

        return "\n".join(f"{i}: {neighbors}" for i, neighbors in enumerate(self.adj) if neighbors)