
import distutils.core
import sys
import os

version=None
try:
	import edgepwutil.__init__
	version = edgepwutil.__init__.__version__
except:
	pass

distutils.core.setup(
	name="edgepwutil",
	version=version,
	description="Edge Box Password Utility",
	author="Hurricane Labs",
	author_email="steve@hurricanelabs.com",
	url="http://www.hurricanelabs.com/oss",
	packages=[
		'edgepwutil',
	],
	scripts=[
		'scripts/edgepwutil'
	],
)
