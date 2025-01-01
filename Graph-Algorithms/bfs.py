from errors import *
from collections import deque
from adjlist import AdjList

adj = None
nodes = 0

def set_adj(adj_list):
    """
    Set the global adjacency list from the given AdjList instance.
    
    :param adj_list: An instance of the AdjList class.
    """

    global adj, nodes
    if not isinstance(adj_list, AdjList):
        raise TypeError("The adjacency list must be an instance of AdjList.")
    
    adj = adj_list.adj
    nodes = adj_list.nodes

def bfs(start_node):
    """
    Perform BFS starting from a given node using the global adjacency list.
    
    :param start_node: The starting node for BFS.
    :return: A list of nodes visited in BFS order.
    """

    if adj is None:
        raise ValueError("Adjacency list is not set. Use set_adj() to set the adjacency list.")

    visited = [False] * (nodes + 1)
    result = []
    queue = deque()

    if start_node <= 0 or start_node > nodes:
        raise ValueError(f"Start node must be between 1 and {nodes}, inclusive.")

    queue.append(start_node)
    visited[start_node] = True

    while queue:
        current = queue.popleft()
        result.append(current)
        
        for neighbor, _ in adj[current]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)

    return result
