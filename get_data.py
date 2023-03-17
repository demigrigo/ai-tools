import lxml.etree as ET
import glob
import os
import re


NAMESPACES = {
    "tei": "http://www.tei-c.org/ns/1.0",
    "xml": "https://www.w3.org/XML/1998/namespace"
}

files = glob.glob("./data/editions/*.xml")

for f in files:
    fn = os.path.basename(f)
    print("parsing", fn)
    with open(f, "r", encoding="UTF-8") as l:
        xml = l.read()
    try:
        text = ET.fromstring(xml)
    except SyntaxError as err:
        print(err)
    text = " ".join(text.xpath(".//tei:body//text()", namespaces=NAMESPACES))
    text = text.replace("^\s+", "")
    with open("tiny-auden-musulin.txt", "a", encoding="UTF-8") as l:
        l.write(text)

