#Author: Diane Tam Ben Cheung

import re
tags = []
import heapq

with open('tweetstream.txt', 'r') as f:
	for line in f:
		# find the hashtags via regex...not sure how to do this using twitter api??
		ht = re.findall(r"#(\w+)", line)
		for h in ht:
			tags.append(h.lower())
	print len(tags)

#k is number of buckets
#m is the stream itself
def main(k, m):
	itemlist = []
	counter = []
	for c in range(0,k):
		itemlist.append(None)
		counter.append(0) 
	
	#process the first k items in the list
	for i in range(0, k):
		if m[i] not in itemlist:
			itemlist[i] = m[i]
			counter[i] = 1
		else:
			counter[itemlist.index(m[i])] =  counter[itemlist.index(m[i])] + 1

	#process the rest of the stream

	for x in range(k, len(m)):
		if m[x] in itemlist:
			counter[itemlist.index(m[x])] =  counter[itemlist.index(m[x])] + 1
		else:
			#check if list is full, if not then add x to the itemList
			found = False
			for item in range(0, len(itemlist)):
				if itemlist[item] is None and found==False:
					itemlist[item] = m[x]
					found = True
					counter[item] = 1

			if found==False:
				#decrement every counter
				for c in range(0, len(counter)):
					counter[c] = counter[c] - 1
					#if count hits 0
					if counter[c]==0:
						#remove value	
						itemlist[c] = None

	freqMap = {}
	items_and_freq = zip(itemlist, counter)

	for itemlist, counter in items_and_freq:
		freqMap[itemlist] = counter

	heap = [(-value, key) for key, value in freqMap.items()] 
	largest = heapq.nsmallest(k, heap)
	largest = [(key, -value) for value, key in largest]
	print largest


#testing
# print main(2, [1,2,2,3,3,1,1,1,3])
# print main(1, [2,3,4,4,1,7])
# print main(1, [1,2,2,3,3,1,1,1,3])

print main(500, tags)
#print main(100, tags)

