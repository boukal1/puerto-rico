# Porto Rico · 24 décembre 2026 → 9 janvier 2027

Tour de l'île en boucle, sept voyageurs, six étapes. Ce dépôt tient la mémoire du
voyage et publie le dossier illustré.

**Dossier publié :** https://boukal1.github.io/puerto-rico/

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
│   ├── verifier.yml           # HTML à jour + aucune donnée sensible
│   └── pages.yml              # publie docs/ sur GitHub Pages
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
cp .motifs-sensibles.exemple .motifs-sensibles && $EDITOR .motifs-sensibles
```

Si le hook ne se déclenche pas, ou si la CI échoue sur `Permission denied`, c'est le
bit exécutable qui manque dans l'index Git :

```bash
git update-index --chmod=+x verifier-avant-push.sh
```

La publication est tenue par `.github/workflows/pages.yml` : tout push sur `main` qui
touche `docs/`, `MEMOIRE.md` ou le générateur déploie `docs/` sur Pages. Rien à régler
dans `Settings` — `actions/configure-pages` bascule la source sur GitHub Actions au
premier passage. Le workflow refuse de publier si `docs/index.html` ne correspond plus
à `MEMOIRE.md` : on ne met pas en ligne un dossier périmé.

Aucune étape de build : le HTML est un fichier autonome, CSS embarqué, et c'est le
fichier committé qui est servi.

`voyage.depot_url` est renseigné dans `MEMOIRE.md` : chaque étape du dossier porte un
lien vers sa fiche de réservation.

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

Le script est en deux moitiés, et la séparation est le fond du sujet :

- **les formes** sont dans le script, parce qu'elles ne révèlent rien : adresse
  e-mail, numéro de neuf chiffres ou plus, code confidentiel en `NNNN.NNN.NNN` ;
- **les valeurs exactes** sont dans `.motifs-sensibles`, ignoré par Git. C'est là que
  vont les codes alphanumériques, qu'aucune forme ne sait isoler sans attraper au
  passage les couleurs hexadécimales du CSS. Modèle commenté :
  `.motifs-sensibles.exemple`.

Sans `.motifs-sensibles`, le script tourne quand même et le dit : les formes seules
sont vérifiées. C'est le mode dans lequel tourne la CI, qui n'a pas le fichier.

Il désigne les lignes fautives par `fichier:ligne` sans jamais recopier ce qu'il a
trouvé : les logs d'Actions d'un dépôt public sont publics.

Les confirmations d'origine restent hors du dépôt. `confirmations/` et `*.pdf` sont
ignorés par Git : c'est l'endroit prévu pour les garder en local.

## Impression

Le dossier embarque une feuille `@media print` : fonds clarifiés, mise en page
resserrée, étapes insécables, une étape par bloc. Ctrl/Cmd+P suffit.

## Alternatives de déploiement

Le workflow sert le HTML committé : l'historique porte un artefact généré, en échange
de quoi `git log docs/index.html` raconte le voyage.

- **Sans workflow.** `Settings → Pages → Deploy from a branch → main /docs` suffit :
  `docs/.nojekyll` est déjà là pour ça. Supprimer alors `pages.yml`, sinon les deux
  sources se disputent le déploiement. On perd le garde-fou qui empêche de publier un
  HTML périmé.
- **Sans HTML committé.** Générer dans le pipeline : `pip install pyyaml`,
  `python3 outils/generer.py`, puis `upload-pages-artifact`. Le `git log` sur
  `docs/index.html` disparaît, celui sur `MEMOIRE.md` reste.

## Licence

Textes et mise en page : usage privé.
Photographies : Wikimedia Commons, licences Creative Commons. Les attributions
exigées par CC BY / BY-SA sont dans `CREDITS.md` ; `python3 outils/credits.py` les
récupère depuis l'API Commons et réécrit le tableau.
