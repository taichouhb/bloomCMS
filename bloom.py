import random
from bitarray import bitarray
# need a sudo pip install bitarray

#takes in a number and returns true or false if it is prime or not
def isprime(n):
    if n == 2:
        return True
    if n == 3:
        return True
    if n % 2 == 0:
        return False
    if n % 3 == 0:
        return False
    i = 5
    w = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += w
        w = 6 - w
    return True

#takes in a number and returns the next prime number in succession 
def nextPrime(n):
		if isprime(n+1):
			return n+1
		else:
			return nextPrime(n+1)

#returns a random prime number within the range
def getRandPrime(p, q):
	n = random.randint(p, q)
	while not isprime(n):
	    n = random.randint(p, q)
	return n

def main():
	#we are using bit arrays so the size is 32*10^5 for around a 400KB array 
	w = 3200000
	hashs = bitarray(w)
	hashs.setall(0)

	# generate random hash family
	a = []
	b = []
	p = []

	#library to map the ascii numbers to a unique prime number
	library = dict()
	previousPrime = 2
	real = []

	#preprocess all the normal ascii characters into library
	for i in range(33,127):
		nexts = nextPrime(previousPrime)
		library[chr(i).decode('utf-8')] = nexts
		previousPrime = nexts

	#generate hash function numbers into arrays a,b, and p
	for x in range(0, 100): # num hash functions
		prime = getRandPrime(340000, 9999999)
		p.append(prime) # stream size, uppper bound
		a.append(random.randint(0, prime - 1))
		b.append(random.randint(1, prime - 1))


	# preprocessing of dictionary file
	for word in open("./dict", "r"):
		real.append(word.rstrip())
		#convert each character of the current word to a prime number. 
		#prodcut is the the product of all the prime numbers of the characters mulitplied together
		product = 1 
		for c in word.rstrip():
			try: #some letters are too special and the decode function will give an error. so we just ignored them
				if c.decode('utf-8') not in library : #add the mapping to the library if the character did not already exist in the lib
					nexts = nextPrime(previousPrime)
					library[c.decode('utf-8')] = nexts
					previousPrime = nexts
				product = product*library[c.decode('utf-8')]
				
			except UnicodeDecodeError:
				#print "Skipping this illegal character"
				s=1 #just a placeholder for the exception 

		#hash the product
		for ha in range(0,len(a)): #loop through each hash function
			hashs[((((a[ha]+b[ha]*product))% p[ha]) % w)] = 1

	# generate 100 random 5-letter strings
	strings = []
	for s in range(0, 100):
		word = ""
		for i in range(0,5):
			num = random.randint(65,122)
			word = word + chr(num)
		strings.append(word)

	# strings.append("hello")
	# strings.append("these")
	# strings.append("are")
	# strings.append("real")
	# strings.append("words")
	# strings.append("zzzfddddddddddddddssgdfgdgftsedgf")
	# strings.append("balloon")
	# strings.append("food")
	# strings.append("keyboard")
	# strings.append("computer")
	# strings.append("room")
	# strings.append("book")
	# strings.append("awsedrftgyhujidrtyfgjgseg")

	#true or false array for hashing strings
	resultOfHash = []

	#returns true if the word is in the set 
	#false if not
	def checkWord(word):
		product = 1 
		for c in word: #redo product calculation on the randoml generated strings
			#same algorithm as above
			try: 
				if c.decode('utf-8') not in library :
					nexts = nextPrime(previousPrime)
					library[c.decode('utf-8')] = nexts
					previousPrime = nexts
					print "New Value being added to library  after preprocessing"
				product = product*library[c.decode('utf-8')]
			except UnicodeDecodeError:
				#print "Skipping this illegal character"
				s=1
		#check to see if the index of the product in the array has been hashed or not. 
		for ha in range(0, len(a)):
			if hashs[((((a[ha]+b[ha]*product))% p[ha]) % w)] == 0:
				return False
		return True

	for word in strings:
		resultOfHash.append(checkWord(word))

	falsePositive = 0.0000000
	total = 0.0000000
	#calculate false posistive
	for s in range(0, len(resultOfHash)):
		if resultOfHash[s] == True:
			#check if this is in real
			if strings[s] not in real:
				print strings[s] 
				falsePositive+=1
			total += 1

	print resultOfHash
	print strings

	#print the false positive rate
	
	print "rate of false pos 2: " + str(falsePositive/(1.00000*len(strings)))


main()

