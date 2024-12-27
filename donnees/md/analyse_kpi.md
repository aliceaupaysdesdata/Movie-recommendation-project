# Analyse des KPI et Visualisation

## 🎯 Objectifs de l'analyse
L'objectif de ce projet est d'explorer les bases de données IMDb et TMDb afin d'en tirer des insights pertinents à l'aide de visualisations PowerBI.

Les analyses porteront sur :

1. **Vue générale des bases de données (Oeuvres, Supports, Genres, Pays)**
2. **Les films les mieux notés et les caractéristiques qu'ils partagent.**
3. **L'évolution de la durée moyenne des films au fil des années.**
4. **L'identification des acteurs les plus présents et les périodes associées.**
5. **La comparaison entre les acteurs présents au cinéma et dans les séries.**
6. **L'âge moyen des acteurs.** 

---

## 📋 Méthodologie
### Étapes clés :

1. **Préparation des données :**
   - Nettoyage des datasets IMDb et TMDb pour éliminer les doublons et les valeurs manquantes.
   - Standardisation des formats de colonnes (dates, durées, notes, etc.).
   - Fusion des datasets pour enrichir les analyses (liens entre acteurs, films et séries).

2. **Exploration et création des KPI :**
   - Définition des indicateurs à suivre pour répondre aux objectifs.
   - Extraction et transformation des données nécessaires.

3. **Construction des visualisations Power BI :**
   - Création de rapports dynamiques et interactifs.
   - Mise en place de filtres et slicers pour explorer les données en détail.

---

##  **Schéma de liaison des Tables sur Power BI**
---

## Périmètre d'analyse

- ***Cinéma*** : Tous les films - hors Court Métrages
- ***Télévision*** : Uniquement TVSeries
- **Suppression des Films et Séries pour Adulte**

---

##  **📊 KPI** : Vue générale des bases de données

### Nombre d'oeuvres par supports, Ratio et Evolution par Décennie
<br>

![oeuvres_support](../images/kpi/3_répartition.PNG)
***Source : ImdB title.basics***

- Nombre total d'oeuvres (hors films Adulte) : ***834 859***
- Ratio des Supports : ***70,3% Cinéma, 29,7% Télévision***
- **Evolution dans le temps** :
  - Le cinéma connait une première période de croissance entre les 2 guerres mondiales, puis connait à partir des années 2000 une très forte croissance consécutive à l'***explosion*** d'internet et l'apparition des Plateformes de Streaming.
  - La télévision ***suit cette courbe*** à partir de 1950, dans une moindre mesure.
- Le nombre d'oeuvres cinématographiques restent pour chaque décennie **entre 40 et 50% supérieur** au nombre de Séries télévisées.

---

### Fréquences des Films par Genre au Cinéma
<br>

![genres](../images/kpi/4_genres.PNG)
***Source : ImdB title.basics***

- 3 Genres (Drame, Documentaire, Comédie) représentent ***79% des films***
- Le ***Drame*** occupe depuis toujours la 1ère place des genres de films.
- La période ***phare*** pour les films d'action est entre 1660 et 2000
- Depuis les années 2000, le ***documentaire*** ne cesse de croitre et représente 30% des oeuvres dans le top 5 des genres par décennie.

---

### Films par Genre 2000-2024 au Cinéma
<br>

![genres_2000](../images/kpi/4_genres_2000_2020.PNG)
***Source : ImdB title.basics***

- Une vue plus détaillée de la répartition des genres de films sur la période la plus prolifique (2000 - 2024)

---

### Séries par Genre 2000-2024 à la télévision
<br>

![genre_tv](../images/kpi/4_genres_tv.PNG)

- La répartition des genres à la télévision est différente, avec un place dédiée aux Séries ***'***Talk-Show'*** et ***'TV Réalité'***
- La ***Comédie*** est le genre le plus présent à la télévision ; qui reste donc un ***divertissement*** pour le public.
- Le ***Drame*** a toujours une place importante, l'objectif étant de créer des ***émotions*** aux téléspectateurs.

---
### Répartition des Films par Pays
<br>

![Pays](../images/kpi/7b_pays.PNG)
***Source : TmdB Full***

- L'***Amérique*** a produit ***37,67%*** des oeuvres cinématographiques et télévisuelles et s'affirme comme leader dans la production.
- L'***Europe*** et l'***Asie*** suivent dans le classement avec respectivement ***33,52%*** et ***26,23%***.
- Sans surprise, les ***Etats-Unis*** est le pays le plus prolifique en création cinématographique, suivi de l'***Inde***, le ***Japon***, la ***France*** et le ***Royaume-Uni***.
- Par la quantité d'oeuvres proposées, ces 5 pays sont des acteurs majeurs et doivent être intégrés dans la sélection du moteur de recherche.

---
### Films les mieux notés

#### Top 10 des films les mieux notés par Continent

##### Top 10 - Amérique
![TOP10Amerique](../images/kpi/10_TopFilms_Amerique.PNG)

##### Top 10 - Europe
![TOP10Europe](../images/kpi/10_TopFilms_Europe.PNG)

##### Top 10 - Asie
![TOP10Asie](../images/kpi/10_TopFilms_Asie.PNG)

##### Top 10 - Océanie
![TOP10Océanie](../images/kpi/10_TopFilms_Oceanie.PNG)

##### Top 10 - Afrique
![TOP10Afrique](../images/kpi/10_TopFilms_Afrique.PNG)
***Source : ImdB - TmdB***

- La note de chaque film est obtenue en calculant la moyenne pondérée entre les notes ImDb et TmdB en fonction du nombre de votes.
- Un filtre (> 5000 votes) a été appliqué pour discerner les films les plus populaires.
- Une analyse peut être faite en incluant les films où les nombre de votants sont inférieurs pour ***dénicher les pépites*** utiles pour le moteur de recherche et la future programmation.
- Une analyse peut être faite également par Genre de Films

### Évolution de la durée moyenne des films au fil des années
- **KPI :** Durée moyenne par décennie ou année.
- **Visualisation :**
  - Graphique en courbes montrant l'évolution au fil des décennies.
  - Histogramme pour une répartition plus détaillée.

---

##  **📊 KPI** : Analyse des acteurs dans la base de données

### Nombre d'acteurs au cinéma, à la télévision par décennie
<br>

![décennie_acteur](../images/kpi/6_décennie_acteur.PNG)
***Source : ImdB title.basics / name.basics***

- Entre 1950 et 2000, le nombre d'acteurs au cinéma et à la télévision est en croissance constante, en raison du développement mondial.
- A partir des années 2000, la croissance s'accélère; le nombre d'acteurs doublant pour chaque décennie pour atteindre **576K** acteurs dans les années 2010 pour le cinéma, et **340K** pour la télévision. Cela s'explique par le **démocratisation d'internet et des supports numériques** d'une part, et par l'apparition à partir de 2010 des **plateformes de Streaming**.

### Comparaison entre les acteurs présents au cinéma et dans les séries
- **KPI :** Proportion d'acteurs présents dans les films, les séries ou les deux.
- **Visualisation :**
  - Diagramme de Venn ou un graphique en barres empilées.
  - Tableau croisé dynamique pour une exploration plus fine.

---

### Identification des acteurs les plus présents et les périodes associées

#### Périmètre 
- Nous analysons la présence des acteurs selon le ***nombre d'apparitions*** dans les films. Le classement est établi sur le ***Top 15***.
- L'analyse est faite par continent de production des films / séries. Dans le rapport, l'analyse peut être filtrée par pays également.
- Les visuels ci dessous montrent un échantillon des analyses possibles.
- L'analyse est construite selon les grandes périodes du cinéma :
  - 1910-1949 : Du cinéma muet jusqu'à l'après guerre
  - 1950-1979 : L'age d'or d'Hollywood et le développement du cinéma et de la télévision
  - 1980-1999 : La démocratisation de la télévision et les débuts de la mondialisation
  - 2000-2024 : L'explosion d'internet, l'apparition des plateformes de Streaming
- Un focus est fait sur le ***Cinéma Français***

#### Au cinéma

##### Top 15 Acteurs en France
![top_15_acteur](../images/kpi/8_top_15_france.PNG)

##### Top 15 Acteurs en Amérique
![top_15_acteur](../images/kpi/8_top_15_amerique.PNG)

##### Top 15 Acteurs en Europe
![top_15_acteur](../images/kpi/8_top_15_europe.PNG)

##### Top 15 Acteurs en Asie
![top_15_acteur](../images/kpi/8_top_15_asie.PNG)

##### Top 15 Acteurs en Océanie
![top_15_acteur](../images/kpi/8_top_15_oceanie.PNG)

##### Top 15 Acteurs en Afrique
![top_15_acteur](../images/kpi/8_top_15_afrique.PNG)
***Source : ImdB title.basics / name.basics***

#### A la télévision

![top_15_télévision](../images/kpi/9_top_15_télévision.PNG)
***Source : ImdB title.basics / name.basics***



### 4. Âge moyen des acteurs
- **KPI :** Calcul de l'âge moyen des acteurs par période et par genre (homme/femme).
- **Visualisation :**
  - Graphique en barres pour la moyenne par décennie.
  - Carte de chaleur pour explorer la répartition par âge et genre.

### 5. Les films les mieux notés et les caractéristiques qu'ils partagent
- **KPI :** Moyenne des notes des films, analyse des caractéristiques communes (genres, réalisateurs, durée, année de sortie).
- **Visualisation :**
  - Tableau récapitulatif des films les mieux notés.
  - Graphique en bulles pour explorer les corrélations (durée, notes, genres).

---

## Livrables
1. Rapport Power BI complet avec :
   - Dashboard interactif.
   - Pages dédiées pour chaque KPI.

2. Documentation expliquant les étapes suivies, les transformations effectuées et les sources des données.

---

## Conclusion
Cette analyse permettra d'extraire des insights clés sur les tendances des acteurs, les films, et les séries, tout en mettant en avant les outils de visualisation Power BI pour une compréhension claire et efficace des données.

