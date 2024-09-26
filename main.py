import collections

def bfs(graph,root):

    visited, queue = set(), collections.deque([root])
    visited.add(root)

    while queue:

        vertex = queue.popleft()
        print(str(vertex) + " ", end=" ")

        if vertex == 11:
            break

        for neighbour in graph[vertex]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)

if __name__ == '__main__':
    graph = {1: [2,3], 2: [4,5], 3: [6,7], 4: [8,9], 5: [10,11], 6: [12,13], 7: [14,15], 8:[], 9:[], 10:[],11:[], 12:[], 13:[], 14:[], 15:[]}
    print("Following is Breadth First Traversal: ")
    bfs(graph, 1)