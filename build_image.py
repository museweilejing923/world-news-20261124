#!/usr/bin/env python3
"""Build the 24 November 2026 world-news infographic (1024x1024 PNG).

Programmatic drawing with PIL only: no network, no randomness, no clock,
so the output is byte-identical on every run.
"""
import math
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
OUT = "entry.png"

SANS = "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf"
SANS_BOLD = "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, max_w):
    words = text.split()
    lines, cur = [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if draw.textlength(trial, font=fnt) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def draw_icon(d, cx, cy, kind, color):
    """Simple flat icon in a coloured circle, drawn with PIL primitives."""
    r = 26
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=color)
    white = (255, 255, 255, 255)
    if kind == "chip":  # Nvidia: a chip
        d.rectangle([cx - 12, cy - 12, cx + 12, cy + 12], outline=white, width=3)
        d.rectangle([cx - 5, cy - 5, cx + 5, cy + 5], fill=white)
        for dx in (-8, 0, 8):
            d.line([cx + dx, cy - 18, cx + dx, cy - 12], fill=white, width=3)
            d.line([cx + dx, cy + 12, cx + dx, cy + 18], fill=white, width=3)
            d.line([cx - 18, cy + dx, cx - 12, cy + dx], fill=white, width=3)
            d.line([cx + 12, cy + dx, cx + 18, cy + dx], fill=white, width=3)
    elif kind == "flame":  # Middle East / fire
        d.polygon([(cx, cy - 17), (cx + 11, cy - 2), (cx + 7, cy + 12),
                   (cx - 7, cy + 12), (cx - 11, cy - 2)], fill=white)
        d.polygon([(cx, cy + 2), (cx + 5, cy + 12), (cx - 5, cy + 12)],
                  fill=color)
    elif kind == "burst":  # explosion / strike
        pts = []
        for i in range(16):
            ang = math.pi * i / 8
            rad = 18 if i % 2 == 0 else 8
            pts.append((cx + rad * math.cos(ang), cy + rad * math.sin(ang)))
        d.polygon(pts, fill=white)
        d.ellipse([cx - 4, cy - 4, cx + 4, cy + 4], fill=color)
    elif kind == "target":  # Gaza / strike
        for rr in (16, 10, 4):
            d.ellipse([cx - rr, cy - rr, cx + rr, cy + rr], outline=white, width=3)
        d.ellipse([cx - 3, cy - 3, cx + 3, cy + 3], fill=white)
    elif kind == "satellite":  # NATO / space
        d.rectangle([cx - 6, cy - 6, cx + 6, cy + 6], fill=white)
        d.rectangle([cx - 20, cy - 4, cx - 8, cy + 4], outline=white, width=2)
        d.rectangle([cx + 8, cy - 4, cx + 20, cy + 4], outline=white, width=2)
        d.line([cx + 4, cy - 10, cx + 14, cy - 18], fill=white, width=3)
        d.ellipse([cx + 11, cy - 21, cx + 17, cy - 15], outline=white, width=2)
    elif kind == "factory":  # factory fire
        d.polygon([(cx - 16, cy + 14), (cx - 16, cy - 2), (cx - 8, cy - 8),
                   (cx, cy - 2), (cx + 8, cy - 8), (cx + 16, cy - 2),
                   (cx + 16, cy + 14)], fill=white)
        d.rectangle([cx + 8, cy - 16, cx + 13, cy - 2], fill=white)


CARDS = [
    dict(tag="TECH", color=(22, 163, 74), icon="chip",
         title="Nvidia chief is back — shares soar",
         body="Jensen Huang returns as CEO. Nvidia jumps 31.5%; the Nasdaq "
              "has its best day since April 2025.",
         pill="NVDA +31.5%  •  Nasdaq +6.5%"),
    dict(tag="MIDDLE EAST", color=(220, 60, 40), icon="flame",
         title="Riyadh tower hit as Iran tensions rise",
         body="A Houthi attack hits a tower in Riyadh, injuring 11. Iran says "
              "tankers were hit by mines in Hormuz.",
         pill="11 injured in Riyadh"),
    dict(tag="WAR IN UKRAINE", color=(37, 99, 235), icon="burst",
         title="Russian strike hits Zaporizhzhia",
         body="An overnight attack kills 2 and wounds 44, including four "
              "children, in an apartment block.",
         pill="2 killed  •  44 wounded"),
    dict(tag="GAZA", color=(124, 58, 237), icon="target",
         title="Israeli strike kills Hamas security chief",
         body="Airstrikes kill Naeem Abu Nahel, head of Hamas' internal "
              "security, and six others.",
         pill="7 killed in Gaza"),
    dict(tag="SECURITY", color=(8, 145, 178), icon="satellite",
         title="NATO warns over 'nuclear satellite'",
         body="NATO will defend space after reports Russia may launch a "
              "nuclear-armed satellite.",
         pill="NATO: space is defended"),
    dict(tag="DISASTER", color=(234, 88, 12), icon="factory",
         title="Factory fire toll rises to 26",
         body="The death toll from the Indonesia candy factory fire rises to "
              "26; 8 workers are still missing.",
         pill="26 killed  •  8 missing"),
]

ALSO = [
    ("S. Korea offers $375,000 rewards to catch AI exam cheats",
     (22, 163, 74)),
    ("Two US states sue SpaceX over Grok images", (37, 99, 235)),
    ("Blast in Hanoi kills 6", (220, 60, 40)),
]


def build():
    img = Image.new("RGB", (W, H), (244, 246, 250))
    d = ImageDraw.Draw(img)

    # ---- header ----
    d.rectangle([0, 0, W, 148], fill=(14, 30, 58))
    d.rectangle([0, 148, W, 152], fill=(212, 175, 55))
    d.text((32, 20), "WORLD NEWS", font=font(SANS_BOLD, 46),
           fill=(255, 255, 255))
    d.text((32, 76), "TUESDAY, 24 NOVEMBER 2026", font=font(SANS_BOLD, 30),
           fill=(212, 175, 55))
    d.text((716, 26), "THE DAY IN", font=font(SANS, 22),
           fill=(180, 195, 220))
    d.text((716, 54), "ONE PAGE", font=font(SANS, 22),
           fill=(180, 195, 220))
    d.text((716, 94), "6 big stories + more", font=font(SANS, 18),
           fill=(140, 160, 190))

    # ---- cards 2 x 3 ----
    margin, gap = 24, 12
    cw = (W - 2 * margin - gap) // 2
    ch = 224
    top0 = 166
    f_tag = font(SANS_BOLD, 15)
    f_head = font(SANS_BOLD, 26)
    f_body = font(SANS, 20)
    f_pill = font(SANS_BOLD, 17)

    for i, c in enumerate(CARDS):
        x = margin + (i % 2) * (cw + gap)
        y = top0 + (i // 2) * (ch + gap)
        d.rounded_rectangle([x, y, x + cw, y + ch], radius=14,
                            fill=(255, 255, 255))
        d.rounded_rectangle([x, y, x + cw, y + 8], radius=7, fill=c["color"])
        d.rectangle([x, y + 4, x + cw, y + 8], fill=c["color"])
        draw_icon(d, x + 48, y + 48, c["icon"], c["color"])
        d.text((x + 86, y + 36), c["tag"], font=f_tag, fill=c["color"])
        lines = wrap(d, c["title"], f_head, cw - 32)
        yy = y + 80
        for ln in lines[:2]:
            d.text((x + 16, yy), ln, font=f_head, fill=(20, 30, 50))
            yy += 30
        yy += 4
        for ln in wrap(d, c["body"], f_body, cw - 32)[:2]:
            d.text((x + 16, yy), ln, font=f_body, fill=(70, 80, 100))
            yy += 24
        pill_w = d.textlength(c["pill"], font=f_pill) + 24
        py = y + ch - 32
        d.rounded_rectangle([x + 16, py, x + 16 + pill_w, py + 26], radius=13,
                            fill=(238, 242, 247))
        d.text((x + 28, py + 3), c["pill"], font=f_pill, fill=c["color"])

    # ---- footer: ALSO TODAY ----
    fy = 874
    d.rounded_rectangle([margin, fy, W - margin, 1000], radius=14,
                        fill=(255, 255, 255))
    d.text((margin + 16, fy + 10), "ALSO TODAY", font=font(SANS_BOLD, 18),
           fill=(14, 30, 58))
    f_item = font(SANS_BOLD, 19)
    yy = fy + 38
    for text, color in ALSO:
        d.ellipse([margin + 20, yy + 5, margin + 32, yy + 17], fill=color)
        d.text((margin + 42, yy), text, font=f_item, fill=(40, 50, 70))
        yy += 30

    img.save(OUT, format="PNG")
    return img


if __name__ == "__main__":
    build()
    print("wrote", OUT)
