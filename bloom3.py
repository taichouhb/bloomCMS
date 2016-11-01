import random
from bitarray import bitarray
import mmh3

def main():
	w = 3200000
	hashs = bitarray(w)
	hashs.setall(0)
	real = []
	hashRes = []
	seeds = []
	hello = []
	for s in range(0,5):
		seeds.append(random.randint(0,5000))
	# preprocessing of dictionary file
	for word in open("./dict", "r"):

		real.append(word.rstrip())
		for s in seeds:
			hashRes.append(mmh3.hash(word.rstrip(), s))
			hashs[mmh3.hash(word.rstrip(), s) % w] = 1
			if word == "hello":
				hello.append(mmh3.hash(word.rstrip(), s) % w)
	
	
	# generate 100 random 5-letter strings
	strings = []
	for s in range(0, 100):
		word = ""
		for i in range(0,5):
			num = random.randint(65,122)
			word = word + chr(num)
		strings.append(word)

	# strings = []
	# strings.append("hello")
	# strings.append("these")
	# strings.append("are")
	# strings.append("real")
	# strings.append("words")
	# strings.append("zzz")
	# strings.append("balloon")
	# strings.append("food")
	# strings.append("keyboard")
	# strings.append("computer")
	# strings.append("room")
	# strings.append("book")
	# strings.append("awsedrftgyhujidrtyfgjgseg")

	#true or false array for hashing strings
	resultOfHash = []
	def checkWord(word):
		for s in seeds:
			if hashs[mmh3.hash(word, s) % w] == 0:
				return False
		return True


	for word in strings:
		resultOfHash.append(checkWord(word))

	heloo2 = []
	for s in seeds:
		heloo2.append(mmh3.hash("hello", s) % w)

	falsePositive = 0
	total = 0.0000000

	for s in range(0, len(resultOfHash)):
		if resultOfHash[s] == True:
			#check if this is in real
			if strings[s] not in real:
				print strings[s] 
				falsePositive+=1
			total += 1

	print "Rate of False Positive: " + str(falsePositive/total)

	#print real
main()

