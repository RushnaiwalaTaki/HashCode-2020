file = open("input//a_example.in","r")
line1 = file.readline()										
MAX,NUM = [int(i) for i in line1.rstrip().split(" ")]	# Read The First Line
orders_line = file.readlines()
order, total_slice, SUM = [], [], 0
for i in orders_line:											# Read The Order Slice Lines.
	for j in i.rstrip().split(" "):
		order.append(int(j))
file.close()

if __name__ == '__main__':
	for i in reversed(range(0,len(order))):
		TEMP = SUM + order[i]
		if TEMP == MAX:
			SUM = TEMP
			total_slice.append(i)
		elif TEMP > MAX:
			continue
		elif TEMP < MAX:
			SUM = TEMP
			total_slice.append(i)
			continue
	total_slice.reverse()
	print(len(total_slice))
	print(*total_slice, sep =' ')
	del(order,TEMP,SUM,total_slice)	