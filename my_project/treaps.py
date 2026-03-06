import random


class Node:
    def __init__(self, value, priority, parent, left_child, right_child):
        self.value = value
        self.priority = priority
        self.parent = parent
        self.left_child = left_child
        self.right_child = right_child

    def get_info(self):
        return f"value: {self.value}, priority: {self.priority}, parent: {self.parent.value if self.parent else "none"}, left child: {self.left_child.value if self.left_child else "none"}, right child: {self.right_child.value if self.right_child else "none"}"  # noqa


def simple_insert(root_node, value):
    # print("root node: " + root_node.get_info())
    # print("value: ", value)
    if value < root_node.value and root_node.left_child:
        print("traversing down left")
        return simple_insert(root_node.left_child, value)
    elif value > root_node.value and root_node.right_child:
        print("traversing down right")
        return simple_insert(root_node.right_child, value)
    elif value < root_node.value and not root_node.left_child:
        print("adding new left child")
        new_child = Node(value, random.random(), root_node, None, None)
        root_node.left_child = new_child
        return new_child
    elif value > root_node.value and not root_node.right_child:
        print("adding new right child")
        new_child = Node(value, random.random(), root_node, None, None)
        root_node.right_child = new_child
        return new_child


def simple_search(root_node, value):
    if value == root_node.value:
        return root_node
    elif value < root_node.value and root_node.left_child:
        return simple_search(root_node.left_child, value)
    elif value > root_node.value and root_node.right_child:
        return simple_search(root_node.right_child, value)


def simple_delete(root_node, value):
    delete_node = simple_search(root_node, value)
    if not delete_node.right_child and not delete_node.left_child and delete_node.parent:  # type: ignore
        delete_node = None
        return root_node
    elif delete_node.right_child and not delete_node.left_child and delete_node.parent:  # type: ignore
        delete_node.right_child.parent = delete_node.parent  # type: ignore


my_values_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
random.shuffle(my_values_list)
print(my_values_list)
my_root_node = Node(my_values_list[0], random.random(), None, None, None)
print(my_root_node.get_info())
for i in range(1, 10):
    newest_child = simple_insert(my_root_node, my_values_list[i])
    # print(newest_child)
    print(newest_child.get_info())  # type: ignore

print(simple_search(my_root_node, random.choice(my_values_list)))
