import datetime


class Entry:
	def __init__(self, identifier: str, deadline: datetime.datetime):
		self.identifier = identifier
		self.deadline = deadline


	def get_deadline(self):
		return self.remaining_time(self.deadline)


	@staticmethod
	def remaining_time(date: datetime.datetime):
		delta = date - datetime.datetime.now()
		days = delta.days
		hours = int(delta.seconds / 60 // 60)
		minutes = int((delta.seconds - hours * 60 ** 2) // 60)
		seconds = int(delta.seconds - hours * 60 ** 2 - minutes * 60)
		return {
			"days": delta.days,
			"hours": int(delta.seconds / 60 // 60),
			"minutes": int((delta.seconds - hours * 60 ** 2) // 60),
			"seconds": int(delta.seconds - hours * 60 ** 2 - minutes * 60)
		}


	@staticmethod
	def format_deadline(deadline: datetime.datetime):
		return f"{deadline.date()} : {deadline.time()}"


	def __repr__(self):
		return f"{self.identifier} :: {self.format_deadline(self.deadline)}"
