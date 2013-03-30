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

import re

from coret_fake import *
from coret_log import *

from coret_command import *

import coret_std_unix

# Koret Honey ;)

uname_re = re.compile("uname(\ )*.*")
ls_re = re.compile("ls(\ )*.*")
su_re = re.compile("su(\ )*.*")
passwd_re = re.compile("passwd(\ )*.*")

denied_re = re.compile("""
(cat(\ )*.*)|(chgrp(\ )*.*)|(chmod(\ )*.*)|(chown(\ )*.*)|(cp(\ )*.*)|(cpio(\ )*.*)|(csh(\ )*.*)|(date(\ )*.*)|
(dd(\ )*.*)|(df(\ )*.*)|(ed(\ )*.*)|(echo(\ )*.*)|(grep(\ )*.*)|(false(\ )*.*)|(hostname(\ )*.*)|(kill(\ )*.*)|(ln(\ )*.*)|
(login(\ )*.*)|(mkdir(\ )*.*)|(mknod(\ )*.*)|(mktemp(\ )*.*)|(more(\ )*.*)|(cd(\ )*.*)|(mount(\ )*.*)|(more(\ )*.*)|
(mv(\ )*.*)|(ping(\ )*.*)|(ps(\ )*.*)|(rmdir(\ )*.*)|(sed(\ )*.*)|(sh(\ )*.*)|(bash(\ )*.*)|(tar(\ )*.*)|(su(\ )*.*)|(true(\ )*.*)|
(umount(\ )*.*)|(useradd(\ )*.*)|(grpadd(\ )*.*)""", re.VERBOSE)

def processCmd(data, transport):

    global FAKE_SHELL, con

    retvalue = 1
    print "COMMAND IS : " + data
    transport.write('\r\n')

    if uname_re.match(data):
        transport.write(FAKE_OS)
    elif ls_re.match(data):
        for line in FAKE_LS:
            transport.write(line + '\r\n')
    elif data == "exit":
        transport.loseConnection()
    elif data == "w":
        for line in FAKE_W:
            transport.write(line + '\r\n')
    elif data == "who":
        transport.write(FAKE_USER)
    elif data == "ftp ..":
        for line in FAKE_FTP:
            transport.write(line + '\r\n')
    elif su_re.match(data):
        pass
    #elif data == "":
    #    pass
    elif passwd_re.match(data):
        transport.write('geteuid: _getuid: Invalid operation')
    elif denied_re.match(data):
        #
        # Patch from Nicolas Surribas to fix bug 1463713
        #
        transport.write(FAKE_SHELL+ data.split(" ")[0] + ": " + FAKE_DENIED)
    else:
        if data == "":
            return 0

        result_data = ""
        try:
            result_data = executeCommand(data.split())
            
            if type(result_data) is bool:
                if not result_data:
                    transport.write(FAKE_SHELL + ": " + str(data.split()[0]) + ": command not found")
        except:
            print "Internal error:", data, ":",str(sys.exc_info()[1])
            transport.write(FAKE_SHELL + ": " + str(data.split()[0]) + ": command not found")
        
        data = ""

        if type(result_data) is not bool and result_data != "":
            transport.write(result_data)
            
        return retvalue
