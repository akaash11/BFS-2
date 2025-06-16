# S30 Problem #60 Binary Tree Right Side View
#LeetCode #199 https://leetcode.com/problems/binary-tree-right-side-view/description/

# Author : Akaash Trivedi
# Time Complexity : O(n)
# Space Complexity : O(n)
# Did this code successfully run on Leetcode :  Yes #
# Any problem you faced while coding this : No

# dfs
class Solution:
    def __init__(self):
        self.res = []
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        self.dfs(root,0)
        return self.res
    def dfs(self, root, level):
        #base
        if not root:
            return
        #logic
        if len(self.res) == level:
            self.res.append(root.val)
        # first traverse right subtree
        self.dfs(root.right, level+ 1)
        self.dfs(root.left, level + 1)

# bfs and checking the level size 
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if not root:
            return res
        q = deque()
        q.append(root)
        level = 0

        while q:
            size = len(q)
            for i in range(size):
                curr = q.popleft()
                # check if its the last element of the level
                if i == size -1:
                    res.append(curr.val)
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
            level +=1
        return res