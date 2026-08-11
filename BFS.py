from collections import deque

# 1. Khai báo đồ thị dạng Danh sách kề
graph = {
    'A': ['C', 'D', 'F'],
    'B': [],
    'C': ['B', 'E'],
    'D': ['G'],
    'E': [],
    'F': [],
    'G': ['H', 'T'],
    'H': ['K', 'M'],
    'T': [],
    'K': [],
    'M': []
}

def bfs_with_shortest_path(graph, start_node, target_node):
    L = deque([start_node])
    visited = set([start_node])
    
    # Từ điển lưu đỉnh cha để tìm đường đi ngắn nhất
    FATHER = {start_node: None}
    
    # Danh sách lưu kết quả các đỉnh được duyệt
    traversal_result = []
    
    print("--- QUÁ TRÌNH DUYỆT BFS ---")
    stt = 1
    
    while L:
        u = L.popleft()
        traversal_result.append(u)
        
        if u == target_node:
            print(f"Bước {stt}: Lấy u = {u} -> Đã tìm thấy đỉnh đích {target_node}!")
            break
            
        neighbors = graph.get(u, [])
        v_list = []
        
        for v in neighbors:
            if v not in visited:
                visited.add(v)
                FATHER[v] = u   # Lưu đỉnh cha của v
                L.append(v)
                v_list.append(v)
                
        # In bảng quá trình duyệt
        v_str = ", ".join(v_list) if v_list else "không"
        l_str = ", ".join(L)
        print(f"Bước {stt}: u = {u:<2} | Đỉnh kề v mới = {v_str:<8} | Hàng đợi L còn = [{l_str}]")
        
        stt += 1

    # Truy vết đường đi ngắn nhất từ target_node về start_node
    path = []
    curr = target_node
    while curr is not None:
        path.append(curr)
        curr = FATHER.get(curr)
    path.reverse() # Đảo ngược để có chiều từ start -> target

    return traversal_result, path

# --- CHƯƠNG TRÌNH CHÍNH ---
start = 'A'
target = 'T'

traversal, shortest_path = bfs_with_shortest_path(graph, start, target)

# 1. In kết quả duyệt BFS
print("\n=> Kết quả duyệt BFS từ", start, "đến", target, "là:")
print(" -> ".join(traversal))

# 2. In đường đi ngắn nhất
print("\n=> Đường đi ngắn nhất từ", start, "đến", target, "là:")
print(" -> ".join(shortest_path))