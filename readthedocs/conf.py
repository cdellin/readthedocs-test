import os
import subprocess

print(os.listdir('.'))

with open('_build/html/mypage.html','w') as fp:
   fp.write('hello world!')

subprocess.check_call(['doxygen'])

#exit()
