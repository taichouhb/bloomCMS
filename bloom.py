import random

# declare hash and initialize all bits to 0


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

def main():
	hashs = []
	w = 400000/24
	for i in range(w):
		hashs.append(0)

	# generate random hash family
	a = []
	b = []
	p = []

	library = dict()
	previousPrime = 2
	real = []

	for i in range(33,126):
		nexts = nextPrime(previousPrime)
		library[chr(i).decode('utf-8')] = nexts
		previousPrime = nexts

	for x in range(0, 5): # num hash functions
		prime = getRandPrime(330000, 9999999)
		p.append(prime) # stream size, uppper bound
		a.append(random.randint(0, prime - 1))
		b.append(random.randint(1, prime - 1))

	# preprocessing of dictionary file
	for word in open("./dict", "r"):
		real.append(word)
		#print word
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
		for ha in range(0,len(a)-1): #loop through each hash function
			hashs[((((a[ha]+b[ha]*product))% p[ha]) % w)] = 1

	print hashs
	#generate 100 random 5-letter strings
	strings = []
	for s in range(0, 100):
		word = ""
		for i in range(0,5):
			num = random.randint(65,122)
			word = word + chr(num)
		strings.append(word)

	#treu or false array for hashing strings
	resultOfHash = []

	for word in strings:
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
		falseInstance = True
		for ha in range(0, len(a)-1):
			if hashs[((((a[ha]+b[ha]*product))% p[ha]) % w)] == 0:
				if falseInstance == True:
					resultOfHash.append(False)
					falseInstance = False
		if falseInstance == True:
			resultOfHash.append(True)



	print resultOfHash

	print strings	

main()

