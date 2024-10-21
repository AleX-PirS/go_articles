from pypdf import PdfReader
import regex as re
from WORDS import WORDS

def GetText(path, last_idx):
    data = list()
    for idx, p in enumerate(PdfReader(path).pages):
        if idx <last_idx:
            data.append(p.extract_text().rstrip().replace("\n", " ").replace(" -", "-").replace(" —", " — "))
    return data

def FindWords(path, last_idx):    
    result = dict()
    res_w = []
    text = GetText(path, last_idx)
    for w in WORDS:
        for page_num, p in enumerate(text):
            page_num += 1
            t = re.findall(rf"[^\.]* {w}[\,\:sied]* [^\.]*\.", p, re.IGNORECASE)
            if len(t)>0:
                if w in result:
                    if page_num in result[w]:
                        result[w][page_num].append(t)
                    else:
                        result[w][page_num] = t
                else:
                    result[w] = {}
                    result[w][page_num] = t
                    res_w.append(w)
    for k, v in result.items():
        print(f"\n\n\n––––––––––––––––––––––––'{k}'––––––––––––––––––––––––")
        for num, snt in v.items():
            print(f"\tpage:{num}")
            for s in snt:
                print(f"\t\t-{s}")
    
    wordss = []
    for w in WORDS:
        if w not in list(result.keys()) and w not in wordss:
            wordss.append(w)

    print(f"\n\n\n----This article has:{len(res_w)}-----------------------")
    print(res_w)
    print(f"\n\n----Lasts:{len(wordss)}----------------------------------")
    print(wordss)

if __name__ == "__main__":
    FindWords("articles/10.pdf", 10)