import pandas as pd
import sys
import numpy as np
import matplotlib.pyplot as plt
import operator

def top_ten(port_list, octet_list, proto_list):
	_traffic ={}

	for port in list(set(port_list)):
		_traffic[int(port)] = 0

	print(len(_traffic))
	total_volume = 0 
	for port, vol, proto in zip(port_list, octet_list, proto_list):
		if  (int(proto) == 6) or (int(proto) == 17):
			_traffic[int(port)] += int(vol)
		total_volume += int(vol)

	for key in _traffic:
		_traffic[key] = (_traffic[key]/total_volume)*100

	return sorted(_traffic.items(), key=operator.itemgetter(1), reverse=True)[:10]


def ip_traffic_fraction(ipaddr, octet_list, mask_list, masked, fractions):
	ip_traffic = {}
	for ip in list(set(ipaddr)):
		ip_traffic[ip] = 0

	total_traffic = 0
	for ip, octets, mask in zip(ipaddr, octet_list, mask_list):
		if masked:
			if mask != 0:
				ip_traffic[ip] += octets
		else:
			ip_traffic[ip] += octets
		total_traffic += octets

	for f in fractions:
		f = f/100
		a = dict(sorted(ip_traffic.items(), key=operator.itemgetter(1), reverse=True)[:int(len(ip_traffic)*f)])
		print("Fraction of the total traffic comes from the most popular ", f*100," percent of source IP prefixes: ", sum(a.values())/total_traffic)
	return 


def ip_traffic_zero_mask(octet_list, mask_list):
	res = 0
	tot = 0
	for oc, mask in zip(octet_list,mask_list):
		if mask == 0:
			res += oc
		tot += oc 
	print(tot)
	print(res)
	print("Fraction of traffic (by bytes) that has a source mask of 0", res/tot)


def specific_ip_traffic(ipaddr, _list, ip_string, addr_block):
	total_traffic = 0
	res = 0
	for ip, octets in zip(ipaddr, _list):
		if ip_string in ip[:addr_block]:
			res += octets
		total_traffic += octets
	print(total_traffic)
	print(res)

	return res/total_traffic


try:
	data = pd.read_csv("ft-v05.2010-09-29.235501+0000.csv")
except:
	print("Unable to read csv file")
	sys.exit(1)

sender = top_ten(data.srcport, data.doctets, data.prot)
reciever = top_ten(data.dstport, data.doctets, data.prot)
print("Top Ten Senders: ")
print(sender)
print("Top Ten Recievers: ")
print(reciever)

ip_traffic_fraction(data.srcaddr, data.doctets, data.src_mask, False, [0.1, 1, 10])

ip_traffic_zero_mask(data.doctets, data.src_mask)

print("Non zero mask traffic:")

ip_traffic_fraction(data.srcaddr, data.doctets, data.src_mask, True, [0.1, 1, 10])

p1 = specific_ip_traffic(data.srcaddr, data.doctets, "128.112", 16)
p2 = specific_ip_traffic(data.srcaddr, data.dpkts, "128.112", 16)
p3 = specific_ip_traffic(data.dstaddr, data.doctets, "128.112", 16)
p4 = specific_ip_traffic(data.dstaddr, data.dpkts, "128.112", 16)

print("fraction of the traffic (by bytes) in the trace is sent by Princeton: ", p1)
print("fraction of the traffic (by packets) in the trace is sent by Princeton: ", p3)
print("fraction of the traffic (by bytes) in the trace is to by Princeton: ", p2)
print("fraction of the traffic (by packets) in the trace is to by Princeton: ", p4)
