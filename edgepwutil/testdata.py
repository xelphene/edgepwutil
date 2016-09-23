
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


# for testing: some passwords and their hashes tested against a real edge
knownGoodHashes = [
	('$QR9k|!>TCHN#s'            ,'{S}SZ6WcC01ZHoylDicbCM='),
	('M+<KWB.;8jVL5-~=IJZYg6^_'  ,'{S}IGR4gpGLa39ePSaeen07b52TKZEic4oo'),
	("xiFjC)^oq8@pVD'.-w"        ,'{S}lSaCI4VgmyuXbzAimZRifHku'),
	('OW+m?,>:|/{(Tk'            ,'{S}IphvJHlle36aeIt6mzs='),
	("+8#RMKQ"                   ,'{S}Rndnm4uClA=='),
	('IF7p6DmV;'                 ,'{S}JIlzOXCNKJJd'),
	('[OC@GNfTu#Jl|7e'           ,'{S}NoCHiYGHI5CTdDo+M2cg'),
	('Ks=e~*Lv0'                 ,'{S}Jjx5LDhjiTJW'),
	('V?BYSH=sFAgz5PC0'          ,'{S}O3CGkJWBeDcglpcoeoCGYg=='),
	('H7efc5N&jM(:z,'            ,'{S}JXghLyV8i2KMmlhoNXw='),
	('k[rRq.'                    ,'{S}hpQ2mzdn'),
	('For5_Q'                    ,'{S}KyA2fJmY'),
	('07-%Op@LkQ>tIPZ"w'         ,'{S}XXhpbIk5hYiNhk4mhoCfcCM='),
	('QV2*)g/5'                  ,'{S}PJl2Y28uanE='),
	(":\"=J%N{'h&ge^sMSY-(P72H"  ,'{S}V215g2OHPmOOcZc3kSOIgY10W5hyd5w='),
	('<J;Q6C_,1u!)@~eUX8vPp\\g'  ,'{S}UYV/mHCKmmhXIlF7jy4gh4xhhZg1mTM='),
	('5(Ftr'                     ,'{S}WGeCPTQ='),
	('#;T8R'                     ,'{S}TnSQcZQ='),
	("7MK'6ZAFRu*(^#bVCP3N]gn&G" ,'{S}WoKPbnCThII0Ilp6kXMnhJeJQIaYIjpRjg=='),
	(')$i_Mh6oNsz}ldwTg7"Xr.|*'  ,'{S}RGstloshcysoJIovIzQyhjNuUZA3ayhd'),
	('wH[u%^aqf'                 ,'{S}moefPGOXJDWA'),
	("k-u[P4I`'8]NU:fs?vylR"     ,'{S}hmIxkpZ9jCRBby2cmmojIWsviiSX'),
	(':y3R0IOZr@\'_*"JPUi}xhK'    ,'{S}VzZ3m3aAip6Ul1eNZXKPgoEwjjAtjg==')
]
