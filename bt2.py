from collections import deque

# ----------------------------
# 1. Xây dựng đồ thị (danh sách kề)
# ----------------------------
graph = {
    'A': ['B', 'C', 'D'],
    'B': ['E', 'F'],
    'C': ['G', 'H'],
    'D': ['I', 'J'],
    'E': ['K', 'L'],
    'F': ['L', 'M'],
    'G': ['N'],
    'H': ['O', 'P'],
    'I': ['P', 'Q'],
    'J': [],
    'K': ['S'],
    'L': ['T'],
    'M': [],
    'N': [],
    'O': [],
    'P': ['U'],      # 'U' là con nhưng không cần xét vì đã tìm thấy P
    'Q': [],
    'S': [],
    'T': [],
    'U': []
}

start = 'A'
goal = 'P'

# ----------------------------
# 2. BFS – Tìm kiếm theo chiều rộng
# ----------------------------
def bfs(graph, start, goal):
    visited = []          # thứ tự duyệt
    queue = deque([start])
    
    while queue:
        node = queue.popleft()
        if node in visited:
            continue
        visited.append(node)
        if node == goal:
            break
        for neighbor in graph.get(node, []):
            if neighbor not in visited and neighbor not in queue:
                queue.append(neighbor)
    return visited

print("BFS thứ tự duyệt:", bfs(graph, start, goal))

# ----------------------------
# 3. DFS – Tìm kiếm theo chiều sâu (dùng stack)
# ----------------------------
def dfs(graph, start, goal):
    visited = []
    stack = [start]
    
    while stack:
        node = stack.pop()
        if node in visited:
            continue
        visited.append(node)
        if node == goal:
            break
        # Thêm các con vào stack (đảo ngược để duyệt trái trước)
        for neighbor in reversed(graph.get(node, [])):
            if neighbor not in visited and neighbor not in stack:
                stack.append(neighbor)
    return visited

print("DFS thứ tự duyệt:", dfs(graph, start, goal))

# ----------------------------
# 4. Depth‑Limited DFS (giới hạn độ sâu = 3)
# ----------------------------
def depth_limited_dfs(graph, start, goal, max_depth):
    visited = []
    
    def recursive_dfs(node, depth):
        if node in visited:
            return False
        visited.append(node)
        if node == goal:
            return True
        if depth >= max_depth:
            return False   # không mở rộng nếu đã đạt giới hạn
        
        for neighbor in graph.get(node, []):
            if recursive_dfs(neighbor, depth + 1):
                return True
        return False
    
    recursive_dfs(start, 0)
    return visited

print("Depth-Limited DFS (giới hạn 3):", depth_limited_dfs(graph, start, goal, 3))