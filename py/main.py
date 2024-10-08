from pypdf import PdfReader

reader = PdfReader("articles/ADC.pdf")
text = ""
for page in reader.pages:
    text += page.extract_text().rstrip().replace("\n", "").replace(" -", "-").replace(" —", " — ")

print(text)