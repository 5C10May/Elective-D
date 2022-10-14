# Return True if the queue is empty

def isEmpty():
    global end    
    return (end+1==front)
 

# Retutn True if the queue is full
def isFull():
    return (end-front+1 == queue_size)


# Function to add an item to end of the queue
def add(item):
    if  not isFull():
        global queue, front, end
        end = end + 1                                     #required in Python if we're modifying a global variable    
        queue[end] = item
        print('Added', item, 'OK!')
    
    else:
        print('Error: Queue is full.')                                     #required in Python if we're modifying a global variable    

    
  

# Function to remove the front item from the queue
def remove():
    global queue, front, end
    if isEmpty():
        print('Queue is empty') 
    else:
        front = front + 1    
    return queue[front-1]
    
    
# Function to return the number of items in the queue
def size():
    return (end - front +1)


# Function to return the front item without removing it from the queue
def peek():    
    if isEmpty():
        return None
    return queue[front]


# Function to print the queue contents
def printQueue():
    if isEmpty():
        return "Queue is empty"
    else:        
        for i in range(front, front+size()):
            print(f'{queue[i]} ', end=' ')   
    print()



'''
Global variables
'''
queue_size = 5                  #set queue_size here
queue = [None]*10000            #build a very long list
front = 0                       #front pointing to the first item of the queue
end = -1                        #end pointing to the last item of the queue, end < front if queue is empty


'''
Driver code - test the queue operations here
'''
add('a')
add('b')
add('c')
printQueue()

print('The front item:', peek())
print('Dequeue:', remove())
printQueue()

add('d')
add('e')
add('f')
add('g')
printQueue()

print('Dequeue:', remove())
add('g')
printQueue()

remove()
remove()
remove()
remove()
remove()
printQueue()

remove()
