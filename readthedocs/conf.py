import os
import subprocess
import tempfile

for pkg in ['pr_bgl','ompl_lemur']:
   
   # generate doxygen output into subfolder
   fd,filename = tempfile.mkstemp(text=True)
   fp = os.fdopen(fd,'w')
   fp.write('''
PROJECT_NAME = "{pkg}"
INPUT = ../{pkg}
RECURSIVE = YES
GENERATE_HTML = YES
GENERATE_LATEX = NO
OUTPUT_DIRECTORY = _build/html/{pkg}
HTML_OUTPUT = .
'''.format(pkg=pkg))
   fp.close()

   print('file contents ...')
   subprocess.check_call(['cat',filename])

   print('calling doxygen {} ...'.format(filename))
   subprocess.check_call(['doxygen',filename])

#exit()
