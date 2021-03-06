def kahn(adj):
    """Kahn topological sort: pull out all vertices without incoming edges
    until there are no more vertices.
    Input: adj is an adjacency matrix [0..n-1][0..n-1] for a DAG,
            such that adj[i][i] has the weight of an edge from i to k.
    Output: list of vertices in a topological order
    >>> kahn([[0,1],\
              [0,0]])   # 0 --> 1
    [0, 1]
    >>> kahn([[0,0,0],\     # 0 points nowhere
              [1,0,1],\     # 1 points to 0 and to 2
              [1,0,0]])     # 1 --> 2 --> 0 <-- 1
    [1, 2, 0]
    """

    n = len(adj)
    # fill in the diagonal [i][i] with the number of incoming edges for vertex i
    for i in range(n):
        incoming = 0
        for k in range(n):
            incoming += adj[k][i]
        adj[i][i] = incoming

    # now take out any vertices that have no incoming edges,
    # repeating until there are no more vertices
    out = []
    while len(out) < n:
        # in the following loop, since the graph is acyclic,
        # we are guaranteed to pick up at least one vertex
        for i in range(n):
            # if vertex i has no incoming edges, remove it from the graph
            if adj[i][i] == 0:
                out.append(i)
                for k in range(n):
                    adj[k][k] -= adj[i][k]  # remove each edge from tally in adj[k][k]
                    adj[i][k] = 0     # remove each edge from adjacency array
                adj[i][i] = -1      # adj[i][i] == -1 means vertex i no longer is in the graph

    return out
