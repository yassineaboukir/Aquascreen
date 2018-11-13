import os, argparse, sys, json

def parse_args():
	parser = argparse.ArgumentParser(epilog='\tExample: \r\npython ' + sys.argv[0] + " -d example.com")
	parser._optionals.title = "OPTIONS"
	domain = parser.add_argument('-d', '--domain', help="Target", required=True)
	return parser.parse_args()

args = parse_args()
domain = args.domain

def aqua():
	# Browse to Aquatone results and dump the subdomains to webscreenshot directory as a new file
	with open("/Users/yassineaboukir/aquatone/" + domain + "/hosts.json") as hosts:
		jsondata = json.loads(hosts.read())
		for key in jsondata.keys():
			with open("/Users/yassineaboukir/desktop/tools/webscreenshot/" + domain + ".txt", "a") as extract:
				extract.write(key + "\n")

def screenshot():
	# Execute Webscreenshot python script to start taking screenshots of the dumped subdomains from Aquatone
	path = '/Users/yassineaboukir/desktop/tools/webscreenshot/webscreenshot.py -i /Users/yassineaboukir/desktop/tools/webscreenshot/'+domain+'.txt -o /Users/yassineaboukir/desktop/tools/webscreenshot/'+domain+' -w 5'
	os.system('python ' + path)

if __name__ == '__main__':
	aqua()
	screenshot()
