import heapq

# 0 = Safe, 1 = Smoke/Fire Obstacle
fire_map = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [1, 1, 0, 1, 0],
    [0, 0, 0, 0, 0]
]

def fire_escape(start, goal):
    queue, came_from, cost = [(0, start)], {start: None}, {start: 0}
    while queue:
        curr = heapq.heappop(queue)[1]
        if curr == goal: break
        for dx, dy in [(0,1), (1,0), (0,-1), (-1,0)]:
            nb = (curr[0]+dx, curr[1]+dy)
            if 0 <= nb[0] < 5 and 0 <= nb[1] < 5 and fire_map[nb[0]][nb[1]] == 0:
                new_cost = cost[curr] + 1
                if nb not in cost or new_cost < cost[nb]:
                    cost[nb] = new_cost
                    priority = new_cost + abs(goal[0]-nb[0]) + abs(goal[1]-nb[1])
                    heapq.heappush(queue, (priority, nb))
                    came_from[nb] = curr
    return came_from

results = fire_escape((0,0), (4,4))
path, curr = [], (4,4)
while curr:
    path.append(curr)
    curr = results.get(curr)

print("--- [REPORT: FIRE ESCAPE SIMULATION] ---")
print(f"EVACUATION ROUTE: {path[::-1]}")
print("STATUS: Safe Exit Path identified away from hazard zones.")