# Sarah Engel
# February 20th, 2018
# Professor Foo
# Data Structures

class Node(object):
    
    # create a linked list node consisting of a key/data pair
    def __init__(self, k, d, n = None):
        self.__key  = k
        self.__data = d
        self.__next = n   # reference to next item in list
    
    def __str__(self):
        return "{" + str(self.__key) + ", " + str(self.__data) + "}"
    
    # accessors and mutators
    def getKey(self):     return self.__key
    def getNext(self):    return self.__next
    def getKeyData(self): return self.__key, self.__data
    def setNext(self, n): self.__next = n
    
class CLL(object):
    
    def __init__(self):
        self.__tail = None                  # To start, empty CLL
    
    
    def __len__(self):
        size = 0
        cur = self.__tail                   # Originally cur is last
        
        if cur:                             # If it's not empty
            size += 1                       # Increment the size, and then move to the next node, almost like a fence post
            cur = cur.getNext() 
        
        while cur and cur != self.__tail:   # As long as cur exists and has not gone full-circle back to itself
            size += 1
            cur = cur.getNext()
        
        return size
    
    
    def __str__(self):
        cur = None
        ans = "("
        
        if len(self) > 0:                    # Checking if empty    
            head = self.__tail.getNext()     # Starting at the head    
            ans += str(head)
            cur = head.getNext()
        
        while cur and cur != head:           # As long as cur has not gone full circle
            ans += " ==> " + str(cur)
            cur = cur.getNext()
        
        return ans + " ==>)"
    
    # Inserting at head    
    def insert (self, key, data):
        
        if self.__tail == None:              # Empty CLL
            newNode = Node(key, data, None)
            self.__tail = newNode
            newNode.setNext(self.__tail)     # Needs to point to itself
        
        elif len(self) == 1:                 # One item in the CLL
            newNode = Node(key, data, self.__tail)
            self.__tail.setNext(newNode)
        
        else:                                # If CLL has more than 1 item
            newNode = Node(key, data, self.__tail.getNext())
            self.__tail.setNext(newNode)
        
    
    # deletes the Node at the head of the CLL and returns a tuple containing the deleted key/data pair   
    def delete(self):
        
        # If the CLL has only one element 
        if len(self) == 1:
            ans = self.__tail
            self.__tail = None                # Garbage collection safe
            return ans.getKeyData() 
        
        # If the CLL is empty
        elif self.__tail == None:
            return None
        
        # Normal case, of two or more elem in the CLL
        ans = self.__tail.getNext()
        self.__tail.setNext(ans.getNext())    # Setting tail's next to the one past the head we're deleting
        ans.setNext(None)                     # Then setting the head's next to None to be GC friendly
        
        return ans.getKeyData()
    
    # Accessors and mutators to enable merge
    def getTail(self):             return self.__tail
    def setTail(self, value):      self.__tail = value
       
        
    def merge(self, other):
        
        # If self is empty, steal other's nodes
        if len(self) == 0 and len(other) != 0:
            self.__tail = other.getTail()
            other.setTail(None)
            
        # If other is empty, or both empty we do nothing to self
        elif (len(self) != 0 and len(other) == 0):
            return self
        
        elif (len(other) == 0 and len(self) == 0):
            return self
        
        # If both are full
        elif len(other) > 0 and len(self) > 0:
            temp = self.__tail.getNext()
            self.__tail.setNext(other.getTail().getNext())
            other.getTail().setNext(temp)
            other.setTail(None)


def __main():
    
    # Testing insert
    test = CLL()
    test.insert("Louisa", 19)
    test.insert("Paul", 20)
    test.insert("Pizza", 1.1)
    print("Testing Insert")
    print("Expected result is CLL with Pizza, Paul and Louisa keys. Result: ", test)
    
    # Creating new CLL for merge
    test2 = CLL()
    test2.insert(1233, 123)
    test2.insert("Pasta", "12344")
    
    print()
    
    print("Testing Merge")
    print("CLL 1: ", test)
    print("CLL 2: ", test2)
    test.merge(test2)
    print("Testing merge of CLL1 and CLL2:", test)
    
    print()
    
    print("Testing merge when self is empty")
    e = CLL()
    print("Self:", e)
    print("Other CLL:", test)
    e.merge(test)
    print("Self after merge", e)
    
    print()
    
    print("Testing merge when other is empty")
    other = CLL()
    print("Self:", e)
    print("Other CLL:", other)
    e.merge(other)
    print("Self after merge", e)
    
    print()

    print("Testing merge when both are empty")
    nothing = CLL()
    print("Self:", nothing)
    print("Other CLL:", other)
    nothing.merge(other)
    print("Self after merge", nothing)
    
    print()    
    # Testing over-deletion
    print("Testing delete overflow:")
    print("Before", e)
    for i in range(len(e) + 3):
        e.delete()
        print("After", i+1, "deletion:", e)

    
    
if __name__ == '__main__':
    __main()
        
            
                
        
    
