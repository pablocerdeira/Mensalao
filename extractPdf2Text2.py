# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


import pyPdf

print 'Opening PDF file'
pdf = pyPdf.PdfFileReader(open("Docs/10QO_AP470.pdf", "rb"))

print 'Opening TXT file'
txt = open("Docs/10QO_AP470.txt","a")

for page in pdf.pages:
    txt.write(page.extractText())

print 'Saving TXT file'
txt.close
 

