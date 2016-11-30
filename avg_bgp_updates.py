import pandas as pd
import sys
import numpy as np

session = "1"

intervals = [1200, 1215, 1230, 1245, 1300, 1315, 1330, 1345]

updates = []

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
	for aw, entry in zip(data["C"], data["F"]):			# index "F" is the sixth column
		if aw == "A" or aw == "W":
			ent = entry.split()			# multiple prefixes in one update entry
			for e in ent:
				if ':' not in e:	# not ipv6
					count += 1
	updates += [count]

print(updates)
print(sum(updates))
print("Average BGP updates per minute: ", sum(updates)/120)


