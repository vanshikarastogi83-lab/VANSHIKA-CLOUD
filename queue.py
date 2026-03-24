queue = []

queue.append(10)
queue.append(20)
queue.append(30)

print("Queue after enqueue:", queue)


removed = queue.pop(0)
print("Dequeued element:", removed)

print("Queue after dequeue:", queue)


print("Front element:", queue[0])


if not queue:
    print("Queue is empty")
else:
    print("Queue is not empty")
