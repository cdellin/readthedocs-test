import os
import subprocess
import tempfile

for pkg in ['pr_bgl','ompl_lemur']:
   
   # generate doxygen output into subfolder
   fd,filename = tempfile.mkstemp(text=True)
   fp = os.odopen(fd)
   fp.write('''
PROJECT_NAME = "{pkg}"
INPUT = ../{pkg}
RECURSIVE = YES
GENERATE_HTML = YES
GENERATE_LATEX = NO
OUTPUT_DIRECTORY = _build/{pkg}
HTML_OUTPUT = .
'''.format(pkg=pkg))
   fp.close()

   subprocess.check_call(['doxygen',filename])

#exit()
