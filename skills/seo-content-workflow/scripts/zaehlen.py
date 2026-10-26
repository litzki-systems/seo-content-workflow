#!/usr/bin/env python3
"""Zählt Wörter im Fließtext und Zeichen in SEO-Angaben.

Aufruf:
  python3 scripts/zaehlen.py text.md            Wörter im Fließtext einer Markdown-Datei
  python3 scripts/zaehlen.py --zeichen "Text"   Zeichen (mit Leerzeichen) eines Title oder einer Meta-Description

Fließtext heißt: ohne Überschriften, Tabellen, Code-Blöcke, HTML-Kommentare und
ohne Platzhalter in eckigen Klammern ([OFFEN: …], [LINK …]). Linktexte zählen,
Linkziele nicht. Nur Python-Standardbibliothek.
"""
import re
import sys


def fliesstext(md: str) -> str:
    md = re.sub(r"```.*?```", " ", md, flags=re.S)
    md = re.sub(r"<!--.*?-->", " ", md, flags=re.S)
    zeilen = []
    for zeile in md.splitlines():
        z = zeile.strip()
        if not z or z.startswith("#") or z.startswith("|") or re.fullmatch(r"-{3,}", z):
            continue
        zeilen.append(z)
    text = "\n".join(zeilen)
    text = re.sub(r"\[(OFFEN|LINK)[^\]]*\]", " ", text)   # Platzhalter
    text = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", text)  # Linktext behalten
    text = re.sub(r"^\s*(?:[-*+]|\d+\.)\s+", "", text, flags=re.M)  # Listenzeichen
    text = re.sub(r"^>\s?", "", text, flags=re.M)
    text = re.sub(r"[*_`]", "", text)
    return text


def woerter(text: str) -> int:
    return len([w for w in text.split() if re.search(r"\w", w)])


def main(argv):
    if len(argv) == 3 and argv[1] == "--zeichen":
        print(len(argv[2]))
        return 0
    if len(argv) == 2:
        with open(argv[1], encoding="utf-8") as f:
            print(woerter(fliesstext(f.read())))
        return 0
    print(__doc__)
    return 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))
