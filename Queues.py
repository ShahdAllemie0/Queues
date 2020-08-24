class Node:
    def __init__(self, size, next_node=None):
        self.size = size
        self.next_node = next_node
    
    def set_next_node(self, next_node):
        self.next_node = next_node
    
    def get_next_node(self):
        return self.next_node
    
    def get_size(self):
        return self.size
class Queue:
    def __init__(self, limit=None,front_node=None,back_node = None):
        self.front_node =front_node
        self.back_node = back_node
        self.length = 0
        self.limit = limit
        self.waiting_time=0
    
    def is_full(self):
        return self.length == self.limit 

    def is_empty(self):
        return self.length == 0
    
    def get_length(self):
        return self.length

    def add_node(self,data):
      new_node=Node(data)
      if self.is_empty():
        self.front_node=new_node
      else:
        self.back_node.set_next_node(new_node) 
      self.back_node=new_node
      self.length+=1
      self.waiting_time+=(data*0.5)   
       

    def peek(self):
        return self.waiting_time

    def enqueue(self, data):
        
        if not self.is_full():
            people_num=data
            while people_num>12:
              self.add_node(12)
              people_num-=12
            self.add_node(people_num)
        else:
            print("No more spaces")


    def dequeue(self):
        if not self.is_empty():
            removed_node = self.front_node
            self.front_node =removed_node.get_next_node()
            self.length-=1
            self.waiting_time-=(removed_node.get_size()*0.5)
            return removed_node.get_size()
        else:
            print("Ya basic! Nothing here nerd!")  

    def getData(self): 
       data=[]
       currentNode=self.top
       while currentNode:
         if currentNode.getData()!= None:
            data.append(currentNode.getData())
         currentNode=currentNode.getNext()
       return data                 
s=Queue(10)
s.enqueue(3)
print(s.waiting_time)
print("-"*20)
s.enqueue(3)
s.enqueue(10)
s.enqueue(13)
print(s.waiting_time)
print("-"*20)
s.dequeue()
print(s.waiting_time)

