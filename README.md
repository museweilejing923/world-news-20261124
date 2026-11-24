# World News — Tuesday, 24 November 2026

One image summing up the day's world news, for the make.fun bounty
"Sum up 24 November's world news in one image" ($100).

## The image

A 1024x1024 PNG, drawn programmatically with Python PIL (no AI image
generation, so the text is crisp and correct). Dark navy header with the
date, six white cards for the six biggest stories — each with a coloured
top bar, a flat icon, a category tag, a bold headline, one plain-English
sentence and a key-data pill — and an "ALSO TODAY" bar with three more
stories. Readable at 300px wide.

### The six main stories
1. **Nvidia chief is back — shares soar** (Tech): Jensen Huang returns as
   CEO; Nvidia jumps 31.5%, Nasdaq has its best day since April 2025.
2. **Riyadh tower hit as Iran tensions rise** (Middle East): Houthi attack
   on a Riyadh tower injures 11; Iran says tankers were hit by mines in
   the Strait of Hormuz.
3. **Russian strike hits Zaporizhzhia** (War in Ukraine): overnight attack
   kills 2 and wounds 44, including four children.
4. **Israeli strike kills Hamas security chief** (Gaza): airstrikes kill
   Naeem Abu Nahel and six others.
5. **NATO warns over 'nuclear satellite'** (Security): NATO will defend
   space after reports Russia may launch a nuclear-armed satellite.
6. **Factory fire toll rises to 26** (Disaster): Indonesia candy factory
   fire death toll rises to 26; 8 workers still missing.

### Also today
- S. Korea offers $375,000 rewards to catch AI exam cheats.
- Two US states sue SpaceX over Grok images.
- Blast in Hanoi kills 6.

Sources: BBC Global News Podcast, Just Security Early Edition, Naharnet/AP,
DAWN live updates, The Global Eye, Reuters/AP via Mid-Day and Khaama Press,
CCTV+.

## How to run

```sh
python3 main.py   # writes /output/entry.png
```

`main.py` embeds the PNG as base64 and decodes it. No network, no
randomness, no clock — repeated runs write byte-identical files.

`build_image.py` is the program that drew the image; `entry.png` is the
image itself.

## License

MIT — see LICENSE.
