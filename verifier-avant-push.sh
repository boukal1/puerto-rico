#!/usr/bin/env bash
# Dépôt public : empêche la publication d'identifiants de réservation.
# Installation en hook : ln -sf ../../verifier-avant-push.sh .git/hooks/pre-commit
#
# Ce script ne contient aucune valeur sensible, et c'est le point :
#   - les motifs de FORME (e-mail, longueur d'un numéro, gabarit d'un code)
#     sont ici, ils ne révèlent rien ;
#   - les valeurs EXACTES vivent dans .motifs-sensibles, ignoré par Git, qui ne
#     quitte jamais la machine. Voir .motifs-sensibles.exemple.
#
# Les lignes fautives sont désignées par fichier:ligne, jamais recopiées : les
# logs d'Actions d'un dépôt public sont publics, un garde-fou n'y écrit pas ce
# qu'il protège.
set -uo pipefail

# Les chemins qui suivent sont relatifs à la racine : y aller, d'où qu'on appelle.
racine=$(git rev-parse --show-toplevel 2>/dev/null) && cd "$racine"

LISTE_EXACTE="${MOTIFS_SENSIBLES:-.motifs-sensibles}"

# Formes suffisamment caractéristiques pour ne rien attraper à tort dans ce
# dépôt — vérifié sur l'ensemble des fichiers suivis.
FORMES=(
  '[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}'
  '(^|[^0-9A-Za-z_(%])[0-9]{9,}([^0-9A-Za-z_)%]|$)'
  '[0-9]{4}\.[0-9]{3}\.[0-9]{3}'
)
LIBELLES=(
  "adresse e-mail"
  "numéro de confirmation (9 chiffres ou plus)"
  "code confidentiel Booking (NNNN.NNN.NNN)"
)

code=0

# En hook : les fichiers de l'index. Sinon (CI, appel à la main) : tout le suivi.
fichiers_a_lire() {
  local stages
  stages=$(git diff --cached --name-only --diff-filter=ACM 2>/dev/null)
  if [ -n "$stages" ]; then
    printf '%s\n' "$stages"
  else
    git ls-files 2>/dev/null || find . -type f -not -path './.git/*'
  fi
}

# grep -I saute les binaires ; -o est volontairement absent, on ne cite rien.
chercher() {
  local motif="$1" libelle="$2" touche=0 fichier ligne
  while IFS= read -r fichier; do
    [ -f "$fichier" ] || continue
    [ "$fichier" = "$LISTE_EXACTE" ] && continue
    while IFS= read -r ligne; do
      echo "  $fichier:$ligne — $libelle" >&2
      touche=1
    done < <(grep -InE "$motif" -- "$fichier" 2>/dev/null | cut -d: -f1)
  done < <(fichiers_a_lire)
  return $touche
}

for i in "${!FORMES[@]}"; do
  chercher "${FORMES[$i]}" "${LIBELLES[$i]}" || code=1
done

if [ -f "$LISTE_EXACTE" ]; then
  numero=0
  while IFS= read -r motif || [ -n "$motif" ]; do
    numero=$((numero + 1))
    case "$motif" in ''|\#*) continue ;; esac
    chercher "$motif" "valeur connue ($LISTE_EXACTE, ligne $numero)" || code=1
  done < "$LISTE_EXACTE"
else
  echo "Note : $LISTE_EXACTE absent — seules les formes sont vérifiées." >&2
  echo "       Les codes alphanumériques ne sont pas détectables par forme." >&2
  echo "       Voir $LISTE_EXACTE.exemple." >&2
fi

if [ $code -ne 0 ]; then
  echo >&2
  echo "ARRÊT : donnée de réservation détectée aux lignes ci-dessus." >&2
  echo "Ce dépôt est public. Voir reservations/README.md." >&2
fi

# Les confirmations d'origine n'ont rien à faire dans l'historique.
if fichiers_a_lire | grep -qiE '(^|/)confirmations/|\.pdf$'; then
  echo "ARRÊT : un PDF ou un fichier de confirmations/ est suivi par Git." >&2
  code=1
fi

if command -v python3 >/dev/null && [ -f outils/generer.py ]; then
  avant=$(sha1sum docs/index.html 2>/dev/null | cut -d' ' -f1)
  python3 outils/generer.py >/dev/null 2>&1 || true
  apres=$(sha1sum docs/index.html 2>/dev/null | cut -d' ' -f1)
  if [ "$avant" != "$apres" ]; then
    echo "docs/index.html était périmé — régénéré. Le réajouter à l'index :" >&2
    echo "  git add docs/index.html" >&2
    code=1
  fi
fi

[ $code -eq 0 ] && echo "OK — rien de sensible, HTML à jour."
exit $code
