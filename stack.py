class Stack:
	def __init__(self):
		self.items = []

	def push(self, item):
		self.items.append(item)

	def pop(self):
		return self.items.pop(0)

	def isEmpty(self):
		if len(self.items)==0:
			return True
		return False	
		

# s = Stack()
# s.push(5)
# s.push(7)
# s.push(11)
# print(s.items)
# s.pop()
# print()
# s.pop()
# print(s.items)
