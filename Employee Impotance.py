"""
We have connected components, we can traverse by using BFS and DFS.
TC: O(n) and SC: O(2n) saving in map and queue
Todo: with one hashmap, where key is id and value is reference to that object.
"""

from collections import deque

"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""
class Solution:

    def getImportance(self, employees: List['Employee'], id: int) -> int:
        hmap_imp = {}
        hmap_sub = {}
        ans = 0
        q = deque()
        for emp in employees:
            # store the importance of each employee by id
            hmap_imp[emp.id] = emp.importance
            # store the subordinates of each employee by id
            hmap_sub[emp.id] = emp.subordinates

        # append the subordinates of given employee to BFS queu
        q.append(hmap_sub[id])
        ans += hmap_imp[id]

        while q:
            # pop the subordaintes of current employee
            curr_lst = q.popleft()
            # for each sub.
            for emp_id in curr_lst:
                print(emp_id)
                q.append(hmap_sub[emp_id])
                ans += hmap_imp[emp_id]

        return ans









