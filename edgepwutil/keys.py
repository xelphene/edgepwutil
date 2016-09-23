
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

# the magic numbers that are the "key" to the edge password "encryption"
# these were reverse engineered via known plaintext
edgeKeys = {
	'low':  '109 79  68  73  70  73  69  68  102 87  112 82  79  80  69  82  84  89  115 72  69  69  84  119 73',
	'mid':  '109 207 196 201 198 201 197 196 102 215 112 210 207 208 197 210 212 217 115 200 197 197 212 119 201',
	'high': '237 79  68  73  70  73  69  68  230 87  240 82  79  80  69  82  84  89  243 72  69  69  84  247 73'
}
# turn values above into arrays of ints
for area in edgeKeys.keys():
	edgeKeys[area] = edgeKeys[area].split(' ')
	edgeKeys[area] = filter(lambda s: s!='', edgeKeys[area])
	edgeKeys[area] = [int(i) for i in edgeKeys[area]]

