# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import gfx
doc = gfx.open("pdf", "Docs/InteiroTeor_AP470.pdf")
text = gfx.PlainText()
for pagenr in range(1,doc.pages+1):
    page = doc.getPage(pagenr)
    text.startpage(page.width, page.height)
    page.render(text)
    text.endpage()
text.save("Docs/InteiroTeor_AP470.txt")
