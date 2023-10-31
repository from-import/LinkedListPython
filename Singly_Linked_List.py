class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self,data):
        new_node = Node(data)
        if self.head:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        else:
            self.head = new_node

    def delete(self,data):
        current = self.head
        if current.data == data:
            self.head = current.next
            return 0
        while current.next.data != data:
            current = current.next
            if current.next == None:
                # 链表中不存在此节点
                return -1

        if current.next.next:
            current.next = current.next.next
        else:
            current.next = None


    def display(self):
        current = self.head
        result = []
        while(current.next!=None):
            result.append(current.data)
            current = current.next
        for i in result:
            print(i,end="->")
        print("None")

if __name__ == "__main__":
    my_list = LinkedList()
    my_list.append(1)
    my_list.append(5)
    my_list.append(3)
    my_list.delete(4)
    my_list.display()
