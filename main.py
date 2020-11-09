import pyttsx3
from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfpage import PDFTextExtractionNotAllowed
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.pdfdevice import PDFDevice
from pdfminer.layout import LAParams
from pdfminer.converter import PDFPageAggregator
import parsepage as p

# Open a PDF file.
fp = open("book.pdf", 'rb')

# Create a PDF parser object associated with the file object.
parser = PDFParser(fp)

# Create a PDF document object that stores the document structure.
# Password for initialization as 2nd parameter
document = PDFDocument(parser)

# Check if the document allows text extraction. If not, abort.
if not document.is_extractable:
    raise PDFTextExtractionNotAllowed

# Create a PDF resource manager object that stores shared resources.
rsrcmgr = PDFResourceManager()

# Create a PDF device object.
device = PDFDevice(rsrcmgr)

# BEGIN LAYOUT ANALYSIS
# Set parameters for analysis.
laparams = LAParams()

# Create a PDF page aggregator object.
device = PDFPageAggregator(rsrcmgr, laparams=laparams)

# Create a PDF interpreter object.
interpreter = PDFPageInterpreter(rsrcmgr, device)

# loop over all pages in the document
fontsize = []
text = []

for page in PDFPage.create_pages(document):
    # read the page into a layout object
    interpreter.process_page(page)
    layout = device.get_result()

    # extract text from this object
    fontsize_page, text_page = p.parse_obj(layout._objs)
    fontsize.extend(fontsize_page)
    text.extend(text_page)

final_text_unfiltered = list(zip(fontsize, text))
talking_text = p.filter_text(final_text_unfiltered)
final_text = [x.replace('\n', '') for x in talking_text]
print(final_text)
speaker = pyttsx3.init()
#speaker.say(final_text)
#speaker.runAndWait()
speaker.save_to_file(text=final_text, filename="finaldemo.mp3")
speaker.runAndWait()
