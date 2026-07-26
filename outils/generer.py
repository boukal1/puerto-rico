#!/usr/bin/env python3
"""
Génère docs/index.html depuis le front matter de MEMOIRE.md.

MEMOIRE.md est la source unique. Ce script n'invente rien : il met en page.

    python3 outils/generer.py
"""

from __future__ import annotations

import html
import re
import sys
from pathlib import Path
from urllib.parse import quote

import yaml

RACINE = Path(__file__).resolve().parent.parent
SOURCE = RACINE / "MEMOIRE.md"
CIBLE = RACINE / "docs" / "index.html"

COMMONS = "https://commons.wikimedia.org/wiki/Special:FilePath/"


# --------------------------------------------------------------------------- #
# Utilitaires
# --------------------------------------------------------------------------- #

def lire_source() -> tuple[dict, str]:
    """Sépare le front matter YAML du corps markdown."""
    texte = SOURCE.read_text(encoding="utf-8")
    if not texte.startswith("---"):
        sys.exit("MEMOIRE.md doit commencer par un front matter YAML.")
    _, brut, corps = texte.split("---", 2)
    donnees = yaml.safe_load(brut)
    if not isinstance(donnees, dict):
        sys.exit("Front matter illisible.")
    return donnees, corps


def enligne(texte: str | None) -> str:
    """Échappe le HTML puis rend **gras** et *italique*. Rien d'autre."""
    if not texte:
        return ""
    sortie = html.escape(str(texte).strip())
    sortie = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", sortie)
    sortie = re.sub(r"(?<!\*)\*(?!\*)(.+?)(?<!\*)\*(?!\*)", r"<em>\1</em>", sortie)
    return sortie


def url_image(fichier: str, largeur: int) -> str:
    return f"{COMMONS}{quote(fichier, safe='(),._-')}?width={largeur}"


def balise_img(image: dict, largeur: int) -> str:
    return (
        f'<img alt="{html.escape(image["alt"])}" '
        f'src="{url_image(image["fichier"], largeur)}" loading="lazy">'
    )


# --------------------------------------------------------------------------- #
# Fragments
# --------------------------------------------------------------------------- #

def bloc_bandeau(images: list[dict]) -> str:
    vignettes = "".join(
        f'<figure class="thumb">{balise_img(i, 640)}</figure>' for i in images
    )
    return f'<div class="band">{vignettes}</div>'


def bloc_traverse(etapes: list[dict], actif: int) -> str:
    jalons = []
    for i, etape in enumerate(etapes):
        if i < actif:
            classe = "tick is-done"
        elif i == actif:
            classe = "tick is-on"
        else:
            classe = "tick"
        jalons.append(f'<span class="{classe}">{html.escape(etape["nom"])}</span>')
    return (
        '<div class="traverse"><div class="traverse__line"></div>'
        f'<div class="traverse__ticks">{"".join(jalons)}</div></div>'
    )


def bloc_etape(etape: dict, index: int, etapes: list[dict], depot: str) -> str:
    vignettes = etape.get("vignettes") or []
    classe_vignettes = "thumbs thumbs--2" if len(vignettes) == 2 else "thumbs"
    grille = "".join(
        f'<figure class="thumb">{balise_img(v, 520)}</figure>' for v in vignettes
    )
    bloc_vignettes = (
        f'<div class="{classe_vignettes}">{grille}</div>'
        f'<p class="cap">{enligne(etape.get("vignettes_legende"))}</p>'
        if vignettes
        else ""
    )

    jours = "".join(
        '<div class="day">'
        f'<p class="day__when">{enligne(j["quand"])}</p>'
        f'<p class="day__what">{enligne(j["texte"])}</p>'
        "</div>"
        for j in etape.get("jours", [])
    )

    alerte = (
        f'<div class="alert">{enligne(etape["alerte"])}</div>'
        if etape.get("alerte")
        else ""
    )
    note = (
        f'<p class="note">{enligne(etape["note"])}</p>' if etape.get("note") else ""
    )
    repli = (
        '<p class="repli"><span>Repli</span>'
        f'{enligne(etape["repli"])}</p>'
        if etape.get("repli")
        else ""
    )

    fiche = ""
    if depot and etape.get("fiche"):
        fiche = (
            f'<p class="fiche"><a href="{depot}/blob/main/{etape["fiche"]}">'
            "Fiche de réservation →</a></p>"
        )

    return f"""
  <article class="stage">
    {bloc_traverse(etapes, index)}
    <div class="stage__grid">
      <div>
        <figure class="plate">{balise_img(etape["image"], 900)}</figure>
        <p class="cap">{enligne(etape.get("image_legende"))}</p>
        {bloc_vignettes}
      </div>
      <div>
        <p class="stage__num">Étape {html.escape(etape["numero"])}</p>
        <h3>{html.escape(etape["nom"])}</h3>
        <p class="stage__dates">{enligne(etape.get("dates"))}</p>
        <p class="stage__coords">{enligne(etape.get("coords"))}</p>
        <div class="stage__body">
          <p>{enligne(etape.get("intro"))}</p>
          {jours}
          {alerte}
          {note}
          {repli}
          {fiche}
        </div>
      </div>
    </div>
  </article>"""


def bloc_sommaire(donnees: dict) -> str:
    lignes = "".join(
        "<tr>"
        f'<td><strong>{html.escape(e["nom"])}</strong> · {html.escape(e["region"])}</td>'
        f'<td class="mono">{html.escape(e["dates_courtes"])}</td>'
        f'<td>{html.escape(e["base"])}</td>'
        f'<td class="mono">{html.escape(e["route"])}</td>'
        "</tr>"
        for e in donnees["etapes"]
    )
    return f"""
<section class="wrap" style="padding-bottom:24px">
  <p class="eyebrow">Le principe</p>
  <div class="section-head"><h2>Une boucle, jamais de retour en arrière</h2></div>
  <p class="lead">{enligne(donnees["principe"])}</p>
  <table>
    <thead><tr><th style="width:24%">Étape</th><th style="width:20%">Dates</th>
    <th>Base</th><th style="width:15%">Route</th></tr></thead>
    <tbody>{lignes}</tbody>
  </table>
</section>"""


def bloc_vols(vols: dict) -> str:
    lignes = "".join(
        "<tr>"
        f'<td class="mono">{html.escape(v["jour"])}</td>'
        f'<td class="mono">{html.escape(v["vol"])}</td>'
        f'<td>{html.escape(v["trajet"])}<br><span class="sub">{html.escape(v["appareil"])}</span></td>'
        f'<td class="mono">{html.escape(v["horaires"])}</td>'
        "</tr>"
        for v in vols["lignes"]
    )
    return f"""
<section class="wrap" style="padding-top:20px">
  <p class="eyebrow">Transport aérien</p>
  <div class="section-head"><h2>Les vols</h2></div>
  <p class="lead">{enligne(vols.get("intro"))}</p>
  <table>
    <thead><tr><th style="width:14%">Jour</th><th style="width:14%">Vol</th>
    <th>Trajet</th><th style="width:22%">Horaires</th></tr></thead>
    <tbody>{lignes}</tbody>
  </table>
  <div class="alert" style="margin-top:22px">{enligne(vols.get("alerte"))}</div>
</section>"""


def bloc_actions(actions: dict) -> str:
    lignes = "".join(
        "<tr>"
        f'<td><strong>{html.escape(a["quoi"])}</strong></td>'
        f'<td><span class="tag{"" if a.get("critique") else " tag--ok"}">'
        f'{html.escape(a["urgence"])}</span></td>'
        f'<td>{enligne(a["pourquoi"])}</td>'
        "</tr>"
        for a in actions["lignes"]
    )
    return f"""
<section class="wrap" style="padding-top:8px">
  <p class="eyebrow">Actions</p>
  <div class="section-head"><h2>À boucler maintenant</h2></div>
  <p class="lead">{enligne(actions.get("intro"))}</p>
  <table>
    <thead><tr><th style="width:30%">Réservation</th><th style="width:14%">Urgence</th>
    <th>Pourquoi</th></tr></thead>
    <tbody>{lignes}</tbody>
  </table>
</section>"""


def bloc_echeances(echeances: list[dict]) -> str:
    lignes = "".join(
        "<tr>"
        f'<td class="mono{" crit" if e.get("critique") else ""}">{html.escape(e["date"])}</td>'
        f'<td>{html.escape(e["quoi"])}</td>'
        f'<td>{enligne(e["consequence"])}</td>'
        "</tr>"
        for e in echeances
    )
    return f"""
<section class="wrap" style="padding-top:8px">
  <p class="eyebrow">Calendrier</p>
  <div class="section-head"><h2>Dernières dates d'annulation gratuite</h2></div>
  <table>
    <thead><tr><th style="width:22%">Échéance</th><th>Établissement</th>
    <th style="width:32%">Conséquence</th></tr></thead>
    <tbody>{lignes}</tbody>
  </table>
</section>"""


def bloc_pratique(pratique: list[dict]) -> str:
    cases = "".join(
        '<div class="check"><span></span><p>'
        f'<b>{html.escape(p["titre"])}</b>{enligne(p["texte"])}</p></div>'
        for p in pratique
    )
    return f"""
<section class="wrap" style="padding-top:8px">
  <p class="eyebrow">Sur place</p>
  <div class="section-head"><h2>Ce qu'il faut savoir</h2></div>
  <div class="checks">{cases}</div>
</section>"""


# --------------------------------------------------------------------------- #
# Assemblage
# --------------------------------------------------------------------------- #

def construire(donnees: dict) -> str:
    v = donnees["voyage"]
    depot = (v.get("depot_url") or "").rstrip("/")
    etapes = donnees["etapes"]

    hero_img = url_image(v["image_hero"]["fichier"], 1900)
    corps_etapes = "".join(
        bloc_etape(e, i, etapes, depot) for i, e in enumerate(etapes)
    )

    return f"""<!DOCTYPE html>
<html lang="fr">
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(v["titre"])} · Dossier de voyage</title>
<meta name="robots" content="noindex">
<!-- FICHIER GÉNÉRÉ — ne pas éditer. Source : MEMOIRE.md · outils/generer.py -->
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Bodoni+Moda:opsz,ital,wght@6..96,0,400;6..96,0,500;6..96,1,400;6..96,0,700&family=Karla:wght@300;400;500;700&family=IBM+Plex+Mono:wght@400;500&display=swap" rel="stylesheet">
<style>{CSS}</style>

<header class="hero">
  <img class="hero__img" alt="{html.escape(v["image_hero"]["alt"])}" src="{hero_img}">
  <div class="hero__scrim"></div>
  <div class="wrap hero__inner">
    <p class="eyebrow">Dossier de voyage · {html.escape(v["voyageurs"])}</p>
    <h1>{html.escape(v["titre"]).replace(" ", "&nbsp;")}<br><em>{html.escape(v["sous_titre"])}</em></h1>
    <p class="hero__sub">{html.escape(v["periode"])} · {v["nuits"]} nuits · {v["etapes_nb"]} étapes</p>
    <dl class="hero__meta">
      <div><dt>Départ</dt><dd>{html.escape(v["depart"])}</dd></div>
      <div><dt>Retour</dt><dd>{html.escape(v["retour"])}</dd></div>
      <div><dt>Voyageurs</dt><dd>{html.escape(v["voyageurs"])}</dd></div>
      <div><dt>Étapes</dt><dd>{v["etapes_nb"]} bases</dd></div>
    </dl>
  </div>
</header>

<main>
{bloc_sommaire(donnees)}
{bloc_bandeau(donnees["bandeau"])}
<section class="wrap" style="padding-top:34px">{corps_etapes}
</section>
{bloc_vols(donnees["vols"])}
{bloc_actions(donnees["actions"])}
{bloc_echeances(donnees["echeances"])}
{bloc_pratique(donnees["pratique"])}
{bloc_bandeau(donnees["bandeau_final"])}
<footer class="wrap">
  <p style="margin:0">{html.escape(v["titre"])} · {html.escape(v["periode"])} · {html.escape(v["voyageurs"])}</p>
  <p style="margin:8px 0 0">Page générée depuis <code>MEMOIRE.md</code>. Photographies : Wikimedia Commons, licences Creative Commons — voir <code>CREDITS.md</code>.</p>
</footer>
</main>
</html>
"""


CSS = """
:root{
  --tinta:#0A2530; --tinta2:#10343F; --tinta3:#17434F;
  --adoquin:#7C99A4; --adoquin-d:#4A6773;
  --mango:#F0A93B; --flamboyan:#D8452F;
  --cal:#F5F0E6; --cal-dim:#CFC9BC;
  --display:"Bodoni Moda",Didot,"Times New Roman",serif;
  --body:"Karla","Helvetica Neue",Arial,sans-serif;
  --mono:"IBM Plex Mono",ui-monospace,"SF Mono",Menlo,monospace;
}
*{box-sizing:border-box}
html{-webkit-text-size-adjust:100%}
body{margin:0;background:var(--tinta);color:var(--cal);font-family:var(--body);font-weight:300;font-size:16px;line-height:1.58}
.wrap{max-width:1120px;margin:0 auto;padding:0 28px}
.eyebrow{font-family:var(--mono);font-size:11px;letter-spacing:.16em;text-transform:uppercase;color:var(--adoquin);margin:0}
h1,h2,h3{font-family:var(--display);font-weight:400;margin:0;line-height:1.06}
strong{font-weight:700;color:#fff}
a{color:var(--mango)}
code{font-family:var(--mono);font-size:.88em}
.sub{color:var(--adoquin);font-size:12.5px}
.crit{color:var(--flamboyan)}

.hero{position:relative;min-height:min(84vh,720px);display:flex;align-items:flex-end;background:linear-gradient(140deg,#14495c,#0A2530 70%);overflow:hidden}
.hero__img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}
.hero__scrim{position:absolute;inset:0;background:linear-gradient(180deg,rgba(10,37,48,.6) 0%,rgba(10,37,48,.25) 36%,rgba(10,37,48,.98) 100%)}
.hero__inner{position:relative;padding:0 0 56px;width:100%}
.hero h1{font-size:clamp(44px,8.8vw,108px);letter-spacing:-.015em;margin:12px 0 0}
.hero h1 em{font-style:italic;color:var(--mango)}
.hero__sub{font-family:var(--mono);font-size:clamp(11px,1.6vw,13.5px);letter-spacing:.22em;text-transform:uppercase;color:var(--cal-dim);margin:22px 0 0}
.hero__meta{display:flex;flex-wrap:wrap;gap:0 40px;margin-top:28px;padding-top:20px;border-top:1px solid rgba(124,153,164,.4)}
.hero__meta div{padding:5px 0}
.hero__meta dt{font-family:var(--mono);font-size:10px;letter-spacing:.16em;text-transform:uppercase;color:var(--adoquin)}
.hero__meta dd{margin:4px 0 0;font-size:18px;font-family:var(--display)}

.traverse{position:relative;margin:0 0 26px;padding-top:18px}
.traverse__line{position:absolute;left:0;right:0;top:24px;height:1px;background:var(--adoquin-d);opacity:.5}
.traverse__ticks{position:relative;display:flex;justify-content:space-between}
.tick{position:relative;flex:0 0 auto;text-align:center;font-family:var(--mono);font-size:9.5px;letter-spacing:.1em;color:var(--adoquin-d);text-transform:uppercase}
.tick::before{content:"";display:block;width:7px;height:7px;margin:0 auto 8px;border-radius:50%;background:var(--tinta);border:1px solid var(--adoquin-d)}
.tick.is-on{color:var(--mango)}
.tick.is-on::before{background:var(--mango);border-color:var(--mango);width:9px;height:9px;margin-bottom:7px}
.tick.is-done::before{background:var(--adoquin-d)}

section{padding:56px 0}
.section-head h2{font-size:clamp(25px,3.8vw,38px);margin-top:6px}
.lead{font-size:17px;color:var(--cal-dim);max-width:64ch;margin:14px 0 0}

.stage{border-top:1px solid rgba(124,153,164,.28);padding:48px 0 6px}
.stage:first-of-type{border-top:0}
.stage__grid{display:grid;grid-template-columns:0.92fr 1fr;gap:40px;align-items:start}
figure{margin:0}
.plate{position:relative;aspect-ratio:3/2;background:linear-gradient(150deg,var(--tinta3),var(--tinta));overflow:hidden}
.plate img{width:100%;height:100%;object-fit:cover;display:block;filter:saturate(.93) contrast(1.03)}
.cap{font-family:var(--mono);font-size:9.5px;letter-spacing:.09em;text-transform:uppercase;color:var(--adoquin);margin:7px 0 0;line-height:1.4}
.thumbs{display:grid;grid-template-columns:repeat(3,1fr);gap:10px;margin-top:14px}
.thumbs--2{grid-template-columns:repeat(2,1fr)}
.thumb{position:relative;aspect-ratio:1;background:linear-gradient(150deg,var(--tinta3),var(--tinta));overflow:hidden}
.thumb img{width:100%;height:100%;object-fit:cover;display:block;filter:saturate(.93) contrast(1.03)}

.stage__num{font-family:var(--display);font-size:12.5px;letter-spacing:.3em;color:var(--mango);text-transform:uppercase}
.stage h3{font-size:clamp(28px,4.3vw,42px);margin:8px 0 0;letter-spacing:-.01em}
.stage__dates{font-family:var(--mono);font-size:12px;letter-spacing:.09em;color:var(--cal);margin:13px 0 0}
.stage__coords{font-family:var(--mono);font-size:10px;letter-spacing:.08em;color:var(--adoquin);margin:4px 0 0}
.stage__body{margin-top:20px}
.stage__body>p{margin:0 0 14px}
.repli{margin:16px 0 0;font-size:13.5px;color:var(--cal-dim)}
.repli span{display:inline-block;font-family:var(--mono);font-size:9px;letter-spacing:.14em;text-transform:uppercase;color:var(--adoquin);border:1px solid var(--adoquin-d);padding:2px 6px;margin-right:9px;vertical-align:1px}
.fiche{margin:18px 0 0;font-family:var(--mono);font-size:10.5px;letter-spacing:.08em;text-transform:uppercase}

.day{display:grid;grid-template-columns:80px 1fr;gap:14px;padding:12px 0;border-top:1px dotted rgba(124,153,164,.35)}
.day:first-child{border-top:0}
.day__when{font-family:var(--mono);font-size:10.5px;letter-spacing:.07em;color:var(--mango);text-transform:uppercase;padding-top:3px}
.day__what{margin:0;font-size:15px}
.day__what strong{color:#fff;font-weight:700}

.note{border-left:2px solid var(--adoquin-d);padding:1px 0 1px 16px;margin:18px 0 0;font-size:14px;color:var(--cal-dim);font-style:italic}
.alert{border-left:2px solid var(--flamboyan);padding:1px 0 1px 16px;margin:18px 0 0;font-size:14px;color:#F3CFC8}
.alert strong{color:#fff}

.band{display:grid;grid-template-columns:repeat(4,1fr);gap:10px;margin:0 auto;max-width:1120px;padding:0 28px}
.band .thumb{aspect-ratio:4/3}

table{width:100%;border-collapse:collapse;margin-top:22px;font-size:14px}
th{text-align:left;font-family:var(--mono);font-weight:500;font-size:9.5px;letter-spacing:.15em;text-transform:uppercase;color:var(--adoquin);padding:0 14px 9px 0;border-bottom:1px solid var(--adoquin-d)}
td{padding:11px 14px 11px 0;border-bottom:1px solid rgba(124,153,164,.2);vertical-align:top}
td.mono,.mono{font-family:var(--mono);font-size:12px;letter-spacing:.02em}
tr td:last-child,tr th:last-child{padding-right:0}
.tag{display:inline-block;font-family:var(--mono);font-size:9px;letter-spacing:.12em;text-transform:uppercase;padding:3px 7px;border:1px solid var(--flamboyan);color:var(--flamboyan);white-space:nowrap}
.tag--ok{border-color:var(--adoquin-d);color:var(--adoquin)}

.checks{display:grid;grid-template-columns:repeat(3,1fr);gap:0 36px;margin-top:22px}
.check{display:grid;grid-template-columns:16px 1fr;gap:11px;padding:11px 0;border-top:1px solid rgba(124,153,164,.2)}
.check span{width:11px;height:11px;border:1px solid var(--adoquin);margin-top:5px}
.check p{margin:0;font-size:13.5px}
.check p b{display:block;color:#fff;font-weight:500}

footer{padding:44px 0 64px;border-top:1px solid rgba(124,153,164,.28);color:var(--adoquin);font-size:12px}

@media(max-width:900px){
  .stage__grid{grid-template-columns:1fr;gap:24px}
  .checks{grid-template-columns:1fr}
  .band{grid-template-columns:repeat(2,1fr)}
  .tick{font-size:0}.tick.is-on{font-size:9.5px}
  .day{grid-template-columns:1fr;gap:3px}
}

@media print{
  @page{margin:11mm}
  *{-webkit-print-color-adjust:exact;print-color-adjust:exact}
  body{background:#fff;color:#16303a;font-size:9pt;line-height:1.4}
  .wrap{max-width:none;padding:0}
  .hero{min-height:0;display:block;background:none}
  .hero__img{position:relative;height:52mm;object-fit:cover}
  .hero__scrim{display:none}
  .hero__inner{padding:8pt 0 0}
  .hero h1{font-size:34pt;color:#0A2530}
  .hero__sub{font-size:8pt;color:#4A6773;margin-top:8pt}
  .hero__meta{margin-top:10pt;padding-top:8pt;border-color:#c3ccd0;gap:0 22pt}
  .hero__meta dd{font-size:11pt;color:#0A2530}
  section{padding:12pt 0}
  .section-head h2{font-size:16pt;color:#0A2530}
  .lead{font-size:9.5pt;color:#33484f;margin-top:6pt}
  .stage{padding:12pt 0 4pt;break-inside:avoid;page-break-inside:avoid;border-color:#c3ccd0}
  .stage__grid{grid-template-columns:0.8fr 1fr;gap:14pt}
  .plate{aspect-ratio:4/3}
  .thumbs{gap:5pt;margin-top:6pt}
  .cap{font-size:6pt;color:#5c7681;margin-top:4pt}
  .stage h3{font-size:19pt;color:#0A2530}
  .stage__dates{font-size:8pt;color:#16303a;margin-top:7pt}
  .stage__coords{font-size:7pt;color:#5c7681}
  .stage__body{margin-top:10pt}
  .repli{font-size:8pt;color:#3d5158;margin-top:8pt}
  .repli span{font-size:6pt;color:#5c7681;border-color:#8fa3ab}
  .fiche{display:none}
  .day{padding:6pt 0;grid-template-columns:62pt 1fr;gap:9pt}
  .day__what{font-size:9pt}
  .day__what strong{color:#0A2530}
  .note,.alert{font-size:8.5pt;margin-top:10pt;padding-left:11pt}
  .note{color:#3d5158;border-color:#8fa3ab}
  .alert{color:#8e2718}
  .alert strong{color:#5e180d}
  .traverse{margin-bottom:14pt;padding-top:12pt}
  .traverse__line{background:#c3ccd0}
  .tick{font-size:6.5pt;color:#9aa9ae}
  .tick::before{background:#fff;border-color:#9aa9ae;width:5pt;height:5pt;margin-bottom:5pt}
  .tick.is-on{color:#B07500}
  .tick.is-on::before{background:#E09A2B;border-color:#E09A2B}
  .tick.is-done::before{background:#9aa9ae}
  table{font-size:8.5pt;margin-top:9pt}
  th{font-size:6.5pt;color:#5c7681;border-color:#8fa3ab;padding-bottom:5pt}
  td{padding:6pt 10pt 6pt 0;border-color:#dde3e5}
  td.mono,.mono{font-size:8pt}
  .sub{color:#5c7681;font-size:7.5pt}
  .band{grid-template-columns:repeat(4,1fr);gap:5pt;padding:0;break-inside:avoid}
  .checks{grid-template-columns:repeat(3,1fr);gap:0 20pt;margin-top:9pt}
  .check{padding:6pt 0;border-color:#dde3e5}
  .check p{font-size:8pt;color:#33484f}
  .check p b{color:#0A2530}
  .check span{border-color:#8fa3ab}
  footer{padding:14pt 0 0;border-color:#c3ccd0;color:#5c7681;font-size:7.5pt}
  .tag{font-size:6.5pt}
}
@media(prefers-reduced-motion:reduce){*{animation:none!important;transition:none!important}}
"""


def main() -> None:
    donnees, _ = lire_source()
    CIBLE.parent.mkdir(parents=True, exist_ok=True)
    CIBLE.write_text(construire(donnees), encoding="utf-8")
    images = (
        len(donnees["etapes"])
        + sum(len(e.get("vignettes", [])) for e in donnees["etapes"])
        + len(donnees["bandeau"])
        + len(donnees["bandeau_final"])
        + 1
    )
    print(
        f"{CIBLE.relative_to(RACINE)} généré — "
        f"{len(donnees['etapes'])} étapes, {images} images, "
        f"{CIBLE.stat().st_size // 1024} Kio"
    )


if __name__ == "__main__":
    main()
