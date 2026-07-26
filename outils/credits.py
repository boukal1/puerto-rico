#!/usr/bin/env python3
"""
Complète le tableau de CREDITS.md depuis l'API de Wikimedia Commons.

La liste des images est lue dans le front matter de MEMOIRE.md — même source
unique que le dossier publié. Seul le tableau entre les deux marqueurs est
réécrit : la prose du fichier n'est jamais touchée.

    python3 outils/credits.py            # réécrit le tableau
    python3 outils/credits.py --verifier  # ne réécrit rien, sort 1 si incomplet

Sans accès réseau à commons.wikimedia.org, le script s'arrête sans rien
modifier : une attribution inventée serait pire qu'un « à compléter ».
"""

from __future__ import annotations

import argparse
import html
import json
import re
import sys
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

import yaml

RACINE = Path(__file__).resolve().parent.parent
SOURCE = RACINE / "MEMOIRE.md"
CIBLE = RACINE / "CREDITS.md"

API = "https://commons.wikimedia.org/w/api.php"
PAGE = "https://commons.wikimedia.org/wiki/File:"
LOT = 25  # limite de titres par requête pour un client non authentifié
UA = "porto-rico-2027/1.0 (dossier de voyage privé ; script outils/credits.py)"

DEBUT = "<!-- TABLEAU AUTO — début. Généré par outils/credits.py, ne pas éditer à la main. -->"
FIN = "<!-- TABLEAU AUTO — fin. -->"

A_COMPLETER = "à compléter"


# --------------------------------------------------------------------------- #
# Liste des images : MEMOIRE.md est la source unique
# --------------------------------------------------------------------------- #

def fichiers_utilises() -> list[str]:
    """Tous les fichiers Commons référencés par le front matter, sans doublon."""
    texte = SOURCE.read_text(encoding="utf-8")
    if not texte.startswith("---"):
        sys.exit("MEMOIRE.md doit commencer par un front matter YAML.")
    _, brut, _ = texte.split("---", 2)
    donnees = yaml.safe_load(brut)

    trouves: list[str] = []

    def ajouter(image: dict | None) -> None:
        if image and image.get("fichier") and image["fichier"] not in trouves:
            trouves.append(image["fichier"])

    ajouter(donnees["voyage"].get("image_hero"))
    for image in donnees.get("bandeau") or []:
        ajouter(image)
    for etape in donnees.get("etapes") or []:
        ajouter(etape.get("image"))
        for vignette in etape.get("vignettes") or []:
            ajouter(vignette)
    for image in donnees.get("bandeau_final") or []:
        ajouter(image)

    return trouves


# --------------------------------------------------------------------------- #
# Interrogation de Commons
# --------------------------------------------------------------------------- #

def texte_nu(valeur: str | None) -> str:
    """Les champs extmetadata arrivent en HTML : on en extrait le texte."""
    if not valeur:
        return ""
    sans_balises = re.sub(r"<[^>]+>", " ", valeur)
    return re.sub(r"\s+", " ", html.unescape(sans_balises)).strip()


def interroger(titres: list[str]) -> dict:
    params = {
        "action": "query",
        "format": "json",
        "formatversion": "2",
        "prop": "imageinfo",
        "iiprop": "extmetadata",
        "iiextmetadatafilter": "Artist|LicenseShortName|LicenseUrl|UsageTerms|AttributionRequired",
        "redirects": "1",
        "titles": "|".join("File:" + t for t in titres),
    }
    requete = urllib.request.Request(
        API + "?" + urllib.parse.urlencode(params), headers={"User-Agent": UA}
    )
    with urllib.request.urlopen(requete, timeout=60) as reponse:
        return json.loads(reponse.read().decode("utf-8"))


def metadonnees(fichiers: list[str]) -> dict[str, dict]:
    """fichier → {auteur, licence, licence_url, requise}. Champs vides si inconnus."""
    resultat: dict[str, dict] = {}

    for depart in range(0, len(fichiers), LOT):
        lot = fichiers[depart : depart + LOT]
        try:
            reponse = interroger(lot)
        except (urllib.error.URLError, urllib.error.HTTPError, TimeoutError) as erreur:
            sys.exit(
                f"Commons injoignable ({erreur}). Rien n'a été modifié.\n"
                "Relancer depuis un réseau qui autorise commons.wikimedia.org."
            )

        query = reponse.get("query", {})
        # Un titre demandé peut être normalisé ou suivre une redirection :
        # on remonte la chaîne pour retrouver le nom de fichier d'origine.
        vers_origine: dict[str, str] = {}
        for etape in ("normalized", "redirects"):
            for saut in query.get(etape, []) or []:
                origine = saut["from"].removeprefix("File:")
                vers_origine[saut["to"]] = vers_origine.get(saut["from"], origine)

        for page in query.get("pages", []) or []:
            titre = page.get("title", "")
            fichier = vers_origine.get(titre, titre.removeprefix("File:"))
            if page.get("missing"):
                resultat[fichier] = {}
                continue
            infos = (page.get("imageinfo") or [{}])[0]
            extra = infos.get("extmetadata") or {}
            valeur = lambda cle: texte_nu((extra.get(cle) or {}).get("value"))
            resultat[fichier] = {
                "auteur": valeur("Artist"),
                "licence": valeur("LicenseShortName") or valeur("UsageTerms"),
                "licence_url": (extra.get("LicenseUrl") or {}).get("value", ""),
                "requise": valeur("AttributionRequired").lower() == "true",
            }

    return resultat


# --------------------------------------------------------------------------- #
# Rendu du tableau
# --------------------------------------------------------------------------- #

def echapper(texte: str) -> str:
    """Un | dans un nom d'auteur casserait la table markdown."""
    return texte.replace("|", "\\|")


def ligne(fichier: str, infos: dict) -> str:
    auteur = echapper(infos.get("auteur") or "") or A_COMPLETER
    licence = echapper(infos.get("licence") or "") or A_COMPLETER
    url = infos.get("licence_url") or ""
    if url and licence != A_COMPLETER:
        licence = f"[{licence}]({url})"
    lien = f"[`{fichier}`]({PAGE}{urllib.parse.quote(fichier)})"
    return f"| {lien} | {auteur} | {licence} |"


def construire_tableau(fichiers: list[str], infos: dict[str, dict]) -> str:
    lignes = [
        "| Fichier Commons | Auteur | Licence |",
        "|---|---|---|",
        *(ligne(f, infos.get(f, {})) for f in fichiers),
    ]
    return "\n".join(lignes)


def remplacer_tableau(texte: str, tableau: str) -> str:
    bloc = f"{DEBUT}\n\n{tableau}\n\n{FIN}"
    if DEBUT in texte and FIN in texte:
        avant = texte.split(DEBUT)[0]
        apres = texte.split(FIN, 1)[1]
        return avant + bloc + apres
    sys.exit(
        f"Marqueurs absents de {CIBLE.name}. Encadrer le tableau par :\n"
        f"  {DEBUT}\n  ...\n  {FIN}"
    )


# --------------------------------------------------------------------------- #

def main() -> None:
    analyseur = argparse.ArgumentParser(description=__doc__)
    analyseur.add_argument(
        "--verifier",
        action="store_true",
        help="ne rien réécrire ; sortir 1 si une attribution manque",
    )
    options = analyseur.parse_args()

    fichiers = fichiers_utilises()
    infos = metadonnees(fichiers)

    manquants = [
        f for f in fichiers if not (infos.get(f, {}).get("auteur") and infos.get(f, {}).get("licence"))
    ]

    if not options.verifier:
        texte = CIBLE.read_text(encoding="utf-8")
        CIBLE.write_text(
            remplacer_tableau(texte, construire_tableau(fichiers, infos)),
            encoding="utf-8",
        )
        print(f"{CIBLE.name} — {len(fichiers)} fichiers, {len(fichiers) - len(manquants)} attribués.")

    if manquants:
        print(
            f"\n{len(manquants)} attribution(s) à reprendre à la main "
            "(page Commons introuvable ou champ Artist vide) :",
            file=sys.stderr,
        )
        for fichier in manquants:
            print(f"  {PAGE}{urllib.parse.quote(fichier)}", file=sys.stderr)
        sys.exit(1)

    print("Toutes les images ont un auteur et une licence.")


if __name__ == "__main__":
    main()
