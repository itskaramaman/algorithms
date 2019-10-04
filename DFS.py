class Stack:
	def __init__(self):
		self.items = []

	def push(self, item):
		self.items.append(item)

	def pop(self):
		return self.items.pop()

	def isEmpty(self):
		if len(self.items)==0:
			return False
		return True

	def topElement(self):
		return self.items[-1]
		

graph = {}
graph[0] = [1, 3]
graph[1] = [5, 3, 2, 6]
graph[3] = [1, 0, 4, 2]
graph[2] = [3, 1, 5, 4]
graph[4] = [3, 2, 6]
graph[6] = [4, 1]
graph[5] = [1, 2]

def DFS(node):
	s = Stack()
	s.push(node)
	result = []
	result.append(node)
	while s.isEmpty():
		topNode = s.topElement()
		for i in graph[topNode]:
			if i not in result:
				s.push(i)
				result.append(i)
				break
		if topNode == s.topElement():
			s.pop()
				
	return result

print(DFS(3))						
