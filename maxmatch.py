import codecs

class MaxMatch():

	def __init__(self,file):
		super(MaxMatch, self).__init__()
		self.words = []
		with codecs.open(file, mode='r', encoding='utf-8') as f:
			for word in f:
				self.words.append(word.strip())

	def printWordList(self):
		for i in self.words:
			print(i)
		pass


	def hasWord(self,word):
		for i in self.words:
			# print('match',i,' - ',word)
			if i==word:
				return True
		return False;



max_match = MaxMatch('wordlist.txt');

with codecs.open('50_nospaces.txt', mode='r', encoding='utf-8') as f:
	
	sentences = []
	for line in f:
		output = []
		line = line.strip()
		if not line:
			continue

		line_len = len(line)

		start=0
		
		end= line_len

		while start!=line_len:
			
			word = line[start:end];
			

			if len(word) ==1:
				output.append(word)
				end = line_len
				start=start+1
				continue

			elif max_match.hasWord(word):
				output.append(word)
				start=end
				end = line_len
				continue

			end = end-1
		sentences.append(output)

f = open("output.txt", "w")
for output in sentences:
	f.write(" ".join(output))
	f.write("\n")
				
			
	