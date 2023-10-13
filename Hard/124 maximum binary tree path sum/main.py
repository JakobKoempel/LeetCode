
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def maxPathSum(self, root):
        (line_sum, path_sum) = self.maxPathSumRec(root)
        return path_sum
    
    def maxPathSumRec(self, root):
        #leaf node
        if root.left == None and root.right == None:
            return (root.val, root.val)
        
        #only left child (arc sum and line sum coincide)
        elif root.left != None and root.right == None:
            (left_line_sum, left_path_sum) = self.maxPathSumRec(root.left)

            #add positive left line sum onto root value
            line_sum = root.val + max(left_line_sum, 0)
            
            path_sum = max(line_sum, left_path_sum)
            return (line_sum, path_sum)
        
        #only right child (arc sum and line sum coincide)
        elif root.left == None and root.right != None:
            (right_line_sum, right_path_sum) = self.maxPathSumRec(root.right)

            #add positive left line sum onto root value
            line_sum = root.val + max(right_line_sum, 0)

            path_sum = max(line_sum, right_path_sum)
            return (line_sum, path_sum)
        
        #2 children
        else:
            (left_line_sum, left_path_sum) = self.maxPathSumRec(root.left)
            (right_line_sum, right_path_sum) = self.maxPathSumRec(root.right)

            #compute line sum by choosing largest positive line sum of the children and adding it onto the root value
            line_sum = root.val + max(left_line_sum, right_line_sum, 0)

            #compute the arc sum by adding all positive line sums of the children
            arc_sum = root.val + max(left_line_sum, 0) + max(right_line_sum, 0)

            path_sum = max(arc_sum, left_path_sum, right_path_sum)
            return (line_sum, path_sum)
        