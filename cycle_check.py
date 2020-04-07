from linked_list import Node 

def cycle_check(node):
    marker1 = node
    marker2 = node

    while marker1 != None and marker2.next_node != None:
        marker1 = node.next_node
        marker2 = node.next_node.next_node

        if marker1 == marker2:
            return True

    return False

         


