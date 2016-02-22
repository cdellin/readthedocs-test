import os
import subprocess
import tempfile

# in dependency order
pkgs = ['pr_bgl','ompl_lemur']
for ipkg,pkg in enumerate(pkgs):
   
   tagfiles=' '.join(['_build/html/{p}.tag=../{p}'.format(p=p) for p in pkgs[:ipkg]])
   
   # temp folder
   fn_tmpdir = tempfile.mkdtemp()
   fn_config = '{}/config.txt'.format(fn_tmpdir)
   fn_header = 'header.html'
   fn_footer = 'footer.html'
   fn_style = 'style.css'
   
   fp = open(fn_config,'w')
   fp.write('''
PROJECT_NAME = "{pkg}"
INPUT = ../{pkg}
RECURSIVE = YES
GENERATE_LATEX = NO
GENERATE_HTML = YES
OUTPUT_DIRECTORY = _build/html/{pkg}
HTML_OUTPUT = .
HTML_HEADER = {fn_header}
HTML_FOOTER = {fn_footer}
HTML_STYLESHEET = {fn_style}
TAGFILES = {tagfiles}
GENERATE_TAGFILE = _build/html/{pkg}.tag
'''.format(**locals()))
   fp.close()
   
   # generate doxygen html headers/footers
   subprocess.check_call(['doxygen','-w','html',fn_header,fn_footer,fn_style,fn_config])
   
   # add css
   fp = open(fn_style,'a')
   fp.write('''
.mybtn {
display:inline-block;
background-color:#333333;
color: #FFFFFF;
padding: 3px 15px;
text-align: center;	
text-decoration: none;
margin-left:5px;
}
.mybtn-current {
display:inline-block;
background-color:#333388;
color: #FFFFFF;
padding: 3px 15px;
text-align: center;	
text-decoration: none;
margin-left:5px;
}
.mybtn:hover {
color:white;
background-color:#5555CC;
opacity:1;
}''')
   fp.close()
   
   # modify header
   headerhtml = open(fn_header).read()
   a,_ = headerhtml.split('<!--BEGIN TITLEAREA-->')
   _,b = headerhtml.split('<!--END TITLEAREA-->')
   fp = open(fn_header,'w')
   fp.write(a)
   fp.write('''<div id="titlearea" style="background-color:#000000;padding-left:5px;color:white;font-size:14px;">LEMUR Packages:\n''')
   for otherpkg in sorted(pkgs):
      if otherpkg == pkg:
         fp.write('<a href="../{}/index.html" class="mybtn-current">{}</a>\n'.format(otherpkg,otherpkg))
      else:
         fp.write('<a href="../{}/index.html" class="mybtn">{}</a>\n'.format(otherpkg,otherpkg))
   fp.write('''<br style="clear:left;" /></div>\n''') # titlearea
   fp.write(b)
   fp.close()
   
   print('calling doxygen {} ...'.format(fn_config))
   subprocess.check_call(['doxygen',fn_config])
   
   os.remove(fn_config)
   os.remove(fn_header)
   os.remove(fn_footer)
   os.remove(fn_style)
   os.rmdir(fn_tmpdir)

# throw in an html redirect to ompl_lemur
fp = open('_build/html/index.html','w')
fp.write('''
<html>
<head>
<meta http-equiv="refresh" content="0; url=ompl_lemur/index.html" />
</head>
<body>
</body>
</html>
''')
fp.close()

# dump bogus contents.rst file
fp = open('contents.rst','w')
fp.close()
