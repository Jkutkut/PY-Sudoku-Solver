# from pdflatex import PDFLaTeX


# f = open("doc.tex", "w")
# f.write("\documentclass{article}\n\begin{document}\n\end{document}")
# f.close()

# # pdfl = PDFLaTeX.from_texfile('doc.tex')
# pdfl = PDFLaTeX.from_texfile("doc.tex")
# print(pdfl.create_pdf())
# # p = pdfl.create_pdf(keep_pdf_file=True, keep_log_file=True)
# # pdf, log, completed_process = pdfl.create_pdf(keep_pdf_file=True, keep_log_file=True)

# # print(log)
# # print(completed_process)

import argparse
import os
import subprocess

content = r'''\documentclass{article}
\begin{document}
... P \& B 
\textbf{\huge %(school)s \\}
\vspace{1cm}
\textbf{\Large %(title)s \\}
...
\end{document}
'''

parser = argparse.ArgumentParser()
parser.add_argument('-c', '--course')
parser.add_argument('-t', '--title')
parser.add_argument('-n', '--name',) 
parser.add_argument('-s', '--school', default='My U')

args = parser.parse_args()

with open('cover.tex','w') as f:
    f.write(content%args.__dict__)

cmd = ['pdflatex', '-interaction', 'nonstopmode', 'cover.tex']
proc = subprocess.Popen(cmd)
proc.communicate()

retcode = proc.returncode
if not retcode == 0:
    os.unlink('cover.pdf')
    raise ValueError('Error {} executing command: {}'.format(retcode, ' '.join(cmd))) 

os.unlink('cover.tex')
os.unlink('cover.log')