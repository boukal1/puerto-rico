---
# =====================================================================
#  Données du voyage. Source unique : docs/index.html est GÉNÉRÉ d'ici.
#  Après toute modification :  python3 outils/generer.py
# =====================================================================

voyage:
  titre: Porto Rico
  sous_titre: le tour de l'île
  periode: 24 décembre 2026 → 9 janvier 2027
  nuits: 16
  etapes_nb: 6
  voyageurs: 6 adultes · 1 ado
  depart: Genève, 24 déc. 11h20
  retour: Genève, 10 janv. 07h35
  # Renseigner après création du dépôt, pour lier les fiches de réservation.
  depot_url: "https://github.com/boukal1/puerto-rico"
  image_hero:
    fichier: Castillo_San_Felipe_Del_Morro_(16869927311).jpg
    alt: Le Castillo San Felipe del Morro et la baie de San Juan

principe: >
  Le parcours suit la côte dans un seul sens : nord, ouest, sud, îles, est, puis
  retour sur San Juan. Chaque journée de transfert devient une journée de visite,
  parce que la route passe naturellement par ce qu'il y a à voir. Les trois jours où
  le pays s'arrête — le 25 décembre, le 1er et le 6 janvier — tombent volontairement
  sur des étapes calmes.

bandeau:
  - fichier: Aerial_View_Of_Old_San_Juan.jpg
    alt: Vue aérienne du Vieux San Juan
  - fichier: Salinas_De_Cabo_Rojo_and_Wildlife_Refuge_in_Puerto_Rico.jpg
    alt: Les salines de Cabo Rojo
  - fichier: La_playa_negra_Vieques.jpg
    alt: Playa Negra, plage de sable noir à Vieques
  - fichier: El_Yunque_National_Forest_Flora.jpg
    alt: La forêt tropicale d'El Yunque

etapes:
  - numero: I
    nom: Dorado
    repli: "Pluie : Casa Bacardí à Cataño et le Museo de Arte de Puerto Rico se visitent à couvert. Sinon les villas, qui sont équipées pour ça."
    region: Côte nord
    dates_courtes: 24 → 27 déc.
    base: Hyatt Vacation Club, Hacienda del Mar
    route: SJU · 40 min
    dates: Jeudi 24 → dimanche 27 décembre · 3 nuits · 2 villas
    coords: N 018° 28.226 · W 66° 19.232 — 301 Highway 693, Dorado
    fiche: reservations/02-dorado-hyatt.md
    image:
      fichier: Castillo_San_Felipe_del_Morro_Sunset_in_San_Juan,_Puerto_Rico.jpg
      alt: El Morro au coucher du soleil
    image_legende: El Morro au couchant — excursion du 26 décembre
    vignettes:
      - fichier: Aerial_View_Of_Old_San_Juan.jpg
        alt: Le casco de San Juan vu du ciel
      - fichier: Cannons_Castillo_San_Felipe_del_Morro.jpg
        alt: Canons du Castillo San Felipe del Morro
      - fichier: Sunset_from_Old_San_Juan_-_panoramio.jpg
        alt: Coucher de soleil depuis le Vieux San Juan
    vignettes_legende: Le casco vu du ciel · Les canons du fort · Le soir sur les remparts
    intro: >
      Une base tranquille à quarante minutes de l'aéroport, avec cuisine dans les
      villas : exactement ce qu'il faut pour une arrivée tardive un soir de
      Nochebuena, quand plus rien n'est ouvert.
    jours:
      - quand: Jeu. 24
        texte: "**Arrivée.** Atterrissage SJU 22h22, récupération des voitures, route vers Dorado. Installation vers minuit."
      - quand: Ven. 25
        texte: "**Noël.** Piscines, Playa Sardinera, la roche d'Ojo del Buey. Dîner cuisiné dans les villas."
      - quand: Sam. 26
        texte: "**Vieux San Juan.** El Morro et les remparts, le Paseo del Morro, les ruelles pavées. Retour par les kiosques de Piñones au coucher du soleil."
    alerte: "**À régler avant le départ.** La réservation annonce une arrivée « entre 21h et 22h ». Avec un atterrissage à 22h22, prévenir l'hôtel. Côté voitures, tout est en place : deux véhicules chez Enterprise, comptoir ouvert 24 h sur 24, retraits à 23:30."
    note: "Les rues du casco sont impraticables en voiture : viser le parking Doña Fela ou Covadonga."

  - numero: II
    nom: Rincón
    repli: "Houle trop forte pour Steps Beach : se replier sur Crash Boat, nettement plus abritée, ou descendre vers Cabo Rojo au sud. Pluie : Museo El Cemí et l'artisanat de Jayuya."
    region: Côte ouest
    dates_courtes: 27 → 30 déc.
    base: Rincon Beach Resort
    route: 2 h
    dates: Dimanche 27 → mercredi 30 décembre · 3 nuits · 2 chambres deluxe
    coords: N 018° 17.733 · W 67° 12.536 — Road 115 km 5.8, Rincón
    fiche: reservations/03-rincon-beach-resort.md
    image:
      fichier: Puerto_Rico_Beaches_01_(cropped).jpg
      alt: Plage de la côte ouest de Porto Rico
    image_legende: La côte ouest, capitale du surf portoricain
    vignettes:
      - fichier: AERIAL_VIEW_LOOKING_EAST_-_Faro_de_Punta_Higuero,_Punta_Higuero,_Centro_Puntas,_Rincon_Municipio,_PR_HAER_PR,67-PUNTS,1-3.tif
        alt: Vue aérienne du phare de Punta Higüero
      - fichier: The_Ocean_From_The_Battlement_(147646121).jpeg
        alt: L'océan depuis les remparts
    vignettes_legende: Le phare de Punta Higüero · L'océan côté large
    intro: >
      Rincón a accueilli le championnat du monde de surf en 1968 et ne s'en est
      jamais remis. En décembre la houle d'hiver arrive du nord : spectaculaire à
      regarder, sérieuse à respecter.
    jours:
      - quand: Dim. 27
        texte: "**Transfert par la côte nord.** Cueva del Indio et ses pétroglyphes taïnos, la crique de Mar Chiquita — baignade seulement si la houle du nord est faible, voir l'encadré —, déjeuner de poisson à Arecibo. Arrivée pour le coucher du soleil."
      - quand: Lun. 28
        texte: "**Snorkeling.** Steps Beach et la réserve marine de Tres Palmas le matin, tortues vertes fréquentes. Le phare de Punta Higüero en fin de journée, et Domes Beach juste en dessous : la plage des surfeurs, et le poste d'observation des baleines depuis la terre. Cours de surf possible."
      - quand: Mar. 29
        texte: "**Aguadilla et Isabela.** Crash Boat Beach, les ruines en bord de mer, puis les piscines naturelles de Playa Montones à Isabela — protégées par le récif, la baignade la plus tranquille de la côte pour les trois générations. Sunset à Playa Jobos, à deux minutes."
    alerte: "**Baignade.** Courants d'arrachement fréquents de décembre à février sur les côtes nord et ouest. Se baigner là où d'autres se baignent, et garder un œil sur l'ado. **Mar Chiquita demande sa propre prudence** : au-delà de quatre pieds de houle du nord, les chenaux entre les rochers deviennent dangereux, et la crique reçoit des vagues de fond imprévisibles même par mer calme en apparence. Vérifier le bulletin le matin même, rester du côté gauche de la crique, garder les petits à portée de bras — et ne grimper sur aucun rocher : le calcaire est glissant et coupant."
    note: "Baleines à bosse : le parc du phare et Domes Beach sont les meilleurs postes depuis la terre, à l'aube ou en fin d'après-midi, jumelles utiles. Mais fin décembre, c'est trop tôt pour en faire une journée : la fenêtre fiable court de la mi-janvier à mars, février étant le sommet, et les sorties en bateau ne tournent qu'à partir de la mi-janvier. Une baleine avant le 30 décembre serait une chance, pas un programme."

  - numero: III
    nom: Ponce
    repli: "Tout le programme du 31 est à couvert, la pluie ne change rien. Mer agitée : Caja de Muertos et Gilligan's Island ne sortent pas, journée resort."
    region: Côte sud
    dates_courtes: 30 déc. → 2 janv.
    base: Hilton Ponce Golf & Casino
    route: 2 h
    dates: Mercredi 30 déc. → samedi 2 janvier · 3 nuits · petit-déjeuner inclus
    coords: N 017° 58.300 · W 66° 36.144 — 1150 Caribe Avenue, Ponce
    fiche: reservations/04-ponce-hilton.md
    image:
      fichier: Parque_de_Bombas,_Ponce,_Puerto_Rico.jpg
      alt: Le Parque de Bombas, ancienne caserne de pompiers rouge et noire de Ponce
    image_legende: Parque de Bombas, 1882 — Plaza Las Delicias, Ponce
    vignettes:
      - fichier: Historic_Faro_Los_Morrillos_de_Cabo_Rojo_in_Puerto_Rico.jpg
        alt: Le phare de Los Morrillos à Cabo Rojo
      - fichier: Playa_Sucia,_Cabo_Rojo,_Puerto_Rico.jpg
        alt: Playa Sucia à Cabo Rojo
      - fichier: Salinas_De_Cabo_Rojo_and_Wildlife_Refuge_in_Puerto_Rico.jpg
        alt: Les salines de Cabo Rojo
    vignettes_legende: "Sur la route du 30 : le phare de Cabo Rojo · Playa Sucia · les salines roses"
    intro: >
      « La Perla del Sur » a gardé son architecture créole et son tempo lent. C'est
      la ville où passer le réveillon : la Plaza Las Delicias s'anime vers minuit, et
      la mer du sud est enfin calme.
    jours:
      - quand: Mer. 30
        texte: "**Transfert par le sud-ouest.** Le phare de Cabo Rojo entre les salines roses et la falaise blanche, Playa Sucia en contrebas, déjeuner de fruits de mer à Joyuda, la forêt sèche de Guánica."
      - quand: Jeu. 31
        texte: "**Ponce historique.** Le Parque de Bombas, le Museo de Arte, le Castillo Serrallés et le panorama de la Cruceta del Vigía. Déjeuner sur la promenade de La Guancha. **Réveillon** à l'hôtel puis sur la place."
      - quand: Ven. 1er
        texte: "**Récupération.** Tout est fermé. Piscine, plage. Éventuellement Gilligan's Island depuis Guánica si les bateaux tournent. Valises « légères » pour Vieques le soir."
    note: "Tradition locale : douze grains de raisin à minuit, un par coup d'horloge. Prévoyez-les, ça fait toujours son effet."

  - numero: IV
    nom: Vieques
    repli: "Forte pluie : les pistes du refuge deviennent impraticables, se rabattre sur Sun Bay et Esperanza, accessibles par route goudronnée. Mosquito Bay annulée pour météo : report possible sur la nuit du 4, c'est la raison pour laquelle elle est programmée le 3."
    region: Île
    dates_courtes: 2 → 5 janv.
    base: Haven House, Calle 1
    route: 2 h 15 + mer
    dates: Samedi 2 → mardi 5 janvier · 3 nuits · Haven House
    coords: Calle 1, Vieques 00765
    fiche: reservations/05-vieques-haven-house.md
    image:
      fichier: Sunbay_beach,_Vieques_-_panoramio_(1).jpg
      alt: Sun Bay, la grande plage en croissant de Vieques
    image_legende: Sun Bay (Sombé) — côte sud de Vieques
    vignettes:
      - fichier: La_playa_negra_Vieques.jpg
        alt: Playa Negra, sable volcanique noir
      - fichier: Puerto_Real,_Vieques,_Puerto_Rico_-_panoramio.jpg
        alt: Puerto Real, près d'Esperanza
      - fichier: Sunbay_beach,_Vieques_-_panoramio_(2).jpg
        alt: Sun Bay, autre vue
    vignettes_legende: Playa Negra · Puerto Real, près d'Esperanza · Sun Bay
    intro: >
      Neuf mille habitants, deux villages, et les deux tiers de l'île classés en
      refuge naturel depuis le départ de la Navy. Des kilomètres de plage sans une
      seule construction, des chevaux en liberté sur les routes, et la baie
      bioluminescente la plus brillante du monde.
    jours:
      - quand: Sam. 2
        texte: "**Traversée.** Route Ponce → Ceiba, dépôt des voitures, avion ou ferry. Récupération des jeeps, installation à 15h. Coucher de soleil sur le malecón d'Esperanza."
      - quand: Dim. 3
        texte: "**Le refuge.** Playa Caracas puis La Chiva — viser les entrées 4 et 9 —, pistes en terre, aucun service : glacière et ombre à emporter. **Les grilles du refuge ferment au coucher du soleil**, prévoir de ressortir avant. **Le soir, kayak sur Mosquito Bay** — la lune est presque nouvelle, les conditions sont idéales."
      - quand: Lun. 4
        texte: "**L'autre visage.** Playa Negra et son sable volcanique au bout d'un lit de rivière, Sun Bay, le fort Conde de Mirasol — le dernier bâti par les Espagnols dans les Amériques."
    alerte: "**Le point critique du voyage.** Sept places sur la même traversée un 2 janvier, c'est incertain — et la date n'est pas encore ouverte à la réservation : surveiller l'ouverture des ventes, prendre l'avion depuis Ceiba et garder le ferry comme option. Les jeeps sur place se réservent des mois à l'avance."
    note: "Ni crème solaire ni antimoustique avant la sortie sur la baie : les produits sont interdits dans l'eau."

  - numero: V
    nom: Fajardo
    repli: "La PR-191 ferme régulièrement pour intempéries. Si El Yunque est inaccessible le 7 : permuter avec la journée Palomino du 6, ou basculer sur Seven Seas et la réserve de Cabezas de San Juan."
    region: Nord-est
    dates_courtes: 5 → 8 janv.
    base: El Conquistador Resort
    route: 15 min
    dates: Mardi 5 → vendredi 8 janvier · 3 nuits · 2 chambres vue océan
    coords: N 018° 21.527 · W 65° 37.707 — 1000 El Conquistador Avenue
    fiche: reservations/06-fajardo-el-conquistador.md
    image:
      fichier: El_Yunque_National_Forest_View.jpg
      alt: La forêt tropicale d'El Yunque
    image_legende: El Yunque — la seule forêt tropicale du système forestier américain
    vignettes:
      - fichier: Road_through_El_Yunque_National_Forest.jpg
        alt: La route PR-191 dans El Yunque
      - fichier: El_Yunque_National_Forest_Flora.jpg
        alt: Flore d'El Yunque
      - fichier: Playa_La_Pared_en_Luquillo,_Puerto_Rico.jpg
        alt: Playa La Pared à Luquillo
    vignettes_legende: La route PR-191 · La flore de la forêt · La plage de Luquillo, au retour
    intro: >
      Un resort perché à quatre-vingt-dix mètres au-dessus de la mer, avec sa propre
      île privée à huit minutes de bateau. Et, à quarante-cinq minutes de route,
      El Yunque.
    jours:
      - quand: Mar. 5
        texte: "**Retour et installation.** Traversée du matin, récupération des voitures à Ceiba, check-in à 16h. Le soir, **Víspera de Reyes** : les enfants déposent de l'herbe sous leur lit pour les chameaux des Rois mages."
      - quand: Mer. 6
        texte: "**Día de Reyes.** Jour férié majeur, tout est fermé dehors : journée sur **Isla Palomino**, l'île privée du resort. Réserver les places au bateau dès le check-in. Le soir, poisson au village de Las Croabas."
      - quand: Jeu. 7
        texte: "**El Yunque.** Départ 7h15 pour être à l'entrée avant 8h. La Coca Falls, la tour Yokahú, Juan Diego, puis Big Tree ou Mt Britton. Descente par les kiosques de Luquillo, fin de journée à Playa Azul."
    alerte: "**Culebra : une journée entière, à arbitrer contre El Yunque.** Cette étape n'a pas de jour libre — le 5 est un jour d'arrivée, le 6 est férié et se passe sur Isla Palomino, le 7 est El Yunque. Culebra prendrait donc la place du 7. Deux façons d'y aller. Le ferry depuis Ceiba, à vingt minutes du resort, est le moins cher mais le plus risqué : les résidents de Culebra ont une priorité d'embarquement réelle, un billet confirmé ne garantit pas de monter, et les voitures de location sont interdites à bord — se garer à Ceiba et louer sur place. Le catamaran au départ de Fajardo est plus sûr : il combine Flamenco Beach et Culebrita, qui n'est accessible que par bateau, et supprime la loterie du ferry. Compter 11 à 12 h de journée dans les deux cas. **Recommandation : garder El Yunque**, plus court et accessible aux trois générations, et réserver Culebra pour un prochain voyage — ou trancher tôt, le catamaran se remplit vite."
    note: "L'entrée d'El Yunque est gratuite et sans réservation, mais le stationnement est plafonné et se remplit dans la matinée. Deux litres d'eau par personne : il n'y a aucune restauration dans la forêt."

  - numero: VI
    nom: Isla Verde
    repli: "Aucune : journée tampon sans programme à sauver."
    region: Transit
    dates_courtes: 8 → 9 janv.
    base: Residence Inn Isla Verde
    route: 1 h
    dates: Vendredi 8 → samedi 9 janvier · 1 nuit · 2 studios
    coords: N 018° 26.493 · W 66° 1.031
    fiche: reservations/07-isla-verde-residence-inn.md
    image:
      fichier: Castillo_San_Felipe_del_Morro_from_air_-Fuerte_San_Felipe_del_Morro.jpg
      alt: Vue aérienne du Castillo San Felipe del Morro et de la baie de San Juan
    image_legende: La pointe de San Juan, vue du ciel
    vignettes:
      - fichier: Street_facing_bay._Calle_frente_a_la_bahía_de_San_Juan.jpg
        alt: Rue donnant sur la baie de San Juan
      - fichier: Sunset_from_Old_San_Juan_-_panoramio.jpg
        alt: Coucher de soleil depuis le Vieux San Juan
    vignettes_legende: Une rue descendant vers la baie · Dernier soir
    intro: >
      Une nuit tampon à cinq minutes de l'aéroport, uniquement là pour rendre le
      départ de 5h30 supportable.
    jours:
      - quand: Ven. 8
        texte: "**Repli.** Bagages déposés, **voitures rendues à l'aéroport le jour même** — pas à l'aube. Derniers achats au Vieux San Juan ou plage à deux cents mètres. Dîner tôt, coucher à 22h."
      - quand: Sam. 9
        texte: "**Départ.** Taxi à 5h30, monospace 7 places déjà réservé. Neuf minutes jusqu'à SJU."

vols:
  intro: Genève ⇄ San Juan via Washington Dulles. Sept voyageurs, classe économique.
  lignes:
    - jour: Jeu. 24 déc.
      vol: UA 749
      trajet: Genève → Washington Dulles
      appareil: Boeing 767-300 · 9 h 35
      horaires: 11:20 → 14:55
    - jour: Jeu. 24 déc.
      vol: UA 2025
      trajet: Washington Dulles → San Juan
      appareil: Boeing 737 MAX 9 · 3 h 53
      horaires: 17:29 → 22:22
    - jour: Sam. 9 janv.
      vol: UA 2022
      trajet: San Juan → Washington Dulles
      appareil: Boeing 737 MAX 8 · 4 h 05
      horaires: 08:10 → 11:15
    - jour: Sam. 9 janv.
      vol: UA 748
      trajet: Washington Dulles → Genève
      appareil: Boeing 767-300 · 8 h 10 · arrivée dim. 10
      horaires: 17:25 → 07:35
  alerte: "**Correspondance aller : 2 h 34 à Dulles.** C'est le premier point d'entrée aux États-Unis : contrôle d'immigration, douane et re-dépose des bagages. Un 24 décembre, c'est serré. L'ESTA doit être validée pour les sept, au moins 72 h avant. Au retour, 6 h 10 d'escale à Dulles."

actions:
  intro: Classé par ce qui fait tomber le reste du voyage si ça manque.
  lignes:
    - quoi: 2 jeeps à Vieques
      urgence: Immédiat
      critique: true
      pourquoi: Le parc de l'île est minuscule. Sans véhicule, les plages du refuge sont inaccessibles.
    - quoi: Traversée pour 7 vers Vieques
      urgence: Dès ouverture
      critique: true
      pourquoi: La date du 2 janvier n'est pas encore ouverte à la réservation. Surveiller l'ouverture des ventes, prendre l'avion depuis Ceiba en priorité et tenter le ferry en parallèle. Jamais l'inverse.
    - quoi: Mosquito Bay, nuit du 3
      urgence: Dès que possible
      critique: false
      pourquoi: "Sept kayaks, c'est presque un groupe complet : demander une sortie privatisée."
    - quoi: Réveillon du 31 à Ponce
      urgence: Oct.–nov.
      critique: false
      pourquoi: Les dîners de gala se remplissent.
    - quoi: ESTA × 7
      urgence: ≥ 72 h avant
      critique: false
      pourquoi: Entrée aux États-Unis à Washington Dulles.

echeances:
  - date: 29 nov. 2026
    quoi: Hilton Ponce
    consequence: Déjà prépayé intégralement
    critique: true
  - date: 16 déc. 2026
    quoi: Hyatt Hacienda del Mar
    consequence: Pénalité par villa
    critique: false
  - date: 23 déc. 2026
    quoi: Rincon Beach Resort
    consequence: Pénalité par chambre
    critique: false
  - date: 2 janv. 2027
    quoi: El Conquistador
    consequence: Première nuit déjà prépayée
    critique: false
  - date: 5 janv. 2027
    quoi: Residence Inn Isla Verde
    consequence: Pénalité par studio
    critique: false

pratique:
  - titre: Conduite
    texte: >
      Permis suisse accepté. Panneaux en espagnol, vitesses en miles/h, distances en
      km, essence en litres. Demander le transpondeur AutoExpreso : les péages
      n'acceptent plus les espèces.
  - titre: Argent
    texte: >
      Dollar US. Cartes partout sauf kiosques de plage, parkings, petits commerces de
      Vieques. Garder 150–200 $ en petites coupures.
  - titre: Téléphone
    texte: >
      Réseaux américains : Porto Rico compte comme les États-Unis chez la plupart des
      opérateurs suisses. Couverture inégale dans le refuge de Vieques et à El Yunque.
  - titre: Météo
    texte: >
      25 à 29 °C, averses courtes, saison des ouragans terminée. Houle d'hiver sur les
      côtes nord et ouest ; sud, est et Vieques nettement plus calmes.
  - titre: Santé
    texte: >
      Antimoustiques, la dengue est endémique. Crème solaire minérale, obligatoire
      dans les réserves marines et sur la baie bioluminescente.
  - titre: Jours fermés
    texte: >
      25 décembre, 1er et 6 janvier : restaurants, musées, El Yunque et la plupart des
      commerces. Ces journées sont déjà prévues sans programme extérieur.

bandeau_final:
  - fichier: Cannons_Castillo_San_Felipe_del_Morro.jpg
    alt: Canons du fort El Morro
  - fichier: Playa_Sucia,_Cabo_Rojo,_Puerto_Rico.jpg
    alt: Playa Sucia, Cabo Rojo
  - fichier: Sunbay_beach,_Vieques_-_panoramio_(2).jpg
    alt: Sun Bay, Vieques
  - fichier: Playa_La_Pared_en_Luquillo,_Puerto_Rico.jpg
    alt: Playa La Pared, Luquillo
---

# Mémoire du projet

Ce fichier est la source unique. `docs/index.html` en est **généré** : ne jamais
l'éditer à la main, il est écrasé à chaque exécution de `outils/generer.py`.

Le front matter ci-dessus contient les données. Ce qui suit est la mémoire humaine :
ce qu'on a décidé, pourquoi, et ce qui reste ouvert.

## Décisions arrêtées

**Une boucle dans un seul sens.** Nord → ouest → sud → îles → est → San Juan. Aucun
retour en arrière, et les journées de transfert servent de journées de visite.

**Les trois jours fériés sont des journées calmes.** Le 25 décembre, le 1er et le
6 janvier, presque tout ferme sur l'île, y compris El Yunque. Ces trois dates sont
placées sur des étapes où le programme se passe de l'extérieur.

**Les sept vont à Vieques**, du 2 au 5 janvier. Décision prise après avoir un moment
envisagé un séjour en solo, avec le reste du groupe basé à Luquillo. Abandonné.

**El Conquistador est décalé au 5 → 8 janvier**, contre 6 → 9 initialement. C'est ce
décalage qui referme le trou du 5 janvier et rend cohérente la nuit du 8 à Isla Verde.

**Deux véhicules de location, pas un.** Sept personnes plus seize jours de bagages ne
tiennent pas dans un monospace unique.

**El Yunque est placé le 7 janvier**, seule journée ouvrable du segment de Fajardo. Le
6 étant férié, la journée se passe sur Isla Palomino, ce qui tombe bien.

**La baie bioluminescente se fait à Vieques, pas à Fajardo.** Mosquito Bay est très
supérieure à la Laguna Grande ; en faire les deux serait redondant. Programmée la
nuit du 3 plutôt que du 4, pour garder une marge de report météo.

**Dépôt public, données de réservation exclues.** Voir `reservations/README.md`.

## À ne pas oublier

- **Prévenir le Hyatt de l'heure d'arrivée réelle.** La réservation annonce 21 h–22 h,
  le vol atterrit à 22:22, l'installation se fera vers minuit.
- **Vérifier l'horaire du comptoir de location à SJU le 24 au soir.** Plusieurs ferment
  à minuit, et c'est la Nochebuena.
- **Réserver les jeeps de Vieques maintenant.** C'est la contrainte la plus dure du
  voyage : le parc de l'île est minuscule.
- **Privilégier l'avion Ceiba → Vieques.** Le ferry ne garantit pas sept places sur la
  même traversée un 2 janvier.
- **Déclarer sept voyageurs à Haven House.**
- **Réclamer la confirmation d'El Conquistador** pour les dates 5 → 8 janvier.
- **Réserver les places du bateau vers Isla Palomino dès l'enregistrement** du 5.
- **Rendre les voitures le 8, pas le 9 à l'aube.**
- **Faire les courses le premier soir à Vieques.** Ravitaillement limité, fermeture tôt.
- **Douze grains de raisin** pour le 31 à minuit.
- **Bagages allégés pour Vieques** : préparés le soir du 1er janvier.

## Adresses et prestataires cités

Repérages faits pendant la préparation. Rien n'est réservé sauf mention contraire.

### Tables

| Où | Étape | Note |
|---|---|---|
| Deaverdura | Vieux San Juan | Cuisine créole simple, midi |
| Café Manolín | Vieux San Juan | Institution de quartier, midi |
| Kiosques de Piñones | Retour de San Juan, 26 déc. | Fritures les pieds dans le sable, espèces uniquement |
| La Copa Llena (The Black Eagle) | Rincón | Vue mer |
| English Rose | Rincón | Vue sur les hauteurs |
| Ola Lola's Garden Bar | Aguadilla, 29 déc. | Institution locale, burgers |
| Levain | Aguadilla | Boulangerie-café |
| Happy Belly's | Playa Jobos, Isabela | Sunset |
| Tino's, Island View | Joyuda, 30 déc. | Fruits de mer sur la route de Ponce |
| La Guancha | Ponce | Promenade en bois du port, kiosques |
| Duffy's, El Blok, Bili | Esperanza, Vieques | Sur le malecón |
| Las Croabas | Fajardo, 6 janv. | Village de pêcheurs, poisson sans la note du resort |
| Kiosques de Luquillo | Retour d'El Yunque, 7 janv. | Une soixantaine d'échoppes le long de la PR-3 |

### Prestataires

| Service | Noms repérés | Quand réserver |
|---|---|---|
| Jeeps à Vieques | Maritza's Car Rental, Vieques Car Rental, Coqui Car Rental | Immédiatement — parc minuscule |
| Vol Ceiba → Vieques | Vieques Air Link, Cape Air | Immédiatement — petits appareils, franchise bagages limitée |
| Ferry Ceiba ⇄ Vieques | puertoricoferry.com | Dès ouverture des ventes, en second recours |
| Mosquito Bay | Taíno Aqua Adventures, Abe's Snorkeling, Black Beard Sports | Sortie privatisée pour 7 |
| Voitures à SJU | Enterprise, Car Rental Center du parking | **2 véhicules réservés**, 24 déc. → 8 janv. |
| Catamaran depuis Fajardo | East Island Excursions, Salty Dog, Erin Go Bragh | Voie recommandée si la journée Culebra est retenue |
| Cours de surf | Rincón Surf School, Puntas Surf School | Sur place, 28 déc. |
| Cabezas de San Juan | Para la Naturaleza | Visite guidée uniquement, sur réservation |
| Cueva Ventana | Réservation en ligne | Arrêt optionnel du 27 déc. |

## Budget hébergement

Estimations en francs telles qu'affichées à la réservation. Les établissements
facturent en dollars, au taux du jour du paiement : ces montants bougeront.

| Étape | Montant |
|---|---|
| Hyatt Hacienda del Mar, Dorado | ~2 744 |
| Rincon Beach Resort | ~1 861 |
| Hilton Ponce | ~2 780 |
| Haven House, Vieques | 2 168 |
| El Conquistador, Fajardo | ~2 069 |
| Residence Inn Isla Verde | ~652 |
| **Total** | **~12 274 CHF** |

Le montant d'El Conquistador correspond à la réservation initiale du 6 au 9 janvier.
Il est susceptible de changer avec le décalage au 5 → 8, ce qui est une raison de
plus de réclamer la confirmation.

Non compris : vols, deux locations de véhicules sur seize jours, deux jeeps à
Vieques, traversées vers Vieques, excursions, carburant, péages, repas, et les
dépôts de garantie de 250 + 200 + 200 USD restitués après séjour.

## Logique météo

La saison des ouragans est terminée. Reste un régime d'hiver aux effets très
inégaux selon la côte, et c'est ce qui structure le placement des journées.

**Houle du nord, de décembre à février.** Elle frappe les côtes nord et ouest —
Dorado, Arecibo, Rincón, Isabela. Superbe pour le surf, dangereuse à la baignade,
avec des courants d'arrachement fréquents. Mar Chiquita est à regarder, pas à
nager. Les côtes sud, est et Vieques restent nettement plus calmes : c'est là que
se placent les vraies baignades du séjour.

**Averses courtes et fortes.** Elles ne ruinent pas une journée, sauf à deux
endroits : la PR-191 d'El Yunque ferme régulièrement pour intempéries, et les
pistes en terre du refuge de Vieques deviennent impraticables. Ces deux journées
ont donc une alternative, notée par étape dans le front matter sous la clé `repli`.

**Lune.** Presque nouvelle début janvier 2027, donc conditions d'obscurité idéales
pour Mosquito Bay. C'est un argument de plus pour ne pas déplacer cette sortie hors
du créneau du 2 au 5.

**Sargasses.** Peu présentes en hiver. Sun Bay peut néanmoins en accumuler sur sa
partie droite : passer de l'autre côté du cordon sableux, vers Esperanza.

## Points ouverts

| Sujet | État |
|---|---|
| Confirmation El Conquistador 5 → 8 janv. | en attente |
| Occupation Haven House déclarée à 1 voyageur | à régulariser |
| Location des 2 véhicules à SJU | à réserver |
| Location des 2 jeeps à Vieques | à réserver |
| Traversée Ceiba ⇄ Vieques pour 7 | à réserver |
| Sortie Mosquito Bay du 3 janvier | à réserver |
| Attributions photographiques (`CREDITS.md`) | à compléter |
| Fin des travaux au Hyatt | à vérifier avant départ |
| Rotation des bateaux vers Caja de Muertos / Gilligan's Island le 1er janvier | à confirmer sur place |

## Corrections apportées en cours de route

**Vols.** Une première version de ce dossier mentionnait un transit par Newark avec
une arrivée à 20h09. C'était faux. Le trajet réel passe par **Washington Dulles**,
avec une arrivée à **22:22**. Cette erreur avait des conséquences réelles sur la
soirée du 24 : elle est corrigée partout, mais c'est la raison pour laquelle l'heure
d'arrivée déclarée au Hyatt ne correspond plus.

## Convention

Toute modification du voyage se fait **dans le front matter de ce fichier**, puis :

```bash
python3 outils/generer.py
git add -A && git commit -m "..."
```

Le HTML régénéré est committé avec la modification, de sorte qu'un `git log` sur
`docs/index.html` raconte l'histoire du voyage.
