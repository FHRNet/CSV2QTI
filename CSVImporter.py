import csv
from question import Question

class CSVImporter:
	def __init__(self, delimiter = ';', quotechar=''):
		if delimiter == '\\t':
			self.delimiter = '\t'
		else: 
			self.delimiter = delimiter
		self.quotechar = quotechar

	def getQuestions(self, question_file):
		questions = []
		with open(question_file, 'rb') as csvfile:
			reader = csv.reader(csvfile, delimiter=self.delimiter)
			line = 0
			for row in reader:
				line += 1
				
				# Skip the header
				if line == 1:
					continue
				if (len(row) < 5):
					continue
				question = Question()
				question.id = row[0]
				question.question = row[1]
				question.category = row[2]
				question.correct_answer = "1"
				for i in range(3, 7):
					if not row[i]:
						continue
					question.answers.append(row[i])
				questions.append(question)
				question.image = row[8]
		return questions
