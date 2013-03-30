"""
    Kojoney - A honeypot that emules a secure shell (SSH) server.
    Copyright (C) 2005 Jose Antonio Coret

    This program is free software; you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation; either version 2 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program; if not, write to the Free Software
    Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA
"""
import sys
import errno
from coret_fake import FAKE_USERS_FILES

def add_users(passwdDB):

    for path in FAKE_USERS_FILES:
	try:
            with open(path,"r") as file:
                for i,line in enumerate(file):
                    data = line.split(' ')
                    try:
                        passwdDB.addUser(data[0], data[1].rstrip())
                    except:
                        print "Error in fake users file at line " + str(i)
                        print sys.exc_info()[1]
        except IOError as e: 
            if e.errno != errno.ENOENT:
                raise e
