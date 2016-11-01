from bitarray import bitarray 
import random 


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

def nextPrime(n):
		if isprime(n+1):
			return n+1
		else:
			return nextPrime(n+1)

def getRandPrime(p, q):
	n = random.randint(p, q)
	while not isprime(n):
	    n = random.randint(p, q)
	return n

def bloom():
	w = 3200000 #should roughly equate to 400 MB
	array = bitarray(w)
	a = []
	b = []
	p = []
	library = dict()
	previousPrime = 2
	real = []

	for i in range(33,127):
		nexts = nextPrime(previousPrime)
		library[chr(i).decode('utf-8')] = nexts
		previousPrime = nexts

	for x in range(0, 5): # num hash functions
		prime = getRandPrime(340000, 9999999)
		p.append(prime) # stream size, uppper bound
		a.append(random.randint(0, prime - 1))
		b.append(random.randint(1, prime - 1))

	#dict of words to hash values
	prePrcessValue = dict()

	for word in open("./dict", "r"):
		real.append(word)
		product = 1 
		for c in word:
			try: 
				if c.decode('utf-8') not in library :
					nexts = nextPrime(previousPrime)
					library[c.decode('utf-8')] = nexts
					previousPrime = nexts
				product = product*library[c.decode('utf-8')]
			except UnicodeDecodeError:
				#print "Skipping this illegal character"
				s=1

		#hash the product
		for ha in range(0,len(a)): #loop through each hash function
			indextoHash = ((((a[ha]+b[ha]*product))% p[ha]) % w)
			if word in prePrcessValue:
				prePrcessValue[word].append(indextoHash)
			else:
				prePrcessValue[word] = [indextoHash]
			array[indextoHash] = True

	print "# True: " + str(array.count(True))
	print "# False: " + str(array.count(False))

	strings = []
	strings.append("hello")
	strings.append("these")
	strings.append("are")
	strings.append("real")
	strings.append("words")
	strings.append("zzz")
	strings.append("balloon")
	strings.append("food")
	strings.append("keyboard")
	strings.append("computer")
	strings.append("room")
	strings.append("book")
	strings.append("awsedrftgyhujidrtyfgjgseg")

	resultOfHash = []
	def checkWord(word):
		product = 1 
		for c in word:
			try: 
				if c.decode('utf-8') not in library :
					nexts = nextPrime(previousPrime)
					library[c.decode('utf-8')] = nexts
					previousPrime = nexts
				product = product*library[c.decode('utf-8')]
			except UnicodeDecodeError:
				#print "Skipping this illegal character"
				s=1
		for ha in range(0, len(a)):
			if array[((((a[ha]+b[ha]*product))% p[ha]) % w)] == False:
				return False
		
		return True

	for word in strings:
		resultOfHash.append(checkWord(word))

	print resultOfHash 


bloom()