
import sys
import re

import edgepwutil.forward
import edgepwutil.reverse
import edgepwutil

from edgepwutil.forward import PasswordLengthError
from edgepwutil.reverse import InvalidHashError, DecryptionError

def confFileExtract(f):
	hashRE = re.compile('({S}[/=a-zA-Z0-9]+)')

	print 'line | context                                    | password'
	print '-'*70

	lineno=0
	extcount=0
	for line in f:
		lineno+=1
		mg = hashRE.search(line)
		if mg:
			#print mg.group(1)
			try:
				ptpassword = edgepwutil.reverse.edgeCrack(mg.group(1))
			except DecryptionError, de:
				ptpassword = str(de)
			
			print '%-4d | %-40s | %s' % (
				lineno, 
				repr(line[0:40]), 
				ptpassword
			)
			extcount+=1
	print '-'*70
	print 'total passwords found: %d' % extcount

def main():
	forward=True
	
	if '-t' in sys.argv:
		print '===== FORWARD ================'
		edgepwutil.forward.test()
		print '===== REVERSE ================'
		edgepwutil.reverse.test()
		return
	elif '-v' in sys.argv:
		print 'edgepwutil v%s' % edgepwutil.__version__
		return
	elif '-h' in sys.argv:
		print 'Enter plain text passwords on stdin. Their hashes will be produced on stdout until EOF.'
		print ' -c: search an edge config file on stdin for all passwords'
		print ' -h: this text'
		print ' -r: reverse hashes. take hases on stdin and write plaintext to stdout.'
		print ' -t: run internal tests'
		print ' -v: print version'
		return
	elif '-c' in sys.argv:
		confFileExtract(sys.stdin)
		return
	elif '-r' in sys.argv:
		forward=False
	
	try:
		line = sys.stdin.readline()
		while line:
			if line[-1]=='\n':
				line = line[:-1]
			if forward:
				try:
					print edgepwutil.forward.edgeHash(line)
				except PasswordLengthError, e:
					print e
			else:
				try:
					print edgepwutil.reverse.edgeCrack(line)
				except InvalidHashError, e:
					print 'Error:',e
				except DecryptionError, de:
					print 'Error:',de
			line = sys.stdin.readline()
	except KeyboardInterrupt:
		pass

