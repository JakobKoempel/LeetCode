
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        if root == None:
            return "N"
        else:
            s = str(root.val + 2000)   #lowest possible root value is -1000 and we dont want negatives 4 digit numbers
            s_left = self.serialize(root.left)
            s_right = self.serialize(root.right)

            return s + s_left + s_right

    def deserialize(self, data):
        tree, data = self.deserializeRec(data)
        return tree
    
    def deserializeRec(self, data):
        if data[0] == "N":
            data = data[1:]
            return None, data
        else:
            val = int(data[0:4]) - 2000
            data = data[4:]
            tree = TreeNode(val)
            tree.left, data = self.deserializeRec(data)
            tree.right, data = self.deserializeRec(data)

            return tree, data




# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))