import pdfplumber

with pdfplumber.open(r"C:\Users\andry\Downloads\Шолохов М. Тихий Дон. .pdf") as pdf:
    with open("book.txt", "w", encoding="utf-8") as txt:
        for page in pdf.pages:
            text = page.extract_text()
            if text:
                txt.write(text + '\n')
