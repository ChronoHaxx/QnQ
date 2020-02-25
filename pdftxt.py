import io
from pathlib import Path
from pdfminer.high_level import extract_text
from pdfminer.converter import TextConverter
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfpage import PDFPage
def extract_text_from_pdf(pdf_path):
    resource_manager = PDFResourceManager()
    fake_file_handle = io.StringIO()
    converter = TextConverter(resource_manager, fake_file_handle)
    page_interpreter = PDFPageInterpreter(resource_manager, converter)
    
    with open(pdf_path, 'rb') as fh:
        for page in PDFPage.get_pages(fh, 
                                      caching=True,
                                      check_extractable=False):
            page_interpreter.process_page(page)
            
        text = fake_file_handle.getvalue()
    
    # close open handles
    converter.close()
    fake_file_handle.close()
    
    if text:
        return text
    
if __name__ == '__main__':
    #file1.write(extract_text_from_pdf('python.pdf'))
    pathlist = Path('mathematics').glob('**/*.pdf') 
    for path in pathlist:
        # because path is object not string
        path_in_str = str(path) # path to pdf files
        path_to_txt = 'textfiles\\' + path_in_str.rstrip('.pdf') + '.txt' # files to be written
        print(path_in_str)
        if path_in_str.endswith('.pdf'):
            file1 = open(path_to_txt,"w", encoding="utf-8") 
            try :
                file1.write(str(extract_text(path_in_str)))
            except:
                continue