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
        # print("traversing down left")
        return simple_insert(root_node.left_child, value)
    elif value > root_node.value and root_node.right_child:
        # print("traversing down right")
        return simple_insert(root_node.right_child, value)
    elif value < root_node.value and not root_node.left_child:
        # print("adding new left child")
        new_child = Node(value, random.random(), root_node, None, None)
        root_node.left_child = new_child
        return new_child
    elif value > root_node.value and not root_node.right_child:
        # print("adding new right child")
        new_child = Node(value, random.random(), root_node, None, None)
        root_node.right_child = new_child
        return new_child


def simple_search(root_node, value):
    if value == root_node.value:
        print("found it")
        return root_node
    elif value < root_node.value and root_node.left_child:
        print("traversing down left")
        return simple_search(root_node.left_child, value)
    elif value > root_node.value and root_node.right_child:
        print("traversing down right")
        return simple_search(root_node.right_child, value)


def find_smallest_right(sub_root_node):
    curr_smallest_right = sub_root_node.right_child
    if curr_smallest_right:
        while True:
            if curr_smallest_right.left_child:
                curr_smallest_right = curr_smallest_right.left_child
            elif not curr_smallest_right.left_child:
                return curr_smallest_right
    return sub_root_node


def simple_delete(root_node, value=None, node=None):
    # print(root_node)
    # print(value)
    if value and not node:
        delete_node = simple_search(root_node, value)
    if node and not value:
        delete_node = node
    if not delete_node:
        print("no delete node")
        return None
    if not delete_node.right_child and not delete_node.left_child and delete_node.parent:  # type: ignore
        print("case 1")
        delete_node = None
        return root_node
    elif delete_node.left_child and not delete_node.right_child and delete_node.parent:  # type: ignore
        print("case 2")
        temp_node = delete_node.left_child  # type: ignore
        delete_node.left_child.parent = delete_node.parent  # type: ignore
        if delete_node.parent.left_child == delete_node:  # type: ignore
            delete_node.parent.left_child = temp_node  # type: ignore
        elif delete_node.parent.right_child == delete_node:  # type: ignore
            delete_node.parent.right_child = temp_node  # type: ignore
        delete_node = None
        return root_node
    elif delete_node.right_child and not delete_node.left_child and delete_node.parent:  # type: ignore
        print("case 3")
        temp_node = delete_node.right_child  # type: ignore
        delete_node.right_child.parent = delete_node.parent  # type: ignore
        if delete_node.parent.left_child == delete_node:  # type: ignore
            delete_node.parent.left_child = temp_node  # type: ignore
        elif delete_node.parent.right_child == delete_node:  # type: ignore
            delete_node.parent.right_child = temp_node  # type: ignore
        delete_node = None
        return root_node
    elif delete_node.left_child and delete_node.right_child:  # type: ignore
        print("case 4")
        switch_node = find_smallest_right(delete_node)
        # print(delete_node.get_info())
        # print(switch_node.get_info())
        delete_node.value, switch_node.value = switch_node.value, delete_node.value  # type: ignore
        delete_node.priority, switch_node.priority = switch_node.priority, delete_node.priority  # type: ignore
        # print(delete_node.get_info())
        # print(switch_node.get_info())
        # display_tree(root_node)
        # display_tree(delete_node)
        # display_tree(switch_node)
        # delete_this_node_ffs = simple_search(root_node, switch_node.value)
        # print(switch_node)
        # print(switch_node.value)
        # print(delete_this_node_ffs)
        display_tree_info(root_node)
        return simple_delete(root_node, node=switch_node)


def get_tree(root_node):
    tree = [[root_node]]
    done = False
    while not done:
        prev_layer = tree[-1]
        new_layer = []
        num_real_nodes = 0
        for node in prev_layer:
            if node:
                if node.left_child:
                    new_layer.append(node.left_child)
                    num_real_nodes += 1
                if not node.left_child:
                    new_layer.append(None)
                if node.right_child:
                    new_layer.append(node.right_child)
                    num_real_nodes += 1
                if not node.right_child:
                    new_layer.append(None)
            if not node:
                new_layer.append(None)
                new_layer.append(None)
        if num_real_nodes != 0:
            tree.append(new_layer)
        elif num_real_nodes == 0:
            done = True
    return tree


def display_tree_info(root_node):
    tree = get_tree(root_node)
    for layer in tree:
        for node in layer:
            if node:
                print(node.get_info())


def display_tree(root_node):
    tree = get_tree(root_node)
    for layer in tree:
        layer_str = ""
        for node in layer:
            if node:
                layer_str += str(node.value)
                layer_str += " "
            if not node:
                layer_str += "_ "
        print(layer_str)


my_values_list = list(range(1, 21))
print(my_values_list)
random.shuffle(my_values_list)
print(my_values_list)
my_root_node = Node(my_values_list[0], random.random(), None, None, None)
print(my_root_node.get_info())
for i in range(1, len(my_values_list)):
    newest_child = simple_insert(my_root_node, my_values_list[i])
    # print(newest_child)
    print(newest_child.get_info())  # type: ignore

# print(simple_search(my_root_node, random.choice(my_values_list)).get_info())  # type: ignore
display_tree(my_root_node)
simple_delete(my_root_node, value=random.choice(my_values_list))
display_tree(my_root_node)
