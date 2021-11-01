from __future__ import annotations

from typing import Protocol, Dict, List, Iterator, Tuple, TypeVar, Optional

T = TypeVar('T')

Location = TypeVar('Location')


class Graph(Protocol):
    def neighbors(self, id: Location) -> List[Location]: pass


class SimpleGraph:
    def __init__(self):
        self.edges: Dict[Location, List[Location]] = {}

    def neighbors(self, id: Location) -> List[Location]:
        return self.edges[id]


import collections


class Queue:
    def __init__(self):
        self.elements = collections.deque()

    def empty(self) -> bool:
        return not self.elements

    def put(self, x: T):
        self.elements.append(x)

    def get(self) -> T:
        return self.elements.popleft()


def breadth_first_search(graph: Graph, start: Location, goal: Location):
    frontier = Queue()
    frontier.put(start)
    came_from: Dict[Location, Optional[Location]] = {}
    came_from[start] = None

    while not frontier.empty():
        current: Location = frontier.get()
        if current == goal:
            break

        for next in graph.neighbors(current):
            if next not in came_from:
                frontier.put(next)
                came_from[next] = current

    return came_from


GridLocation = Tuple[int, int]


# -------------------------------------------------------------------------
class SquareGrid:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.walls: List[GridLocation] = []

    def in_bounds(self, id: GridLocation) -> bool:
        (x, y) = id
        return 0 <= x < self.width and 0 <= y < self.height

    def passable(self, id: GridLocation) -> bool:
        return id not in self.walls

    def neighbors(self, id: GridLocation) -> Iterator[GridLocation]:
        (x, y) = id
        neighbors = [(x + 1, y), (x - 1, y), (x, y - 1), (x, y + 1)]  # E W N S
        # see "Ugly paths" section for an explanation:
        if (x + y) % 2 == 0: neighbors.reverse()  # S N W E
        results = filter(self.in_bounds, neighbors)
        results = filter(self.passable, results)
        return results


def draw_tile(graph, id, style):
    r = " . "
    if 'number' in style and id in style['number']: r = " %-2d" % style['number'][id]
    if 'point_to' in style and style['point_to'].get(id, None) is not None:
        (x1, y1) = id
        (x2, y2) = style['point_to'][id]
        if x2 == x1 + 1: r = " > "
        if x2 == x1 - 1: r = " < "
        if y2 == y1 + 1: r = " v "
        if y2 == y1 - 1: r = " ^ "
    if 'path' in style and id in style['path']:   r = " @ "
    if 'start' in style and id == style['start']: r = " A "
    if 'goal' in style and id == style['goal']:   r = " Z "
    if id in graph.walls: r = "###"
    return r


def draw_grid(graph, **style):
    print("___" * graph.width)
    for y in range(graph.height):
        for x in range(graph.width):
            print("%s" % draw_tile(graph, (x, y), style), end="")
        print()
    print("~~~" * graph.width)
#----------------------------------------------------------------------------------------------------------

def from_id_width(id, width):
    return (id % width, id // width)


def reconstruct_path(came_from: Dict[Location, Location],
                     start: Location, goal: Location) -> List[Location]:
    current: Location = goal
    path: List[Location] = []
    while current != start:
        path.append(current)
        current = came_from[current]
    path.append(start)  # optional
    path.reverse()  # optional
    return path


DIAGRAM1_WALLS = [from_id_width(id, width=30) for id in
                  [21, 22, 51, 52, 81, 82, 93, 94, 111, 112, 123, 124, 133, 134, 141, 142, 153, 154, 163, 164, 171, 172,
                   173, 174, 175, 183, 184, 193, 194, 201, 202, 203, 204, 205, 213, 214, 223, 224, 243, 244, 253, 254,
                   273, 274, 283, 284, 303, 304, 313, 314, 333, 334, 343, 344, 373, 374, 403, 404, 433, 434]]

g = SquareGrid(30, 15)
g.walls = DIAGRAM1_WALLS

start = (0, 2)
goal = (17, 4)
parents = breadth_first_search(g, start, goal)
draw_grid(g, point_to=parents, start=start, goal=goal)
print()
draw_grid(g, path=reconstruct_path(parents, start=start, goal=goal))
