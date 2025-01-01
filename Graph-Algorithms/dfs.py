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

def dfs(start_node):
    """
    Perform DFS starting from a given node using the global adjacency list.
    
    :param start_node: The starting node for DFS.
    :return: A list of nodes visited in DFS order.
    """

    if adj is None:
        raise ValueError("Adjacency list is not set. Use set_adj() to set the adjacency list.")
    
    visited = [False] * (nodes + 1)
    dfs_order = []

    def __dfs(node):
        visited[node] = True
        dfs_order.append(node)
        for neighbor, _ in adj[node]:
            if not visited[neighbor]:
                __dfs(neighbor)

    if start_node <= 0 or start_node > nodes:
        raise ValueError(f"Start node must be between 1 and {nodes}, inclusive.")

    __dfs(start_node)
    return dfs_order