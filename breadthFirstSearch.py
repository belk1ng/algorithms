from collections import deque

graph_bfs = {'me': ['alice', 'bob', 'claire'],
             'bob': ['anuj', 'peggy'],
             'alice': ['paggy'],
             'claire': ['tom', 'johny'],
             'anuj': [],
             'peggy': [],
             'tom': [],
             'johny': []
             }


def breadth_firstSearch(name):
    search = deque()
    search += graph_bfs[name]
    searched = []

    while search:
        person = search.popleft()
        if not person in searched:
            if person[-1] == 'y':  # any condition here
                return f'{person.title()} is a mango seller'
            else:
                search += graph_bfs[person]
                searched.append(person)
    return False


# Another option
def search_name(graph, start):
    distances = {start: 0}
    q = deque([start])
    while q:
        current = q.popleft()
        for neighbour in graph[current]:
            if neighbour not in distances:
                distances[neighbour] = distances[current] + 1
                q.append(neighbour)
    return distances

