import heapq
from typing import List, Optional

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'D', 'E'],
    'D': ['B', 'C', 'F'],
    'E': ['C', 'F'],
    'F': ['D', 'E']
}

h = {
    'A': 10,
    'B': 8,
    'C': 6,
    'D': 4,
    'E': 2,
    'F': 0
}

def best_first_search(start: str, goal: str) -> Optional[List[str]]:
    """Perform greedy best-first search from `start` to `goal` using heuristic `h`.

    Returns the path as a list of node names if found, otherwise `None`.
    """
    if start not in graph:
        raise ValueError(f"Start node '{start}' not in graph")
    if goal not in graph:
        raise ValueError(f"Goal node '{goal}' not in graph")
    if start not in h or goal not in h:
        raise ValueError("Heuristic `h` must contain start and goal nodes")

    # (heuristic, node, path)
    open_list = [(h[start], start, [start])]
    visited = set()

    while open_list:
        heuristic, current, path = heapq.heappop(open_list)

        if current in visited:
            continue

        visited.add(current)

        print(f"Đang xét: {current}, h = {heuristic}")

        if current == goal:
            return path

        for neighbor in graph.get(current, []):
            if neighbor not in visited:
                heapq.heappush(open_list, (h[neighbor], neighbor, path + [neighbor]))

    return None


if __name__ == "__main__":
    start_node = 'A'
    goal_node = 'F'

    try:
        path = best_first_search(start_node, goal_node)
        if path is None:
            print("\nKhông tìm được đường đi.")
        else:
            print("\nĐường đi:", " -> ".join(path))
            print("Tổng chi phí:", len(path) - 1)
    except Exception as exc:
        print("Lỗi:", exc)

    # Pause so the console doesn't close immediately when run by double-click
    try:
        input("\nNhấn Enter để thoát...")
    except EOFError:
        pass