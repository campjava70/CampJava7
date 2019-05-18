user = raw_input("username: ")

import getpass

sandi = getpass.getpass()

if sandi == 'CampJava7' and user == 'CampJava7':

   print "Kamu Berhasil Login"
   
else:

   print "username atau password salah Goblok!!!"