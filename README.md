# SEO-Content-Workflow

Ein Claude-Skill für deutschsprachige SEO-Texte. Er führt jeden Text durch sieben Stufen vom Auftrag bis zur Veröffentlichung, mit einer Prüfung nach jeder Stufe, und erfindet dabei keine Erfahrungen, Quellen oder Messwerte.

Von Thorsten Litzki · [Litzki Systems](https://litzki-systems.com). Entstanden aus der Prompt-Sequenz, mit der ich über Jahre SEO-Texte geschrieben und Texterinnen und Texter geschult habe, neu geordnet und für Claude als Skill gebaut.

*English summary below.*

## Was der Skill macht

| Stufe | Ergebnis |
|---|---|
| 1 Auftrag | Auftragskarte: Thema, Zielgruppe, Suchintention, Fokus-Keyword, Kernaussage, Anrede, Gendern, Wortzahl |
| 2 Material | Erfahrung des Kunden, Fakten mit Quelle und Stand, offene Fragen an den Kunden |
| 3 Gliederung | H1, Einleitung mit Antwort zuerst, H2/H3 je Suchfrage, FAQ, CTA |
| 4 Entwurf | Fließtext nach festen Stilregeln |
| 5 Optimierung | Begriffslisten einbauen, Überschriften schärfen, Links, Kürzen |
| 6 Prüfung | Prüfprotokoll nach Checkliste, Mängel werden in der verursachenden Stufe behoben |
| 7 Veröffentlichung | SEO-Title, Meta-Description, Slug, Bildvorschläge mit Dateinamen und Alt-Texten |

Ohne andere Angabe hält der Skill nach Stufe 1 und nach Stufe 3 an und wartet auf Freigabe. Mit „einfach durchlaufen“ geht er ohne Halt bis zum Ende. Er kann auch mitten im Ablauf einsteigen: nur Lektorat, nur Title und Meta, einen Text kürzen oder einen bestehenden Text optimieren.

### Was er nicht tut

- **Keine erfundene Erfahrung.** Fälle, Kundenstimmen, eigene Zahlen oder Leistungsversprechen des Kunden kommen nur aus dem Briefing. Fehlt etwas, steht im Text `[OFFEN: …]`, und am Ende steht eine Frage an den Kunden.
- **Keine geschätzten Messwerte.** Suchvolumen, Keyword-Schwierigkeit, Content-Scores und Pixelbreiten misst der Skill nicht. Keyword-Recherche und Begriffslisten bringst du aus deinem Werkzeug mit (NEURONwriter, Surfer, Sistrix, WDF*IDF-Tools oder vom Kunden).
- **Keine ungeprüften Links.** Externe Links nur zu Seiten, die tatsächlich aufgerufen wurden, sonst als Platzhalter.

### Stilregeln in Kürze

Ein Absatz, ein Zweck. Antwort zuerst. Aktiv und Indikativ. Keine Gedankenstriche als Satzverbinder. Keine KI-Floskeln („nicht nur …, sondern auch“, „spannend“, „In der heutigen Welt“). Anführungszeichen nur für Rede und Zitate. Anrede (Du, Sie, unpersönlich) durchgehend wie im Auftrag.

**Gendern:** Standard sind neutrale Formulierungen („das Team“, „Fachleute“, „wer einen Antrag stellt“). Auf Wunsch nach dem Styleguide des Kunden (Doppelpunkt, Sternchen, Paarform) oder im generischen Maskulinum. Das Fokus-Keyword behält in Title, H1 und Slug die Form, in der gesucht wird.

Alle Regeln mit Begründung: [`skills/seo-content-workflow/references/stil.md`](skills/seo-content-workflow/references/stil.md).

### Was der Skill ausführt und abruft

- **Lokal:** `scripts/zaehlen.py` zählt Wörter und Zeichen. Es liest nur die Textdatei, die Claude ihm übergibt, nutzt nur die Python-Standardbibliothek und sendet nichts.
- **Im Netz:** Der Skill selbst ruft nichts ab. Er weist Claude an, externe Quellen nur dann zu verlinken, wenn Claude sie mit den eigenen Werkzeugen der Sitzung (z. B. Websuche) tatsächlich aufgerufen hat. Ohne diese Werkzeuge bleiben Links Platzhalter.
- **Daten:** Der Skill speichert nichts und sendet nichts an Dritte. Briefings und Texte bleiben in der Unterhaltung.

## Datenschutz

Der Skill erhebt, speichert und übermittelt keine personenbezogenen Daten. Er besteht aus Anleitungen und einem lokalen Zählskript. Was mit Unterhaltungen in Claude geschieht, regelt die Datenschutzerklärung von Anthropic. Fragen zum Skill: [Issues](https://github.com/litzki-systems/seo-content-workflow/issues).

## Installation

### claude.ai (Web, Desktop, App)

1. Unter [Releases](https://github.com/litzki-systems/seo-content-workflow/releases) die Datei `seo-content-workflow.zip` herunterladen.
2. In Claude unter den Einstellungen die Skills öffnen und die ZIP-Datei hochladen. Code-Ausführung muss eingeschaltet sein. Anleitung von Anthropic: [Use Skills in Claude](https://support.claude.com/en/articles/12512180-use-skills-in-claude).

### Claude Code

```
/plugin marketplace add litzki-systems/seo-content-workflow
/plugin install litzki-seo-content-workflow@litzki-systems
```

Oder von Hand: den Ordner `skills/seo-content-workflow` nach `~/.claude/skills/` kopieren.

### Claude API

Den Ordner `skills/seo-content-workflow` über die Skills-Schnittstelle hochladen, siehe [Agent Skills](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview).

## Beispiele für Aufträge

- „Hier die Keyword-Analyse und das Briefing für einen Ratgeber. Schreib den Beitrag mit Meta-Angaben und Bildvorschlägen.“
- „Lektorier diesen Text. Inhalt und Keywords nicht anfassen, der Kunde gendert mit Doppelpunkt.“
- „Ich brauch nur Title, Meta-Description und Slug für die Landingpage, Fokus-Keyword: …“
- „Kürz diesen Text auf 700 Wörter, die Begriffe aus der Liste sollen drinbleiben.“

## Gemessen statt geschätzt

Der Skill wurde an vier Testaufträgen geprüft, jeweils mit und ohne Skill: Ratgeber aus einem Briefing, Lektorat eines Kundentexts, nur Title/Meta/Slug mit unlösbarer Längenvorgabe, unvollständiger Auftrag. Bewertet wurden 34 überprüfbare Punkte, Zeichen und Wörter per Skript nachgezählt, Zahlen in zitierten Quellen nachgeschlagen.

| | erfüllt |
|---|---|
| mit Skill | 34 von 34 |
| ohne Skill | 23 von 34 |

Typische Fehler ohne Skill: Gedankenstriche und Floskeln im Lektorat stehen gelassen, Kosten ohne Quelle, generisches Maskulinum, ein Title mit 70 Zeichen ohne Hinweis, falsch angegebene Zeichenzahlen, bei unvollständigem Auftrag sofort 1.000 Wörter ins Blaue. Vier Testfälle sind eine kleine Stichprobe; die Fälle liegen in [`skills/seo-content-workflow/evals/`](skills/seo-content-workflow/evals/) und laufen mit `claude plugin eval skills/seo-content-workflow`.

## Aufbau

```
.claude-plugin/          Plugin-Beschreibung und Plugin-Quelle für Claude Code
skills/seo-content-workflow/
  SKILL.md               Ablauf in sieben Stufen, Ausgabeformat
  references/            stil.md, seo.md, erfahrung.md, bilder.md, abnahme.md, beispiele.md
  scripts/zaehlen.py     zählt Wörter im Fließtext und Zeichen in Title und Meta
  evals/                 Testfälle
```

## Lizenz

MIT, siehe [LICENSE](LICENSE). Rückmeldungen und Verbesserungen gern als Issue.

---

## English summary

**SEO-Content-Workflow** is a Claude skill for writing SEO content in **German**. It takes a text through seven stages (brief, material, outline, draft, optimisation, review, publication), each ending with a quality check, and delivers the article, SEO title, meta description, slug, link suggestions, image briefs with alt texts and a review log.

It never invents first-hand experience, sources or metrics: missing client experience is marked `[OFFEN: …]` and turned into questions for the client; keyword research and term lists come from the user's own tools; external links are only used if actually fetched. Gender-inclusive language defaults to neutral wording, with the client's style guide or the generic masculine as options.

Install: download `seo-content-workflow.zip` from Releases and upload it in Claude's settings, or in Claude Code run `/plugin marketplace add litzki-systems/seo-content-workflow` and `/plugin install litzki-seo-content-workflow@litzki-systems`. The skill's instructions are in German and it writes German only. Licence: MIT.
