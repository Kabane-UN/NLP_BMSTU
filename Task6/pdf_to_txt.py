import fitz

with fitz.open("../RL_Theory_Book.pdf") as pdf:
    with open("book.txt", "w", encoding="utf-8") as txt:
        for page in pdf:
            text = page.get_text()
            txt.write(text + " ")
