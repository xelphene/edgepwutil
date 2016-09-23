
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

class PasswordLengthError(Exception):
	def __init__(self, password):
		self.password = password

	def __str__(self):
		return 'Password is too long (%d chars; must be at most 25)' % len(self.password)

def edgeHash(pt):
	"""take a plain text password pt and return an Edge hash for it"""
	if len(pt)>25:
		raise PasswordLengthError(pt)
	hash = ''
	for i in range(0,len(pt)):
		c_pt = ord(pt[i])
		if c_pt < 64:
			area = 'low'
		elif c_pt >=64 and c_pt < 96:
			area = 'mid'
		else:
			area = 'high'
		
		key = edgeKeys[area][i]
		c_ct = c_pt ^ key

		hash += chr(c_ct)

	return '{S}'+base64.b64encode(hash)

def test():
	for pt, ct in knownGoodHashes:
		print 'edgeHash(%s) == %s' % (repr(pt), repr(ct))
		assert edgeHash(pt) == ct
	print 'OK'

