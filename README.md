# Porto Rico · 24 décembre 2026 → 9 janvier 2027

Tour de l'île en boucle, sept voyageurs, six étapes. Ce dépôt tient la mémoire du
voyage et publie le dossier illustré.

**Dossier publié :** https://<utilisateur>.github.io/<depot>/

## Comment ça marche

```
MEMOIRE.md                 ← source unique
   ├─ front matter YAML    → données : étapes, dates, vols, échéances, images
   └─ corps markdown       → journal : décisions, à ne pas oublier, points ouverts
                │
      outils/generer.py
                │
        docs/index.html    ← GÉNÉRÉ, ne pas éditer
                │
         GitHub Pages
```

`reservations/` contient une fiche par réservation, réduite à l'opérationnel.

Le corps de `MEMOIRE.md` va plus loin que le dossier publié : décisions prises et
leur raison, choses à ne pas oublier, points ouverts, adresses et prestataires
repérés, budget hébergement, logique météo. C'est la partie qui survit à l'oubli.

## Structure

```
.
├── MEMOIRE.md                 # source unique + journal de projet
├── reservations/              # une fiche par réservation
│   ├── README.md              # index et politique de confidentialité
│   └── 01…08-*.md
├── outils/
│   ├── generer.py             # MEMOIRE.md → docs/index.html
│   └── credits.py             # attributions Commons → CREDITS.md
├── docs/                      # racine publiée
│   ├── index.html             # généré
│   └── .nojekyll
├── .github/workflows/
│   └── verifier.yml           # HTML à jour + aucune donnée sensible
├── verifier-avant-push.sh
├── CREDITS.md
└── .gitignore
```

## Modifier le voyage

Toujours dans `MEMOIRE.md`, jamais dans le HTML.

```bash
$EDITOR MEMOIRE.md
python3 outils/generer.py
git add -A && git commit -m "Décale El Conquistador au 5 janvier"
```

Le HTML régénéré part dans le même commit. `git log -p MEMOIRE.md` raconte alors
l'histoire du voyage, décision par décision.

## Mise en route

```bash
pip install pyyaml
git init -b main
git add . && git commit -m "Dossier de voyage Porto Rico 2026-2027"
gh repo create porto-rico-2027 --public --source=. --push
ln -sf ../../verifier-avant-push.sh .git/hooks/pre-commit
```

Si le hook ne se déclenche pas, ou si la CI échoue sur `Permission denied`, c'est le
bit exécutable qui manque dans l'index Git :

```bash
git update-index --chmod=+x verifier-avant-push.sh
```

Puis `Settings → Pages → Deploy from a branch → main /docs`. Aucune étape de build :
le HTML est un fichier autonome, CSS embarqué.

Une fois l'URL du dépôt connue, renseigner `voyage.depot_url` dans `MEMOIRE.md` :
chaque étape du dossier obtient alors un lien vers sa fiche de réservation.

## Dépôt public : ce qui n'y figure pas

Ni numéro de confirmation, ni code confidentiel, ni nom de voyageur, ni adresse
e-mail, ni téléphone privé. Détail et raisons dans `reservations/README.md`.

Deux réserves assumées, à trancher par le propriétaire du dépôt :

- **`MEMOIRE.md` contient le budget hébergement**, ajouté volontairement. C'est une
  donnée financière personnelle sur un dépôt public. Pour la sortir sans perdre le
  fichier en local : ajouter `MEMOIRE.md` à `.gitignore` — mais le HTML ne serait
  alors plus reproductible depuis le dépôt.
- **Un itinéraire publie des dates d'absence au domicile**, au jour près. C'est
  inhérent à l'exercice, et c'est exploitable. L'adresse n'y figure pas.

`verifier-avant-push.sh`, branché en hook `pre-commit`, refuse le commit si l'un de
ces éléments réapparaît, et vérifie au passage que `docs/index.html` correspond bien
à `MEMOIRE.md`. La CI refait les deux contrôles sur chaque push.

Les confirmations d'origine restent hors du dépôt. `confirmations/` et `*.pdf` sont
ignorés par Git : c'est l'endroit prévu pour les garder en local.

## Impression

Le dossier embarque une feuille `@media print` : fonds clarifiés, mise en page
resserrée, étapes insécables, une étape par bloc. Ctrl/Cmd+P suffit.

## Alternative de déploiement

Servir `/docs` depuis la branche est le plus simple, au prix d'un artefact généré
dans l'historique. Si tu préfères un dépôt sans HTML committé, remplace le job de
vérification par `actions/configure-pages` + `actions/deploy-pages`, en générant le
HTML dans le pipeline. Le `git log` sur `docs/index.html` disparaît alors, mais
celui sur `MEMOIRE.md` reste.

## Licence

Textes et mise en page : usage privé.
Photographies : Wikimedia Commons, licences Creative Commons. Les attributions
exigées par CC BY / BY-SA sont dans `CREDITS.md` ; `python3 outils/credits.py` les
récupère depuis l'API Commons et réécrit le tableau.
