
# About

edgepwutil can be used to generate hashes used in config files of Checkpoint
Edge firewalls.  It can also be used to reverse these hashes back to plain
text passwords.


# Installation

Requires: python 2.4 or higher

```
% python setup.py build
# python setup.py install
```

# Usage

## Generation

To generate hashes from plain text, simply run 'edgepwutil'. It will read
passwords from standard input and write hashes to standard output.

Examples:

```		
% echo password123 | edgepwutil
{S}nS43OjEmNyBXZUM=
%

% edgepwutil
password1
{S}nS43OjEmNyBX
password2
{S}nS43OjEmNyBU
^D
%
```

# Hash Reversal

To reverse hashes back to plain text, add '-r' to the command line. 
Hashes will then be read on stdin and plain text passowrds produced
on stdout. Valid hashes begin with "{S}".

If '-c' is given on the command line, an Edge Box configuration file
export will be read from standard input and all password hashes
found within it will be cracked and displayed on stdout in a
human-readable format with context.

## Examples:

```
% echo '{S}nS43OjEmNyBXZUM=' | edgepwutil -r
password123
%

% edgepwutil -c < 00_11_22_33_44_55.cfg
line | context                               | password
------------------------------------------------------------------
50   | 'set net wan mode pppoe gateway 192.' | asdf
215  | 'set vpn pkcs12 password {S}iXabc48/' | password1
222  | 'set users 1 namen password {S}XYZ98' | admin99
----------------------------------------------------------------------
total passwords found: 3
```


# Compatibility

We have tested or have heard that edgepwutil works against the following
Edge firmware versions:

* 6.5.48
* 7.0.48
* 7.5.48
* 7.5.55
* 8.0.24
* 8.0.35
* 8.0.36
* 8.0.39
    
As of 6 Nov 2009 we are not aware of any incompatible versions.

# Copyright and License

Copyright (C) 2009-2016 Hurricane Labs

edgepwutil was written by Steve Benson for Hurricane Labs.

edgepwutil is free software; you can redistribute it and/or modify it under
the terms of the GNU General Public License as published by the Free
Software Foundation; either version 3, or (at your option) any later
version.

edgepwutil is distributed in the hope that it will be useful, but WITHOUT ANY
WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more
details.

You should have received a copy of the GNU General Public License along with
this program; see the file LICENSE.  If not, see <http://www.gnu.org/licenses/>.
