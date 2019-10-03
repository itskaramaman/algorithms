class Queue:
	def __init__(self):
		self.items = []

	def enque(self, item):
		return self.items.append(item)

	def deque(self):
		return self.items.pop(0)

	def isEmpty(self):
		if self.items:
			return True
		return False		

	
graph = {}
graph[0] = [1, 3]
graph[1] = [5, 3, 2, 6]
graph[3] = [1, 0, 4, 2]
graph[2] = [3, 1, 5, 4]
graph[4] = [3, 2, 6]
graph[6] = [4, 1]
graph[5] = [1, 2]		


def BFS(node):
	# create a queue instance
	q = Queue()
	# enque the starting node 
	q.enque(0)
	result = []
	while q.isEmpty():
		first_item = q.deque()
		result.append(first_item)
		node = first_item
		# add items to queue
		q.items += [i for i in graph[node] if i not in result and i not in q.items]
	print(result)

BFS(0)