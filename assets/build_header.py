#!/usr/bin/env python3
"""Generates the profile header artwork in both themes from one source.

Run: python3 assets/build_header.py
Writes: assets/header-dark.svg, assets/header-light.svg

Both files are generated. Edit this script, never the SVGs -- a hand-edited
copy of generated artwork drifts from its source and nothing reports it.
"""
import pathlib

W, H = 1200, 240
FONT = "ui-sans-serif,-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,'Helvetica Neue',Arial,sans-serif"
MONO = "ui-monospace,SFMono-Regular,'SF Mono',Menlo,Consolas,'Liberation Mono',monospace"

THEMES = {
    "dark":  dict(bg="#0B1020", name="#F5F7FA", role="#A8B3C4",
                  meta="#7D8CA3", accent="#E5825F", dot="#FFFFFF", dot_op="0.10"),
    "light": dict(bg="#FFFFFF", name="#0B1020", role="#44506A",
                  meta="#6B7688", accent="#D96A43", dot="#0B1020", dot_op="0.10"),
}

NAME = "Muhammad Hamza"
ROLE = "Senior Software Engineer  ·  Ruby on Rails"
META = "multi-tenant SaaS   ·   tax e-invoicing   ·   offline-first POS"


def dot_grid(t):
    """A dot matrix on the right, fading out toward the type."""
    dots = []
    for row in range(7):
        for col in range(18):
            cx, cy = 690 + col * 29, 40 + row * 27
            fade = min(1.0, (col / 17) ** 0.65 + 0.06)
            dots.append(
                f'<circle cx="{cx}" cy="{cy}" r="2.4" fill="{t["dot"]}" '
                f'opacity="{float(t["dot_op"]) * fade:.3f}"/>'
            )
    return "".join(dots)


def svg(t):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" aria-label="{NAME} — {ROLE}">
  <rect width="{W}" height="{H}" rx="14" fill="{t["bg"]}"/>
  <g>{dot_grid(t)}</g>
  <rect x="0" y="0" width="5" height="{H}" rx="2.5" fill="{t["accent"]}"/>
  <text x="66" y="104" font-family="{FONT}" font-size="60" font-weight="700" letter-spacing="-1.4" fill="{t["name"]}">{NAME}</text>
  <rect x="68" y="130" width="58" height="4" rx="2" fill="{t["accent"]}"/>
  <text x="66" y="176" font-family="{FONT}" font-size="24" font-weight="500" fill="{t["role"]}">{ROLE}</text>
  <text x="66" y="210" font-family="{MONO}" font-size="15.5" letter-spacing="0.2" fill="{t["meta"]}">{META}</text>
</svg>
'''


out = pathlib.Path(__file__).parent
for theme, tokens in THEMES.items():
    (out / f"header-{theme}.svg").write_text(svg(tokens))
    print(f"wrote assets/header-{theme}.svg")
