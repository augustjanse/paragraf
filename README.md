# paragraf
Script to add paragraph numbering to Markdown documents according to headings.

`./paragraf.py doc.md`

Should ideally follow the CommonMark specification for headings, but doesn't. Should still work as intended for most documents. The following are two known deviations from the standard:
- Setext heading underlines must be at least 2 characters to be recognized as a headings.
- Headings are assumed by the script to be only one line.

Not thoroughly tested, but generated the same numbering as had been done manually when run on [the statutes](https://github.com/datasektionen/styrdokument/blob/master/stadgar/body.md).
