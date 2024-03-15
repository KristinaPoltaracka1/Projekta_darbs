class Node: # defining the class corresponding to the element
    def __init__(self, value, position): #existence of the one certain element with its unique value and position in linked list
        self.value = value # assigns value to the element
        self.position = position # assigns position to the element
        self.next =  None # just one element, no others going after

class Stack: # defining a list to store the information
    def __init__(self): #exists and does not answer any other purposes
        self.top = None # none of the elemnts is top or last in
        self.height = 0 # therefore it is empty/clear

    def is_empty(self): # function to check if the stack is empty
        return self.height == 0 # if the height of list is equal to 0, there is no elements inside, it is empty

    def push(self, value, position): # function that adds an element to the stack
        new_node = Node(value, position) # variable that takes the current element from the class Node along with its value and number of position 
        if self.is_empty(): # using the previously created is_empty function checks if the list is emtpty
            self.top = new_node #in case the list is empty adds an element called new node to it and marks it as a top
        else: #if list is not empty
            new_node.next = self.top #takes the previous element in, the one before last added and it is set as a top
            self.top = new_node #last added element is marked as a top
        self.height += 1 # after adding a new element the length of the list by one

    def pop(self): #function that gives back the element from list
        if self.is_empty(): #checks if the list is empty
            return None # if it is returns nothing
        temp = self.top # qruns in case the list is not empty, and stores the current top element
        self.top = self.top.next #takes the elemnt before the one that marks as a top/the previous one and set as a new top
        self.height -= 1 #decreasing the length of the list by one
        return temp #takes the last element out of the list

def balancets(s): #function that is assigned to the input line
    stack = Stack() # new variable for class stack to use it as a list
    brackets_map = {')': '(', '}': '{', ']': '['} # creating a map with the 'keys':'values' that should go together, meaningly to acces value the corresponding key shouold be used
        

    for i, char in enumerate(s,1): # creating a list that takes input line starting at position one and goes over remembering the value
        if char in brackets_map.values(): # goes through the input line and checks if the symbol matches to the one of several 'values', that exist in map 
            stack.push (char,i) #the match is added to the stack with the push method, keeping its value and position in input line with it
        elif char in brackets_map.keys(): #goes through the input line and checks if the symbol matches to the one of several 'keys', that exist in map
            if stack.is_empty() or brackets_map[char]!= stack.top.value: #checks the stack and if there is nothing in th estack or the element that is marked as a top in stack does not go together with this key, according to the key:value method
                return i #gives the position(number) of the key that is not a match for the top of the stack 
            else: #if the current key and a top element from stack are pair or match
                stack.pop() # takes the element out of the stack using pop method
    if not stack.is_empty(): #checks if there are spare element in the stack after finishing the loop of reading the input line
        return stack.top.position #prints the position(number) of the last elemnt left in stack
    return "Success" #if there are no elements key: values are balanced and it prints success
     

s = input("Ievadiet rindu: ") #variable s answers like an input line
print(balancets(s)) #prints the final result based on balancets method

