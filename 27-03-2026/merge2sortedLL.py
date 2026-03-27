
class Node:
    def __init__(self, data): 
        self.data = data
        self.next = None


class Solution:
    def sortedMerge(self, head1, head2):
        dummyNode=Node(-1)
        temp=dummyNode
        t1=head1
        t2=head2
        while t1 is not None and t2 is not None:
            if t1.data<t2.data:
                temp.next=t1
                t1=t1.next
                
            else:
                temp.next=t2
                t2=t2.next
            
            temp=temp.next
            
        if t1 is not None:

            temp.next=t1

        else:

            temp.next=t2

        return dummyNode.next


# Helper function to create a linked list from a list
def createLinkedList(arr):
    if not arr:
        return None
    head = Node(arr[0])
    current = head
    for i in range(1, len(arr)):
        current.next = Node(arr[i])
        current = current.next
    return head


# Helper function to print a linked list
def printLinkedList(head):
    result = []
    current = head
    while current:
        result.append(current.data)
        current = current.next
    print(" -> ".join(map(str, result)))


# Test the sortedMerge function
if __name__ == "__main__":
    sol = Solution()
    
    # Example 1
    print("Example 1:")
    list1 = createLinkedList([1, 3, 5, 7])
    list2 = createLinkedList([2, 4, 6, 8])
    
    print("List 1: ", end="")
    printLinkedList(list1)
    
    print("List 2: ", end="")
    printLinkedList(list2)
    
    merged = sol.sortedMerge(list1, list2)
    print("Merged: ", end="")
    printLinkedList(merged)
    
    print("\n" + "="*40 + "\n")
    
    # Example 2
    print("Example 2:")
    list3 = createLinkedList([1, 2, 3])
    list4 = createLinkedList([4, 5, 6])
    
    print("List 1: ", end="")
    printLinkedList(list3)
    
    print("List 2: ", end="")
    printLinkedList(list4)
    
    merged2 = sol.sortedMerge(list3, list4)
    print("Merged: ", end="")
    printLinkedList(merged2)
    
    print("\n" + "="*40 + "\n")
    
    # Example 3
    print("Example 3:")
    list5 = createLinkedList([5, 10, 15])
    list6 = createLinkedList([2, 8, 12, 20])
    
    print("List 1: ", end="")
    printLinkedList(list5)
    
    print("List 2: ", end="")
    printLinkedList(list6)
    
    merged3 = sol.sortedMerge(list5, list6)
    print("Merged: ", end="")
    printLinkedList(merged3)
