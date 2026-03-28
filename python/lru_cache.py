class Node:
    def __init__(self, data = None, key = None, next = None, prev = None):
        self.data = data;
        self.key = key
        self.next = next
        self.prev = prev
  


class DoublyLinkedList:
    def __init__(self, head = None, tail = None):
        self.head = head
        self.tail = tail


    # ADD THE NODE TO THE HEAD OF THE LIST
    # O(1)
    def addHead(self, node):
        # if self.head is None:
        #     self.head = node
        #     self.tail = node
        #     return
        
        # self.head.prev = node
        # node.next = self.head
        # self.head = node
        # self.head.prev = None
        node.prev = None
        node.next = self.head

        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.head.prev = node
            self.head = node


        

    # REMOVE THE TAIL NODE FROM THE LIST
    # AND RETURN IT
    # O(1)
    def removeTail(self):
        # last_node = self.tail
        # self.tail = self.tail.prev

        # if not self.tail:
        #     self.head = None

        # last_node.prev = None

        # return last_node
        '''
        above attemp issues:
            1. if list empty, self.tail is None, self.tail.prev will crash
            2. when litst has more than one node, did not clear last_node.next
        '''
        if self.tail is None:
            return None

        removed = self.tail

        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.tail = removed.prev
            self.tail.next = None

        removed.prev = None
        removed.next = None
        return removed


    # REMOVE THE GIVEN NODE FROM THE LIST
    # AND THEN RETURN IT
    def removeNode(self, node):
        # if self.head == self.tail:
        #     self.head = None
        #     self.tail = None
        #     return node
        
        # node.prev.next = node.next  

        # if node == self.tail:
        #     self.tail = node.prev
        # else:
        #     node.next.prev = node.prev

        # return node
        '''
        issues:
            1. If node == self.head, then node.prev is None,
               node.prev.next = node.next  will crash

            2. removed node should be disconnected
        '''
        if self.head == self.tail:
            self.head = None
            self.tail = None
        elif node == self.head:
            self.head = node.next
            self.head.prev = None
        elif node == self.tail:
            self.tail = node.prev
            self.tail.next = None
        else:
            node.prev.next = node.next
            node.next.prev = node.prev

        node.prev = None
        node.next = None
        return node


    # MOVE THE GIVEN NODE FROM ITS LOCATION TO THE HEAD
    # OF THE LIST
    def moveNodeToHead(self, node):
        # self.removeNode(node)
        # node.next = self.head
        # self.head = node
        '''
        issue:
            1. did not update: 
                - node.prev
                - old head’s prev
                - possibly tail when needed 
        '''
        if node == self.head:
            return

        self.removeNode(node)
        self.addHead(node)
  

class LRUCache:
    def __init__(self, limit = 10):
        self.limit = limit
        self.size = 0
        self.hash = {}
        self.list = DoublyLinkedList()


  # RETRIEVE THE NODE FROM THE CACHE USING THE KEY
  # IF THE NODE IS IN THE CACHE, MOVE IT TO THE HEAD OF THE LIST AND RETURN IT
  # OTHERWISE RETURN -1
    def get(self, key):
        if key in self.hash:
            node = self.hash[key]
            self.list.moveNodeToHead(node)
            return node
        return -1
  

  # ADD THE GIVEN KEY AND VALUE TO THE CACHE
  # IF THE CACHE ALREADY CONTAINS THE KEY, UPDATE ITS VALUE AND MOVE IT TO 
  # THE HEAD OF THE LIST
  # IF THE CACHE DOESN'T CONTAIN THE KEY, ADD IT TO THE CACHE AND PLACE IT
  # AT THE HEAD OF THE LIST
  # IF THE CACHE IS FULL, REMOVE THE LEAST RECENTLY USED ITEM BEFORE ADDING
  # THE NEW DATA TO THE CACHE
    def put(self, key, value):
        node = self.get(key)
        if node != -1:
            node.data = value
        else:
            node = Node(value, key)
            
            if self.size == self.limit:
                removed = self.list.removeTail()
                self.hash.pop(removed.key)
            else:
                self.size += 1

            self.list.addHead(node)
            self.hash[key] = node

        # below is more standard format:
        '''
        if key in self.hash:
            node = self.hash[key]
            node.data = value
            self.list.moveNodeToHead(node)
            return

        new_node = Node(data=value, key=key)

        if self.size == self.limit:
            removed = self.list.removeTail()
            del self.hash[removed.key]
            self.size -= 1

        self.list.addHead(new_node)
        self.hash[key] = new_node
        self.size += 1
        '''

# if (require.main === module) {
#   // add your own tests in here
# }

# module.exports = {
#   Node,
#   DoublyLinkedList,
#   LRUCache
# };

# // Please add your pseudocode to this file
# // And a written explanation of your solution
