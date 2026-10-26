---
name: seo-content-workflow
description: Schreibt und überarbeitet deutschsprachige SEO-Texte in sieben Stufen vom Auftrag bis zur Veröffentlichung, mit Prüfung nach jeder Stufe. Für Blogbeiträge, Ratgeber, Magazinartikel, Landingpages, Leistungs- und Kategorietexte. Liefert Text, Title, Meta-Description, Slug, Linkvorschläge, Bildvorschläge mit Alt-Texten und ein Prüfprotokoll. Erfindet keine Erfahrungen, Quellen oder Messwerte. Verwende diesen Skill immer, wenn jemand auf Deutsch einen SEO-Text oder Blogartikel schreiben, aus einer Keyword-Analyse oder Begriffsliste (WDF*IDF, NEURONwriter, Surfer, Sistrix o. ä.) einen Text machen, einen bestehenden Text für ein Fokus-Keyword optimieren, kürzen oder lektorieren will oder Title, Meta-Description, Slug, Überschriften oder FAQ für eine Seite braucht, auch wenn das Wort SEO nicht fällt.
---

# SEO-Content-Workflow

Dieser Skill führt einen deutschsprachigen SEO-Text durch sieben Stufen. Jede Stufe erzeugt ein Ergebnis und endet mit einer Prüfung. Ein Fehler wird in der Stufe behoben, in der er entstanden ist: Fehlt im fertigen Text die Erfahrung des Kunden, hilft kein besseres Formulieren, dann fehlt Material.

Der Grundsatz dahinter: Ein guter SEO-Text beantwortet die Suchanfrage schneller und belegter als die Konkurrenz. Keywords, Struktur und Meta-Angaben sorgen dafür, dass er gefunden wird. Ob er gelesen wird und Vertrauen schafft, entscheiden Substanz und Sprache.

## Drei Regeln, die immer gelten

1. **Nichts erfinden.** Keine Erfahrungen, Fallbeispiele, Zitate, Studien, Zahlen oder Links, die nicht vorliegen oder überprüft sind. Lücken werden sichtbar markiert (`[OFFEN: …]`), nicht überspielt. Der Text erscheint unter dem Namen des Kunden; eine erfundene Erfahrung fällt auf ihn zurück. Einzelheiten in [references/erfahrung.md](references/erfahrung.md).
2. **Nichts schätzen, was gemessen wird.** Suchvolumen, Keyword-Schwierigkeit, SEO-Scores und Pixelbreiten kann der Skill nicht messen. Er arbeitet mit Werten, die der Nutzer aus seinen Werkzeugen mitbringt, und nennt sonst keine Zahlen.
3. **Die Anrede des Auftrags bleibt.** Du, Sie oder unpersönlich wird in Stufe 1 festgelegt und gilt für jeden Satz, auch für Bildvorschläge und CTA.

## Ablauf

| Stufe | Ergebnis | Prüfung vor der nächsten Stufe |
|---|---|---|
| 1 Auftrag | Auftragskarte | Alle Pflichtangaben da oder als Annahme markiert |
| 2 Material | Materialliste | Jede Erfahrungsaussage hat einen Urheber oder steht als offene Frage |
| 3 Gliederung | Gliederung mit Keyword-Plan | Jeder Abschnitt hat genau einen Zweck und eine Suchfrage |
| 4 Entwurf | Fließtext | Stilregeln eingehalten, Wortzahl im Rahmen |
| 5 Optimierung | optimierter Text | Begriffe natürlich eingebaut, Links echt oder als Platzhalter |
| 6 Prüfung | Prüfprotokoll | Keine offenen Mängel außer markierten Rückfragen |
| 7 Veröffentlichung | Paket für das CMS | Title, Meta, Slug, Bilder vollständig |

### Halten oder durchlaufen

Frage in Stufe 1, ob der Nutzer nach jeder Stufe freigeben will. Ohne Angabe gilt: **nach Stufe 1 und nach Stufe 3 anhalten**, danach bis zum Ende durchlaufen. An diesen beiden Stellen kostet eine Korrektur fast nichts; nach dem Entwurf kostet sie den ganzen Text. Sagt der Nutzer „einfach machen“, läuft alles durch, und die Annahmen stehen oben in der Ausgabe.

### Einstieg mitten im Ablauf

Nicht jeder Auftrag ist ein neuer Text. Steige dort ein, wo die Arbeit beginnt, und hole nur die Angaben aus Stufe 1, die diese Arbeit braucht:

- Bestehenden Text optimieren: Stufe 1 (kurz), dann 5 bis 7.
- Nur Lektorat: Stufe 6 mit [references/stil.md](references/stil.md). Inhalt und Keywords bleiben unangetastet.
- Nur Title, Meta, Slug: Stufe 7 mit [references/seo.md](references/seo.md).
- Text kürzen: Stufe 5, Abschnitt „Kürzen“.
- Nur Bildvorschläge: Stufe 7 mit [references/bilder.md](references/bilder.md).

## Stufe 1: Auftrag

Lies zuerst alles, was beiliegt: Keyword-Analyse, Briefing, Begriffslisten, Beispieltexte, Styleguide, URL-Listen. Was dort steht, fragst du nicht noch einmal ab.

**Pflichtangaben**

- Thema und Textart (Blogbeitrag, Ratgeber, Landingpage, Kategorietext …)
- Zielgruppe und ihre Suchintention (informieren, vergleichen, kaufen, lokal finden)
- Fokus-Keyword, dazu Nebenkeywords und Longtail-Varianten aus der Recherche des Nutzers
- Kernaussage: der eine Satz, den die Leserin mitnehmen soll
- Pain Points der Zielgruppe und die Lösungen, die der Kunde bietet
- Wortzahl (Zielwert oder Obergrenze)

**Angaben mit Standardwert** (ohne Antwort gilt der Standard, und er steht in der Auftragskarte)

- Anrede: wie in Beispieltexten oder auf der Website des Kunden, sonst „Sie“
- Ton: sachlich, beratend, leicht verständlich
- Gendern: neutrale Formulierungen (Varianten in [references/stil.md](references/stil.md#gendern))
- CTA-Ziel: Kontakt aufnehmen
- Website und interne Zielseiten: keine, dann werden interne Links als Platzhalter vorgeschlagen
- Halten: nach Stufe 1 und 3

Die Keyword-Recherche selbst gehört nicht zu diesem Skill. Fehlt sie, bitte den Nutzer um Fokus-Keyword und Nebenkeywords aus seinem Werkzeug oder vom Kunden. Schlage keine Suchvolumen vor.

Fasse das Ergebnis als **Auftragskarte** zusammen (Vorlage unter „Ausgabe“). Fehlen Pflichtangaben, frage in einer einzigen Nachricht nach allen gleichzeitig und warte.

## Stufe 2: Material

Sammle, was in den Text muss und nicht aus dem Allgemeinwissen kommt:

- **Erfahrung des Kunden**: Fälle, Zahlen aus dem eigenen Betrieb, typische Fehler, die er bei Kunden sieht, eigene Vorgehensweise. Nur aus dem, was vorliegt (Briefing, Interview, Website, frühere Texte des Kunden).
- **Fakten mit Quelle**: Gesetze, Normen, Fristen, Kosten, Statistiken. Nur mit Quelle, die der Nutzer geliefert hat oder die du tatsächlich aufrufen und lesen konntest. Notiere zu jeder Quelle Herausgeber und Stand. Bevorzuge die neueste verfügbare Fassung; Daten, die älter als drei Jahre sind, nur mit Jahresangabe im Text. Bei Angaben, die sich ändern (Förderung, Preise, Rechtslage), gehören angekündigte Änderungen von derselben Quelle mit in den Text, und das Stand-Datum steht im Prüfprotokoll.
- **Fragen der Zielgruppe**: aus dem Briefing, aus „Weitere Fragen“-Listen, aus der Keyword-Recherche.

Wo Erfahrung fehlt, formuliere konkrete Fragen an den Kunden (höchstens fünf, jede in einem Satz beantwortbar). Ohne Antworten geht es weiter: Die Stellen werden im Text als `[OFFEN: Erfahrung des Kunden: …]` markiert. Einzelheiten und Beispiele in [references/erfahrung.md](references/erfahrung.md).

## Stufe 3: Gliederung

- **H1** mit Fokus-Keyword in Suchform, möglichst weit vorne, als Versprechen an die Suchenden.
- **Einleitung** (40 bis 80 Wörter): Fokus-Keyword im ersten oder zweiten Satz, in Satzform eingebunden (Regeln in seo.md, Abschnitt 1). Danach die direkte Antwort auf die Suchanfrage, dann was der Text darüber hinaus bietet. Keine Hinführung, keine rhetorische Frage als Einstieg.
- **H2/H3**: je Abschnitt eine Suchfrage oder ein Pain Point. Zu jeder Überschrift eine Zeile: Zweck, geplante Keywords, geplantes Material (Erfahrung, Fakt, Beispiel).
- **FAQ**: 3 bis 5 Fragen, die im Hauptteil noch nicht beantwortet sind. Jede Antwort beginnt mit der Antwort (2 bis 4 Sätze).
- **CTA**: eine Handlung, passend zum CTA-Ziel.

Prüfe: Deckt die Gliederung alle Pain Points ab? Beantwortet die Einleitung die Suchanfrage? Gibt es Abschnitte, die zwei Dinge wollen? Dann teilen.

## Stufe 4: Entwurf

Schreibe den Text nach der Gliederung. Lies vorher [references/stil.md](references/stil.md); dort stehen die Sprachregeln mit Begründung. Die wichtigsten:

- Ein Absatz, ein Zweck. Jeder Satz bringt etwas Neues.
- Aktiv, Indikativ, mit handelnder Person. Passiv und Konjunktiv nur, wo sie genauer sind.
- Keine Gedankenstriche als Satzverbinder, stattdessen neuer Satz.
- Keine KI-Floskeln (Liste in stil.md).
- Gendern nach Auftragskarte, im ganzen Text einheitlich.

Halte die Wortzahl mit 10 Prozent Spielraum ein. Zähle nach, statt zu schätzen: Speichere den Text als Markdown-Datei und führe `python3 scripts/zaehlen.py <datei>` aus (Pfad relativ zum Ordner dieses Skills). Das Skript zählt nur Fließtext, ohne Überschriften, Tabellen und Platzhalter. Ohne Code-Ausführung zähle von Hand nach derselben Regel. Nenne die Zahl.

## Stufe 5: Optimierung

Lies [references/seo.md](references/seo.md). Die Optimierung hat vier Teile, in dieser Reihenfolge:

1. **Begriffe einbauen.** Begriffslisten (WDF*IDF, Content-Score-Werkzeuge, Nebenkeywords) kommen vom Nutzer. Baue sie dort ein, wo der Abschnitt ohnehin davon handelt. Ein Begriff, der nirgends natürlich passt, kommt auf die Liste „nicht eingebaut“ mit Grund.
2. **Überschriften schärfen.** Begriffe nach vorne, Inhalt des Abschnitts genau benennen. In diesem Schritt nur Überschriften ändern.
3. **Links.** Interne Links nur auf Seiten, die der Nutzer genannt hat oder die du auf der Website gesehen hast; sonst Platzhalter `[LINK intern: Leistungsseite …]`. Externe Links nur, wenn du die Seite aufgerufen hast und sie die Aussage stützt; sonst `[LINK extern: Quelle für …]`. Nie Links auf Suchergebnisseiten.
4. **Kürzen**, falls die Wortzahl überschritten ist: zuerst Wiederholungen und Füllsätze, dann Nebenaspekte. Erfahrung des Kunden, Kernaussage und Antworten auf Suchfragen bleiben.

Hat der Nutzer ein Content-Score-Werkzeug, bitte ihn, den Text dort zu messen und Score und fehlende Begriffe zurückzugeben. Dann wiederhole Teil 1 und 4 mit diesen Angaben. Behaupte nie, ein Score sei erreicht oder ein Mitbewerber übertroffen, solange keine Messung vorliegt.

## Stufe 6: Prüfung

Gehe die Checkliste in [references/abnahme.md](references/abnahme.md) vollständig durch. Für jeden Mangel gilt: Benenne ihn, ordne ihn der verursachenden Stufe zu und behebe ihn dort. Ein Lektorat ändert Sprache, nicht Inhalt, Keywords oder Ton.

Das Prüfprotokoll nennt nur Abweichungen und offene Punkte, keine erfüllten Punkte.

## Stufe 7: Veröffentlichung

Erstelle das Paket für das CMS (Regeln in [references/seo.md](references/seo.md) und [references/bilder.md](references/bilder.md)):

- SEO-Title (50 bis 60 Zeichen), Meta-Description (140 bis 155 Zeichen), beide mit Fokus-Keyword vorne. Zeichen mit `python3 scripts/zaehlen.py --zeichen "…"` zählen und angeben. Die Pixelbreite prüft der Nutzer in einer Snippet-Vorschau.
- URL-Slug mit Fokus-Keyword, Kleinbuchstaben, ä → ae usw.
- Bildvorschläge: Platz im Text, Art, Briefing oder Bild-Prompt, Dateiname, Alt-Text.
- Hashtags nur auf Wunsch, als Vorschlag ohne Aussage zur Häufigkeit.

## Ausgabe

Gib das Ergebnis in dieser Reihenfolge aus. Lasse Teile weg, die der Auftrag nicht umfasst.

```markdown
## Auftragskarte
| Angabe | Wert |
|---|---|
| Thema / Textart | … |
| Zielgruppe / Suchintention | … |
| Fokus-Keyword | … |
| Nebenkeywords | … |
| Kernaussage | … |
| Anrede / Ton / Gendern | … |
| Wortzahl | Ziel … · erreicht … |
| Annahmen | was ohne Angabe gesetzt wurde |

## Text
# H1 …
(Text in Markdown, mit Platzhaltern [OFFEN: …] und [LINK …])

## SEO-Angaben
| Feld | Inhalt | Zeichen |
|---|---|---|
| SEO-Title | … | 57 |
| Meta-Description | … | 151 |
| Slug | … | |

## Links
| Ankertext | Ziel | Art | Status |

## Bilder
| Nach Abschnitt | Art | Briefing / Prompt | Dateiname | Alt-Text |

## Prüfprotokoll
- Abweichungen, nicht eingebaute Begriffe mit Grund

## Offene Punkte für den Kunden
1. konkrete Frage …
```

## Beispiele

Vorher-nachher-Beispiele für Einleitung, Floskeln, Gendern und markierte Erfahrungslücken stehen in [references/beispiele.md](references/beispiele.md). Lies sie vor dem ersten Entwurf, wenn der Ton unklar ist.
