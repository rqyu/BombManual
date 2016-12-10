infile = 'toc_cheat.html'
outfile = 'toc_offset.html'
offset = 2

fo = open(outfile, 'w')

with open(infile) as openfile:
	for line in openfile:
		a = line
		wline = line
		if '<td>' in a:
			front,end = a.split('</')
			front2,mid = front.split('>')
			mid = offset + int(mid)
			wline = front2 + '>' + str(mid) + '</' + end
			print(wline)
		fo.write(wline)

fo.close()