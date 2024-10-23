"""
For choosing a BFS/DFS in graph or matrix, then there should be related components for sure.
BFS: TC: O(m*n) to put rotten orange to queue + O(m*n) for the BFS since each cell will be visited once and
SC: O(m*n) worst case all the oranges are rotten

DFS: one rotten orange might be able to rot all the oranges, but the time will not be minimum. In BFS, we start with
all the rotten oranges and then check their neighbors one by one, while in DFS we cannot start with all the rotten oranges
together. Start with first rotten orange find the time taken to rot oranges using that, then update the time when doing dfs
using the next rotten orange.
DFS: TC: for each rotten orange running DFS O(m*n) and for each DFS O(m*n). Thus, O(m^2 * n^2). SC: O(m*n)
"""
from collections import deque


class Solution_dfs:
    def dfs(self, grid, i, j, time):
        # no base case, it is handled while checking boundary

        # update the time of the cell.
        # for example for the first rotten orange when DFS is called it is updated with time
        grid[i][j] = time

        # find the neignbour index
        for d in self.dir:
            nr = i + d[0]
            nc = j + d[1]

            # check for boundary conditions
            # check if the neignbour is a fresh orange,
            # or if it was fresh by checking the value at the grid location with the current time
            if (nr >= 0 and nr < self.m and nc >= 0 and nc < self.n and (grid[nr][nc] == 1 or grid[nr][nc] > time)):
                # call dfs for that neignbour with +1 time
                self.dfs(grid, nr, nc, time + 1)

    def orangesRotting(self, grid: List[List[int]]) -> int:
        self.m = len(grid)
        self.n = len(grid[0])
        self.dir = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        # offset of 2, to store the time taken by dfs, so that when next dfs is called
        # the results of previous dfs are saved and it helps to save the extra space.
        time = 2
        # call DFS for each rotten orange
        for i in range(self.m):
            for j in range(self.n):
                if grid[i][j] == 2:
                    self.dfs(grid, i, j, time)

                    # after all dfs calls, check if there is any fresh orange
        for i in range(self.m):
            for j in range(self.n):
                if grid[i][j] == 1:
                    return -1
                time = max(time, grid[i][j])

        return time - 2


class Solution_bfs:
    def bfs(self, grid):
        q = deque()
        m = len(grid)
        n = len(grid[0])
        dir = [(0,1), (1,0), (-1,0), (0,-1)]
        fresh = 0
        time = 0
        # add all the rotten oranges to the queue, since it is matrix add row and col number
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    q.append((i,j))
                if grid[i][j] == 1:
                    fresh += 1
        # base check
        if fresh ==0:
            return time
        # traverse the queue
        while q:
            size = len(q)
            for _ in range(size):
                curr = q.popleft()
                # find the neighbor of the current node
                for d in dir:
                    # nr is neighbor row
                    nr = curr[0] + d[0]
                    # nc is the neighbor col
                    nc = curr[1] + d[1]
                    # check if nr and nr are in-bound
                    if nr>=0 and nr<m and nc>=0 and nc<n and grid[nr][nc] == 1:
                        # make it rotten before adding to the queue
                        grid[nr][nc] = 2
                        q.append((nr,nc))
                        fresh -= 1
            time += 1
        # subtract 1 since the oranges are rotten before adding to the queue
        if fresh == 0:
            return time-1
        else:
            return -1
    def orangesRotting(self, grid: List[List[int]]) -> int:
        return self.bfs(grid)



