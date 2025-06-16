# S30 Problem #61 Cousins in Tree
#LeetCode #993 https://leetcode.com/problems/cousins-in-binary-tree/description/

# Author : Akaash Trivedi
# Time Complexity : O(n)
# Space Complexity : O(h) #dfs
# Space Complexity : O(n) #bfs
# Did this code successfully run on Leetcode :  Yes #
# Any problem you faced while coding this : No

# DFS
class Solution:
    def __init__(self):
        self.xParent = TreeNode()
        self.yParent = TreeNode()
        # to track the level once found
        self.xlevel = None
        self.ylevel = None

    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        self.dfs(root, x, y, None, 0)
        return self.xlevel == self.ylevel and self.xParent != self.yParent

    def dfs(self, root, x, y, parent, level) -> None:
        # base
        if not root:
            return
        
        #logic
        if root.val == x:
            self.xlevel = level
            self.xParent = parent
            
        if root.val == y:
            self.ylevel = level
            self.yParent = parent 

        # recursion
        self.dfs(root.left, x, y, root, level+1)
        self.dfs(root.right, x, y, root, level+1)

# BFS
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        q = deque()
        pq = deque()
        q.append(root)
        pq.append(None)
        level = 0

        while q:
            size = len(q)
            # bool if x and y exist
            xFlag = False
            yFlag = False
            # store parent of x and y
            xp = TreeNode() 
            yp = TreeNode()
            for i in range(size):
                currNode = q.popleft()
                currParent = pq.popleft()
                if currNode.val == x:
                    xFlag = True
                    xp = currParent
                if currNode.val == y:
                    yFlag = True
                    yp = currParent
                # check if x and y are exist at this level and parents are diff
                if xFlag and yFlag and xp != yp:
                    return True
                # adding children
                if currNode.left:
                    q.append(currNode.left)
                    pq.append(currNode)
                if currNode.right:
                    q.append(currNode.right)
                    pq.append(currNode)
        return False