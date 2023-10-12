class Stack:
    def __init__(self):
        self.stack = []

    def is_empty(self):
        return len(self.stack) == 0

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            print("Stack is empty.")
            return None

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            print("Stack is empty.")
            return None

    def size(self):
        return len(self.stack)


# Example usage
if __name__ == "__main__":
    stack = Stack()

    # Push elements onto the stack
    stack.push(10)
    stack.push(20)
    stack.push(30)

    # Print the stack
    print("Stack elements:")
    print(stack.stack)

    # Pop an element from the stack
    popped_element = stack.pop()
    print("Popped element:", popped_element)

    # Peek the top element in the stack
    top_element = stack.peek()
    print("Top element:", top_element)

    # Print the updated stack
    print("Updated stack elements:")
    print(stack.stack)
