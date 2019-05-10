# Assignment 5
# CSC 310
# Recursion and Tree Traversals
# Ethan Pellittiere
# 3/20/19


class Hanoi:
    def __init__(self, disks, a, b, c):
        self.disks = disks
        self.pegA = self.Stack(a, disks)
        self.pegB = self.Stack(b, disks)
        self.pegC = self.Stack(c, disks)
        for x in range(disks, 0, -1):
            self.pegA.push(x)

        self.move(disks, self.pegA, self.pegB, self.pegC)

    def move(self, disks, source, spare, target):
        if disks == 0:
            return
        self.move(disks-1, source, target, spare)
        target.push(source.pop())
        print("Moving Disk: " + str(disks) + " from " + source.name + " to " + target.name)
        self.move(disks-1, spare, source, target)

    class Stack:
        cursor = -1
        isEmpty = True
        isFull = False

        def __init__(self, name, size):
            self.name = name
            self.size = size
            self.stack = [None]*size

        def push(self, val):
            self.cursor += 1
            self.stack[self.cursor] = val
            if self.isEmpty:
                self.isEmpty = False
            if self.cursor == self.size-1:
                self.isFull = True

        def pop(self):
            self.cursor -= 1
            if self.isFull:
                self.isFull = False
            if self.cursor == -1:
                self.isEmpty = True
            return self.stack[self.cursor+1]

        def top(self):
            return self.stack[self.cursor]


class binTree:

    def __init__(self, val_list):
        self.head = self.TreeNode(val_list[0])
        for x in val_list[1:]:
            self.add(x, self.head)

        self.inorder()
        self.preorder()

    def add(self, val, node):
        if val <= node.val:
            if node.left is None:
                node.left = self.TreeNode(val)
            else:
                self.add(val, node.left)
        else:
            if node.right is None:
                node.right = self.TreeNode(val)
            else:
                self.add(val, node.right)

    def inorder(self):
        print("Inorder: ", end="")
        self.inorderTraversal(self.head)
        print()

    def inorderTraversal(self, root):
        # Left, Root, Right
        if root.left is not None:
            self.inorderTraversal(root.left)
        print(str(root.val) + " ", end="")
        if root.right is not None:
            self.inorderTraversal(root.right)

    def preorder(self):
        print("Preorder: ", end="")
        self.preorderTraversal(self.head)
        print()

    def preorderTraversal(self, root):
        # Root, Left, Right
        print(root.val + " ", end="")
        if root.left is not None:
            self.preorderTraversal(root.left)
        if root.right is not None:
            self.preorderTraversal(root.right)

    class TreeNode:
        def __init__(self, x):
            self.val = x
            self.left = None
            self.right = None

def main():
    Hanoi(int(input("Enter number of disks: ")), "A", "B", "C")

    binTree(input("Enter List Separated by spaces: ").split())

main()
