#!/usr/bin/env bash
# Dépôt public : empêche la publication d'identifiants de réservation.
# Installation en hook : ln -sf ../../verifier-avant-push.sh .git/hooks/pre-commit
set -uo pipefail

MOTIFS='VALEURS_RETIREES_DE_L_HISTORIQUE'  # voir .motifs-sensibles

code=0

if grep -rInE "$MOTIFS" --include='*.md' --include='*.html' --include='*.yml' . 2>/dev/null; then
  echo >&2
  echo "ARRÊT : identifiant de réservation ou adresse e-mail détecté." >&2
  echo "Ce dépôt est public. Voir reservations/README.md." >&2
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
