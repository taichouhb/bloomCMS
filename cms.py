#Author: Diane Tam Ben Cheung
import random
import re

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
	tags = []

	f = open('tweetstream.txt', 'r')
	for line in f:
		# find the hashtags via regex...not sure how to do this using twitter api??
		ht = re.findall(r"#(\w+)", line)
		for h in ht:
			tags.append(h.lower())
	#print tags

	#map ascii letters to unique prime numbers
	previousPrime = 2
	library = dict()
	for i in range(33,126):
		nexts = nextPrime(previousPrime)
		library[i] = nexts
		previousPrime = nexts

	a = []
	b = []
	p = []

	for x in range(0, 6): # num hash functions
		prime = getRandPrime(len(tags), 99999999)
		p.append(prime) # stream size, uppper bound
		a.append(random.randint(0, prime - 1))
		b.append(random.randint(1, prime - 1))

	h1 = []
	h2 = [] 
	h3 = []
	h4 = []
	h5 = []
	h6 = []

	# w = int(2.72*5600000000 )
	w = 5000000
	for i in range(0, w):
		h1.append(0)
		h2.append(0)
		h3.append(0)
		h4.append(0)
		h5.append(0)
		h6.append(0)
		
	for t in tags:
		#get the unique prime value from string
		product = 1
		for c in t:
			product = product * library[ord(c)]
		#for each hash function, hash the value

		h1[((((a[0]+b[0]*product))% p[0])%w)] += 1
		h2[((((a[1]+b[1]*product))% p[1])%w)] += 1
		h3[((((a[2]+b[2]*product))% p[2])%w)] += 1
		h4[((((a[3]+b[3]*product))% p[3])%w)] += 1
		h5[((((a[4]+b[4]*product))% p[4])%w)] += 1
		h6[((((a[5]+b[5]*product))% p[5])%w)] += 1

	freq = []
	for f in range(0, len(tags)+1):
		freq.append(0)
	item = 0
	for t in tags:
		#get the unique prime value from string
		product = 1
		for c in t:
			product = product * library[ord(c)]
		#for each hash function, hash the value

		v1 = h1[((((a[0]+b[0]*product))% p[0])%w)]
		v2 = h2[((((a[1]+b[1]*product))% p[1])%w)]
		v3 = h3[((((a[2]+b[2]*product))% p[2])%w)]
		v4 = h4[((((a[3]+b[3]*product))% p[3])%w)]
		v5 = h5[((((a[4]+b[4]*product))% p[4])%w)]
		v6 = h6[((((a[5]+b[5]*product))% p[5])%w)]

		item += 1
		freq[item] = min(v1, v2, v3, v4, v5, v6)
		# print freq[item]
	result = []
	for i in range(0, len(freq)):
		if freq[i] > 0.002*len(tags):
			if tags[i] not in result:
				result.append(tags[i])
	print result
main()




