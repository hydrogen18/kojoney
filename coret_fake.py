#
# Use the '#' if you want to emulate root
#

FAKE_SSH_SERVER_VERSION = "SSH-2.0-OpenSSH_3.8.1p1"

FAKE_USER_CHAR = "$"

#FAKE_OS = "OpenBSD bigturd 2.5 GENERIC#172 sparc"
#FAKE_OS = "FreeBSD myname.my.domain 3.3-STABLE FreeBSD 3.3-STABLE #8: Fri Dec 17"
#FAKE_OS =  NetBSD pc164 1.4P NetBSD 1.4P (PC164.v6-intl) #5: Sat Nov 27 18:31:37 CET 1999 root@pc164:/usr/src/sys/arch/alpha/compile/PC164.v6-intl alpha"
#FAKE_OS = "OpenBSD 2.1 (TWP) #3: Sat Jul 19 18:37:43 CDT 1997
FAKE_OS = "Linux webtest 2.6.9-5.ELsmp #1 SMP Wed Jan 5 19:30:39 EST 2005 i686 i686 i386 GNU/Linux"

FAKE_SHELL = "bash-2.0"
FAKE_PROMPT = FAKE_SHELL + str(FAKE_USER_CHAR) + " "
FAKE_USER = "admin"

FAKE_W = ("USER     TTY      FROM              LOGIN@   IDLE   JCPU   PCPU WHAT",
": Permission denied"
)

FAKE_LS = ("drwxr-xr-x    2 root root   4096 2005-06-06 07:00 bin",
"drwxr-xr-x    3 root root   4096 2005-06-25 16:13 boot",
"drwxr-xr-x   10 root root  14320 2005-07-10 22:19 dev",
"drwxr-xr-x  100 root root   4096 2005-07-11 20:31 etc",
"drwxr-xr-x   10 root root   8192 2005-07-10 01:33 lib",
"drwxr-xr-x    2 root root  49152 2005-05-14 18:47 lost+found",
"drwxr-xr-x    3 root root   4096 2005-07-06 23:11 opt",
"drwxr-xr-x    3 root root   4096 2005-07-06 04:30 oracle",
"drwxr-xr-x    3 root root   4096 2005-07-06 01:51 personal",
"drwxr-xr-x    3 root root   4096 2005-07-06 22:41 pr0n",
"drwxr-xr-x    3 root root   4096 2005-07-06 23:44 private",
"drwxr-xr-x    2 root root   4096 2005-07-10 01:33 sbin",
"drwxr-xr-x    3 root root   4096 2005-07-06 23:11 secure_firewall_ltd",
"drwxr-xr-x    2 root root   4096 2005-05-14 18:49 srv",
"drwxr-xr-x   10 root root      0 2005-07-11 00:08 sys",
"drwxrwxrwt   11 root root   4096 2005-07-11 21:17 tmp",
"drwxr-xr-x   14 root root   4096 2005-07-10 15:52 usr",
"drwxr-xr-x   14 root root   4096 2005-06-06 07:02 var",
"drwxr-xr-x   14 root root   4096 2005-06-06 07:02 videos",
"lrwxrwxrwx    1 root root     25 2005-06-25 16:13 vmunix -> boot/vmunix-2.5-172"
)
FAKE_WGET = "--00:32:24--  http://../","           => `index.html'", "Resolviendo ..... fallo: No se ha encontrado el anfitrion."
FAKE_FTP = "ftp: ..: No address associated with name", "ftp> "
FAKE_USERS_FILES = [ "./fake_users", "/etc/kojoney/fake_users"]
FAKE_RM = "rm: Permission denied"
FAKE_TOUCH = "touch: Permission denied"
FAKE_DENIED = "Permission denied"

SERVER_PUBLIC_KEY_FILE = "./publicKey"
SERVER_PRIVATE_KEY_FILE = "./privateKey"
