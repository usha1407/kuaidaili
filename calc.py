import json
from collections import Counter

with open('kuaidaili.json') as f:
	data = json.loads(f.read())

# print(type(data))
# print(len(data))
# print(data[:3])
all_port = {}
count = 0
for ip in data:
	port = ip['port']
	if port:
		all_port[port] = all_port.get(port, 0) + 1
	count += 1

# print(all_port)
# print(count)

most_ports = Counter(all_port).most_common(10)
#print(most_ports)
for item in most_ports:
	#print("'%s'," % item[0], end='')
	print('%d, ' % item[1], end='')

