#Author: Diane Tam Ben Cheung
import random
import re
import heapq
import mmh3


def main():
	tags = []
	with open('tweetstream.txt', 'r') as f:
		for line in f:
			# find the hashtags via regex...not sure how to do this using twitter api??
			ht = re.findall(r"#(\w+)", line)
			for h in ht:
				tags.append(h.lower())

	h1 = []
	h2 = [] 
	h3 = []
	h4 = []
	h5 = []
	h6 = []
	seeds = []
	for s in range(0,6):
		seeds.append(random.randint(0,5000))

	# w = int(2.72*5600000000 )

	w = int(2.72/0.001)
	for i in range(0, w):
		h1.append(0)
		h2.append(0)
		h3.append(0)
		h4.append(0)
		h5.append(0)
		h6.append(0)
		
	for t in tags:
	
		
		#for each hash function, hash the value
	
		h1[mmh3.hash(t,seeds[0]) % w] += 1
		h2[mmh3.hash(t,seeds[1]) % w] += 1
		h3[mmh3.hash(t,seeds[2]) % w] += 1
		h4[mmh3.hash(t,seeds[3]) % w] += 1
		h5[mmh3.hash(t,seeds[4]) % w] += 1
		h6[mmh3.hash(t,seeds[5]) % w] += 1

	freq = []
	for f in range(0, len(tags)+1):
		freq.append(0)
	item = 0
	for t in tags:
		
		#for each hash function, hash the value

		v1 = h1[mmh3.hash(t, seeds[0])%w]
		v2 = h2[mmh3.hash(t, seeds[1])%w]
		v3 = h3[mmh3.hash(t, seeds[2])%w]
		v4 = h4[mmh3.hash(t, seeds[3])%w]
		v5 = h5[mmh3.hash(t, seeds[4])%w]
		v6 = h6[mmh3.hash(t, seeds[5])%w]

		freq[item] = min(v1, v2, v3, v4, v5, v6)
		item += 1

	result = []
	for i in range(0, len(freq)):
		if freq[i] > 0.002*len(tags):
			if tags[i] not in result:
				result.append(tags[i])

	# print freq
	# print result

	freqMap = {}
	tags_and_freq = zip(tags, freq)
	# for f in range(0, len(freq)):
	# 	freqMap[tags[f]] = freq[f]

	# print tags_and_freq
	for tags, freq in tags_and_freq:
		freqMap[tags] = freq
	# print freqMap
	heap = [(-value, key) for key, value in freqMap.items()] 
	largest = heapq.nsmallest(100, heap)
	largest = [(key, -value) for value, key in largest]
	print largest

main()




