from bs4 import BeautifulSoup
from bs4.element import Comment
import urllib.request
import spacy

nlp = spacy.load("en_core_web_sm")


def definirTexto(element):
    if element.parent.name in ['style', 'script', 'head', 'title', 'meta', '[document]']:
        return False
    if isinstance(element, Comment):
        return False
    return True


def pegarTexto(body):
    soup = BeautifulSoup(body, 'html.parser')
    texts = soup.findAll(text=True)
    visible_texts = filter(definirTexto, texts)
    return u" ".join(t.strip() for t in visible_texts)


frases = []

html = urllib.request.urlopen('https://en.wikipedia.org/wiki/Vocaloid').read()
page = nlp(pegarTexto(html))
for sentence in page.sents:
    frases.append(sentence.text)

print(frases)
