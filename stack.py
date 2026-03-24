stack = []

stack.append(10)
stack.append(20)
stack.append(30)

print("Stack after push:", stack)

removed = stack.pop()
print("Popped element:", removed)

print("Stack after pop:", stack)


print("Top element:", stack[-1])

if not stack:
    print("Stack is empty")
else:
    print("Stack is not empty")
