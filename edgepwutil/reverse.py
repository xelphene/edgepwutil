
__copyright__ = '''
Copyright (c) 2009, Hurricane Labs
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

    * Redistributions of source code must retain the above copyright notice,
      this list of conditions and the following disclaimer.

    * Redistributions in binary form must reproduce the above copyright
      notice, this list of conditions and the following disclaimer in the
      documentation and/or other materials provided with the distribution.

    * Neither the name of the author nor the names of its
      contributors may be used to endorse or promote products derived from
      this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE
LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
POSSIBILITY OF SUCH DAMAGE.
'''                                          


import base64

from edgepwutil.testdata import knownGoodHashes
from edgepwutil.keys import edgeKeys

# compute target sets for all positions
targets = {}
for i in range(0,25):
	targets[i] = {}
	for area in ('low','mid','high'):
		targets[i][area] = set()
	for j in range(0,64):
		targets[i]['low'].add( j ^ edgeKeys['low'][i] )
	for j in range(64,96):
		targets[i]['mid'].add( j ^ edgeKeys['mid'][i] )
	for j in range(96,128):
		targets[i]['high'].add( j ^ edgeKeys['high'][i] )
# make sure that's valid
for i in range(0,25):
	assert len( targets[i]['low'].intersection(targets[i]['mid']) ) ==0
	assert len( targets[i]['low'].intersection(targets[i]['high']) ) ==0
	assert len( targets[i]['mid'].intersection(targets[i]['high']) ) ==0

class DecryptionError(Exception):
	def __init__(self, reason):
		self.reason = reason

	def __str__(self):
		return 'Unable to decrypt: %s' % self.reason

def lookupKey(ctb, pos):
	cto = ord(ctb)
	if cto in targets[pos]['low']:
		return edgeKeys['low'][pos]
	elif cto in targets[pos]['mid']:
		return edgeKeys['mid'][pos]
	elif cto in targets[pos]['high']:
		return edgeKeys['high'][pos]
	else:
		raise DecryptionError('ciphertext byte %s not found in any target set' % repr(ctb))

class InvalidHashError(Exception):
	def __init__(self, hash):
		self.hash = hash
	
	def __str__(self):
		return "Invalid hash %s. Valid hashes start with '{S}'." % repr(self.hash)
		
def edgeCrack(hash):
	if not hash.startswith('{S}'):
		raise InvalidHashError(hash)
	hash = hash[3:]
	#print 'stripped:',repr(hash)
	hash = base64.b64decode(hash)
	#print 'decoded:',repr(hash)

	pt = ''
	for i in range(0,len(hash)):
		ctb = hash[i]
		cto = ord(hash[i])
		key = lookupKey(ctb, i)
		pt += chr(key^cto)
	return pt

def test():
	for (pt, hash) in knownGoodHashes:
		print 'try',repr(pt)
		assert pt == edgeCrack(hash)
