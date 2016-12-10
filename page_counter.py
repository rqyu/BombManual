#!/usr/bin/python3
import subprocess
import sys, getopt

before = '''
<html class="no-js"><!--<![endif]--><head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8">

<meta http-equiv="X-UA-Compatible" content="IE=edge">
<title>Keep Talking and Nobody Explodes Example Manual Page</title>
<meta name="viewport" content="initial-scale=1"> 
<link href='http://fonts.googleapis.com/css?family=Special+Elite' rel='stylesheet' type='text/css'>
<link rel="stylesheet" type="text/css" href="http://www.bombmanual.com/manual/1/html/css/normalize.css">
<link rel="stylesheet" type="text/css" href="http://www.bombmanual.com/manual/1/html/css/main.css">
<style>
	tbody {
	font-size: 11pt;
	line-height: 14pt;
	}
	table {
	border: none;
	width: 100%;
	}
	td, th {
	border: none;
	}
	td {
	text-align: right;
	}
	.name {
	width:90%;
	text-align: left;
	}

	.original {
	color: green;
	}

	.needy {
	color: red;
	}
</style>
</head>
<body>
	<div class="section">
	<div class="page page-bg-01">
		<div class="page-header">
		<span class="page-header-doc-title">Keep Talking and Nobody Explodes Mod</span>
		<span class="page-header-section-title">Mod Index</span>
		</div>
		<div class="page-footer absolute-footer">Index 1 of 2</div>
		<div class="page-content">
		<h1>Index</h1>
		<p class="favour-test">Legends: <span class="needy">Red</span> are needy modules. <span class="original">Green</span> are original modules.</p>
		<table>
			<tbody>
'''


page_break = '''</tbody>
		</table>
		<div class="page-footer relative-footer">Index 1 of 2</div>
		</div>
	</div>

	<div class="section">
		<div class="page page-bg-01">
		<div class="page-header">
			<span class="page-header-doc-title">Keep Talking and Nobody Explodes Mod</span>
			<span class="page-header-section-title">Mod Index</span>
		</div>
		<div class="page-footer absolute-footer">Index 2 of 2</div>
		<div class="page-content">
			<h1>Index</h1>
			<p class="favour-test">Legends: <span class="needy">Red</span> are needy modules. <span class="original">Green</span> are original modules.</p>
			<table>
			<tbody>'''

after = ''' </tbody>
			</table>
			<div class="page-footer relative-footer">Index 2 of 2</div>
			</div>
		</div>

		</div>
	</body>
	</html>'''

for_future_uses = '''
fname = 'toc_cheat.py'
print_usage = lambda: print('usage: {} -i <inputfile> -o <outputfile>'.format(fname))

def main(argv):
	inputfile = ''
	outputfile = ''
	try:
		opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
	except getopt.GetoptError:
		print_usage()
		sys.exit(2)
	if opts == []:
		print_usage()
		sys.exit()
	for opt, arg in opts:
		if opt == '-h':
			print_usage()
			sys.exit()
		elif opt in ("-i", "--ifile"):
			inputfile = arg
		elif opt in ("-o", "--ofile"):
			outputfile = arg
		else:
			print_usage()
			sys.exit()

if __name__ == "__main__":
	main(sys.argv[1:])
'''

wd = './CHEATS'

p1 = subprocess.Popen(['ls'], cwd=wd, stdout=subprocess.PIPE)
p2 = subprocess.check_output(['wc', '-l'], cwd=wd, stdin=p1.stdout)
p1.stdout.close()
count = int(p2.strip())

p3 = subprocess.check_output(['ls', '-l'], cwd=wd)
lof = p3.decode('UTF-8').split('\n')

ofile = 'toc_cheat.html'

fout = open(ofile,'w')

fout.writelines(before)

page_count = 1
num_count = 1

space_replace = lambda s: ''.join(list(map(lambda x: '\\'+x if x == ' ' or x=='(' or x==')' else x, list(s))))

for i in lof:
	if num_count == 30:
		fout.writelines(page_break)
		num_count = 0
	try:
		a = i.split(':')[1][3:]
		a = a.strip()
		fout.write('<tr>\n<td class="name">{}</td>\n<td>{}</td>\n</tr>\n'.format(a, page_count))
		current_file_page = subprocess.check_output('mdls -name kMDItemNumberOfPages ./CHEATS/{}'.format(space_replace(a)), shell=True)
		current_file_page = int(current_file_page.strip().split()[-1])
		page_count += current_file_page
		num_count += 1
	except:
		pass
	

fout.writelines(after)
fout.close()