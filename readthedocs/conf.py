import os
print(os.listdir('.'))

with open('_build/html/index.html','w') as fp:
   fp.write('hello world!')

exit()
