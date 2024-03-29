# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

def pdf_to_text(data): 
    from pdfminer.pdfinterp import PDFResourceManager, process_pdf 
    from pdfminer.pdfdevice import PDFDevice 
    from pdfminer.converter import TextConverter 
    from pdfminer.layout import LAParams 

    import StringIO 
    fp = StringIO.StringIO() 
    fp.write(data) 
    fp.seek(0) 
    outfp = StringIO.StringIO() 
    
    rsrcmgr = PDFResourceManager() 
    device = TextConverter(rsrcmgr, outfp, laparams=LAParams()) 
    process_pdf(rsrcmgr, device, fp) 
    device.close() 
    
    t = outfp.getvalue() 
    outfp.close() 
    fp.close() 
    return t 


print 'Opening PDF file'
pdf = open("Docs/InteiroTeor_AP470.pdf","r")
print 'Opening TXT file'
txt = open("InteiroTeor_AP470.txt","w")
print 'Converting PDF to txt'
text = pdf_to_text(pdf.read())
print 'Writing TXT file'
txt.write(text)
print 'Saving TXT file'
txt.close
 

