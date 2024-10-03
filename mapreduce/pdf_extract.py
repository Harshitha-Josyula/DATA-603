# My DOB is 12/31/2000.
#Since 12 divided by 2 is 6 I'm choosing book number 6 for this assignment.

#using the PyPDF2 library to read the pdf.

import PyPDF2

def extract_pages(pdf_path, start_page, end_page, output_file):
    # Open the PDF file
    with open(pdf_path, 'rb') as pdf_file:
        reader = PyPDF2.PdfReader(pdf_file)
        # Extract the specified range of pages
        with open(output_file, 'w', encoding='utf-8') as output:
            for page_num in range(start_page - 1, end_page):
                # Extract the text from each page
                page = reader.pages[page_num]
                text = page.extract_text()
                if text:
                    output.write(text)
                    output.write("\n")

pdf_path = 'Harry_Potter.pdf'

# Extract for file.txt.The book number 6 starts at page 4798 so adding my birthdate 31 and extracting from page 4829
extract_pages(pdf_path, 4829, 4838, 'file.txt') #extracting 10 pages from 4829-4838

# Extract for file2.txt . My Birth Year is 2000 . So I need to extract from page 100 .Since my book starts from page 4798 I'm adding 100 to that and extracting from page number 4898.
extract_pages(pdf_path, 4898, 4997, 'file2.txt')

print("Pages extracted and saved to file.txt and file2.txt")
