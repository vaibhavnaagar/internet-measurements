import pandas as pd
import sys
import numpy as np
import matplotlib.pyplot as plt


def plot_ccdf(dataset, xstring, ystring, img, fig_num, log_scale):
	dataset.sort()
	xvals = np.array(list(set(dataset)))
	xvals.sort()

	counts = []
	c = 0
	d_prev = dataset[0]

	for d in dataset:
		if d_prev != d:
			d_prev = d
			counts = counts + [c]
			c = 1
		else:
			c += 1
	counts = counts + [c]

	assert len(counts) == len(xvals)

	cdf = np.cumsum(counts)

	assert len(dataset) == cdf[len(cdf)-1]

	yvals = 1 - cdf/float(len(dataset)) 
		
	if log_scale:
		xvals = np.log(xvals)
		yvals = np.log(yvals)
	else:
		xvals = np.append([xvals[0]-1], xvals)
		yvals = np.append([1],yvals)
		xvals = np.append([xvals[0]-1], xvals)
		yvals = np.append([1],yvals)


	assert len(xvals) == len(yvals)

	plt.figure(fig_num)
	plt.plot(xvals,yvals, color="green")
	plt.xlabel(xstring)
	plt.ylabel(ystring)
#	plt.show()
	plt.savefig(img)


try:
	data = pd.read_csv("ft-v05.2010-09-29.235501+0000.csv")
except:
	print("Unable to read csv file")
	sys.exit(1)

# extract number of packets in the flow <dpkts>
dpkts = data.dpkts

# extract bytes in the flow <doctets>
doctets = data.doctets

assert len(dpkts) == len(doctets)

packet_list = [int(pk) for pk in dpkts]
octets_list = [int(oc) for oc in doctets]

avg = sum(octets_list)/sum(packet_list)

print("Total Size: ", sum(octets_list))
print("Number of Samples: ", len(doctets))
print("Average Packet Size: ", avg) 

finish = data['last']
start = data['first']

assert len(finish) == len(start)

durations = [f-s for f,s in zip(finish, start)]

plot_ccdf(durations, "Flow Duration (last-first)", "CCDF", "traffic_q1.2.1.png", 1, False)
plot_ccdf(durations, "Flow Duration (last-first)", "CCDF", "traffic_q1.2.1_log.png", 2, True)

plot_ccdf(packet_list, "Flow Size (Number of packets)", "CCDF", "traffic_q1.2.2.png", 3, False)
plot_ccdf(packet_list, "Flow Size (Number of packets)", "CCDF", "traffic_q1.2.2_log.png", 4, True)

plot_ccdf(octets_list, "Flow Size (Number of Bytes)", "CCDF", "traffic_q1.2.3.png", 5, False)
plot_ccdf(octets_list, "Flow Size (Number of Bytes)", "CCDF", "traffic_q1.2.3_log.png", 6, True)
