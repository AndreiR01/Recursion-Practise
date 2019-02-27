#Our high-level strategy before moving through the checkpoints.

#1.base case: the input list is empty
#    2.Return "No Child" to represent the lack of node
#3.recursive step: the input list must be divided into two #halves
#    4.Find the middle index of the list
#    5.Store the value located at the middle index
#    6.Make a tree node with a "data" key set to the value
#    7.Assign tree node's "left child" to a recursive call using the left half of the list
#    8.Assign tree node's "right child" to a recursive    call using the right half of the list
#    9.Return the tree node

def build_bst(my_list):

    if len(my_list) == 0:
        return "No Child!"

    middle_idx = len(my_list) // 2
    middle_value = my_list[middle_idx]

    print("Middle index: {0}".format(middle_idx))
    print("Middle value: {0}".format(middle_value))

    tree_node = {"data": middle_value}
    tree_node["left_child"] = build_bst(my_list[:middle_idx])
    tree_node["right_child"] = build_bst(my_list[middle_idx + 1:])

    return tree_node

#-----------TESTING--------------#
sorted_list = [12, 13, 14, 15, 16]
binary_search_tree = build_bst(sorted_list)
print(binary_search_tree)
