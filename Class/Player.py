class Player:
	name = ""
	points = 0
	def __init__(self, name):
		self.name = name
		return

	def increasePlayerPoints(self):
		self.points += 1

	def returnPlayerPoints(self):
		return self.points