import pandas as pd
import sys
import numpy as np
import operator

try:
	cols = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O"]
	rib = pd.read_csv("./rib/rib.20140103.1200.txt" , sep="|", header=None, names=cols)
except:
	raise
	print("Unable to read file")
	sys.exit(1)

rib_data = list(set(rib["F"]))

session = "3"

intervals = [1200, 1215, 1230, 1245, 1300, 1315, 1330, 1345]

updates_data = []
update_messages = 0

for interval in intervals:
	filename = "./updates-asst4/updates.20140" + session + "03." + str(interval) + ".txt"

	try:
		print(filename)
		cols = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O"]
		data = pd.read_csv(filename , sep="|", header=None, names=cols)
	except:
		#raise
		print("Unable to read file")
		sys.exit(1)

	count = 0
	update_messages += len(data["F"])
	for entry in data["F"]:				# index "F" is the sixth column
		ent = entry.split()				# multiple prefixes in one update entry
		for e in ent:
			if ':' not in e:			# not ipv6
				updates_data += [e]	
	

print("This may take some time...")

ip_updates = {}
count = 0
for prefix in rib_data:
	if ":" not in prefix:
		ip_updates[prefix] = updates_data.count(prefix)
		if ip_updates[prefix] == 0:
			count += 1

print("count: ",count)
print("rib size: ", len(rib["F"]))
print("rib_data size(non-repititive: ",len(rib_data))
print("Total Update Messages: ", update_messages)
print("Fraction of IP prefixes experience no update messages: ", count/len(rib_data))

b = dict(sorted(ip_updates.items(), key=operator.itemgetter(1), reverse=True)[:10])
print(b)

fractions = [0.1, 1, 10]
for f in fractions:
	f = f/100
	a = dict(sorted(ip_updates.items(), key=operator.itemgetter(1), reverse=True)[:int(len(ip_updates)*f)])
	print("Sum of update messages for fraction ", f*100, ": ", sum(a.values()))
	print("Fraction of all update messages come from the most popular ", f*100," percent of prefixes: ", sum(a.values())/update_messages)
