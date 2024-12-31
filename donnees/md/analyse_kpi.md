# Analyse des KPI et Visualisation

## 🎯 Objectifs de l'analyse
L'objectif de ce projet est d'explorer les bases de données IMDb et TMDb afin d'en tirer des insights pertinents à l'aide de visualisations PowerBI.

Couplés à l'Etude de Marché précédemment réalisée, ces insights nous permettront de définir l'orientation stratégique pour la suite du projet et nos choix quant aux sélections d'oeuvres pour le moteur de recommandation.

Les principales analyses du dashboard présenteront :

1. **La vue générale des bases de données (Oeuvres, Supports, Genres, Pays)**
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
<br>

### Nombre d'oeuvres par supports, Durée Moyenne et Evolution par Décennie
<br>

![oeuvres_support](../images/kpi/1_analyse_oeuvres.PNG)
***Source : ImdB title.basics***
<br>

#### Analyse

1. **Types de Données :**
   - Les graphiques présentent une vue d'ensemble des œuvres cinématographiques et télévisuelles, avec une répartition entre le nombre de films et de séries.  
   - On constate une dominance des films par rapport aux séries, mais l’essor des séries TV au cours des dernières décennies se manifeste également.  
   - La base de données couvre une large gamme de genres, de pays, de périodes et de formats, ce qui reflète la richesse de l’industrie audiovisuelle.

2. **Tendances Générales :**
   - Une augmentation de la production de séries TV au détriment des films à partir des années 2000.  
   - Une variation marquée dans les genres populaires selon les périodes, les films et séries suivant des modes sociétales et technologiques.
   - Les séries TV connaissent une importante production à partir des années 2010, ce qui correspond à l'explosion des plateformes de streaming comme Netflix, Amazon Prime, et autres.

3. **Top 5 des pays producteurs :**
   - Les États-Unis, Royaume-Uni, et Inde dominent toujours la production, mais d'autres pays émergent progressivement, notamment le Japon et la France.  
   - Le cinéma français et européen se distingue par sa diversité, tout comme l’Inde avec ses productions massives et colorées.

4. **Répartition par Genres et Types :**
   - Les genres les plus populaires restent les drames, comédies, et films d’action, avec des tendances évolutives suivant les attentes des spectateurs (ex. : super-héros, science-fiction dans les années 2000).  
   - La diversité dans les genres proposés est également notable, incluant des films expérimentaux et des séries de niche qui prennent de l'ampleur sur des plateformes comme Netflix, qui investit dans des productions originales.  

#### **Insights pertinents**

1. **Pour le moteur de recherche :**  
   - **Séparation Cinéma / Séries TV :**  
     - Offrir un filtre de sélection entre films et séries, avec la possibilité d’affiner par période, genre, ou pays.  
     - Permettre une recherche croisée qui met en avant la transition cinéma-séries pour certaines franchises (par exemple, adaptation de films populaires en séries).  
   - **Filtrage par Popularité et Nombre de Votants :**  
     - Intégrer un système qui permet de filtrer les œuvres par le nombre de votes et la note moyenne, pour mettre en avant des films populaires tout en découvrant des pépites sous-évaluées.  
   - **Recommandations par Genre et Période :**  
     - Proposer des recommandations basées sur des films ou séries qui ont marqué chaque décennie ou chaque genre, afin de permettre aux utilisateurs de découvrir des classiques ou des films emblématiques.  
     - Intégrer un algorithme qui apprend les préférences de l’utilisateur pour mieux personnaliser les suggestions.

2. **Pour la programmation cinéma :**  
   - **Séries à l'écran :**  
     - Proposer des projections spéciales de séries populaires en salles, sur le modèle des « événements cinéma », comme l’ont fait certains cinémas pour des séries comme *Game of Thrones*.  
     - Créer un espace de projection de séries TV comme des films, avec des événements dédiés aux premières d’épisodes ou aux saisons entières.
   - **Cycle de Programmation Décennies :**  
     - Organiser des cycles de films par décennie, en mettant en avant les grandes œuvres des années 1920 à 2020.  
     - Cela pourrait inclure des discussions autour de l’évolution du cinéma et des séries, et comment les productions ont évolué en réponse à la technologie, à la société, et à la consommation des médias.
   - **Nouvelles Séries et Production Internationale :**  
     - Mettre en avant des séries internationales ou moins connues des États-Unis et du Royaume-Uni, en s’appuyant sur des genres émergents, des productions uniques ou des auteurs inconnus du grand public.  
     - Organiser des projections autour de séries télévisées qui ne sont pas encore largement distribuées, mais qui pourraient captiver un public averti.
   - **Saison thématique de films/séries par genre :**  
     - Proposer des programmations spéciales par genre : films policiers, science-fiction, comédies romantiques, etc. pour capter l’attention de spectateurs intéressés par des thèmes ou genres spécifiques.  
     - Mettez en lumière des genres moins connus (par exemple, films d’horreur classiques ou comédies indépendantes) pour diversifier l’offre.

En optimisant un moteur de recherche et une programmation cinéma basée sur cette analyse, un cinéma peut non seulement attirer un public plus large, mais aussi fidéliser une clientèle curieuse de découvrir de nouveaux horizons cinématographiques et télévisuels. Cela permettra de proposer une offre plus personnalisée, en phase avec les attentes variées des spectateurs actuels.
<br>

---

### Analyse des Genres au Cinéma
<br>

![genres](../images/kpi/2_analyse_genres.PNG)
***Source : ImdB title.basics***
<br>

#### **Analyse**

1. **Répartition des Genres :**
   - Les genres principaux sont le Drame, la Comédie et le Thriller, qui dominent largement la production cinématographique.  
   - Les films d’Action, Science-Fiction et Fantastique représentent une part significative, particulièrement depuis les années 2000, en lien avec l'essor des blockbusters et des avancées technologiques.  
   - Les films de Romance et les Comédies Romantiques gardent une place importante, souvent associés à un public spécifique et des périodes clés comme la Saint-Valentin.  
   - Les films d’Horreur, bien que moins dominants, conservent une base de fans fidèles, notamment lors de festivals ou d'événements comme Halloween.

2. **Évolution des Genres :**
   - Une montée en puissance des genres liés à la Science-Fiction et aux Super-héros, avec des univers partagés comme ceux de Marvel et DC.  
   - Une résurgence des documentaires et des films indépendants dans les années 2010, en partie grâce à l'influence des plateformes de streaming.  
   - Les genres comme le Western ou les films de Guerre, autrefois très populaires, tendent à diminuer mais subsistent par des œuvres marquantes ou des réinterprétations modernes.

3. **Genres de Niche :**
   - Les genres comme le Musical, bien que minoritaires, attirent un public fidèle, notamment grâce à des succès récents comme *La La Land* ou des adaptations de comédies musicales.  
   - Les films Biographiques et Historiques gagnent en popularité, souvent récompensés dans des cérémonies comme les Oscars.

#### **Insights pertinents**

1. **Pour le moteur de recherche :**
   - **Filtrage par Genre Principal :**  
     - Proposer un classement clair des œuvres par genre, avec la possibilité d’affiner selon des sous-genres (par exemple, Comédie > Comédie romantique).  
     - Intégrer des recommandations croisées entre genres similaires ou complémentaires (ex. : Thriller + Horreur ou Drame + Biographique).  
   - **Popularité par Genre :**  
     - Mettre en avant les genres populaires auprès des utilisateurs, basés sur les données d’interaction ou de visionnage récents.  
   - **Recommandations Contextuelles :**  
     - En fonction de la période de l’année, promouvoir des genres spécifiques (par exemple, des films de Noël en décembre ou des films d’horreur en octobre).  
     - Permettre la recherche par ambiance (ex. : "feel-good", "intense", "nostalgique").

2. **Pour la programmation cinéma :**
   - **Soirées Thématiques :**  
     - Organiser des soirées ou week-ends thématiques autour des genres dominants (Drame, Comédie, Thriller) en sélectionnant des films représentatifs de chaque décennie.  
     - Proposer des événements spéciaux autour de genres de niche, comme les Musicals ou les Documentaires.  
   - **Cycles Par Genre :**  
     - Créer des cycles récurrents, comme une semaine dédiée à la Science-Fiction ou un mois de l’Horreur, avec des œuvres cultes et modernes.  
   - **Mise en avant de genres émergents ou sous-représentés :**  
     - Proposer une programmation qui met en lumière des genres moins dominants comme le Western, le Musical, ou des films Historiques.  
   - **Focus sur les Sous-Genres :**  
     - Explorer des sous-genres spécifiques avec des marathons (ex. : films de Super-héros des années 2000 ou Comédies romantiques des années 90).  
   - **Collaboration avec des événements ou festivals :**  
     - Collaborer avec des festivals ou événements pour renforcer la visibilité de certains genres, comme un festival de documentaires ou une soirée dédiée aux films primés.  

En structurant une approche de filtrage par genre et en diversifiant la programmation, le cinéma peut répondre à des goûts variés tout en créant des opportunités pour attirer des spectateurs curieux ou passionnés par des types de films spécifiques. Une stratégie équilibrée entre œuvres populaires et de niche peut ainsi renforcer l'attractivité globale.
<br>

---

### Analyse des Genres dans les Séries TV
<br>

![genres](../images/kpi/2_analyse_genres_tv.PNG)
***Source : ImdB title.basics***
<br>

#### **Analyse**

1. **Répartition des Genres :**  
   - **Drame et Comédie** dominent largement le paysage des séries télévisées, ce qui témoigne de leur capacité à captiver des publics divers sur plusieurs saisons.  
   - **Thriller et Crime** occupent une place significative, souvent associés à des récits captivants et des intrigues à suspense.  
   - **Science-Fiction et Fantastique** connaissent une croissance soutenue, soutenue par des séries cultes comme *Stranger Things* ou *Game of Thrones*.  
   - Les genres comme le **Documentaire** et la **Romance**, bien que plus ciblés, ont un public fidèle et une forte présence dans les catalogues des plateformes de streaming.  

2. **Évolution des Tendances :**  
   - Les dernières décennies montrent une montée en puissance des récits complexes et des genres hybrides, mélangeant Drame et Science-Fiction ou Comédie et Romance.  
   - Les séries **d’animation** destinées aux adultes, telles que *Rick and Morty* ou *BoJack Horseman*, deviennent un genre à part entière, avec un public croissant.  
   - Les séries **documentaires** et **true crime**, popularisées par des plateformes comme Netflix, génèrent un engouement particulier grâce à des histoires intrigantes basées sur des faits réels.  

3. **Genres de Niche :**  
   - Les genres comme **Musical**, bien qu’en marge, attirent un public loyal, notamment avec des productions marquantes comme *Glee*.  
   - Les séries **Historiques/Biographiques**, souvent récompensées dans des festivals, rencontrent un succès auprès des amateurs d’histoire et de culture.  

#### **Insights pertinents**

1. **Pour le moteur de recherche :**  
   - **Filtrage par Genre :**  
     - Offrir une segmentation claire des genres avec la possibilité de rechercher des sous-genres ou des combinaisons (par exemple, "Drame + Crime" ou "Comédie + Science-Fiction").  
   - **Recommandations personnalisées :**  
     - Proposer des recommandations croisées basées sur les tendances observées (ex. : les amateurs de Drame pourraient aimer les séries hybrides avec du Fantastique).  
   - **Filtres avancés :**  
     - Ajouter des options pour explorer des genres selon la durée des épisodes, le type de format (mini-série ou série longue), ou la note critique.  

2. **Pour la programmation cinéma :**  
   - **Événements spéciaux :**  
     - Organiser des marathons ou des projections exceptionnelles pour des séries emblématiques dans des genres populaires (ex. : *Breaking Bad* pour le Crime ou *The Office* pour la Comédie).  
   - **Focus sur les adaptations :**  
     - Mettre en avant les adaptations de séries TV au cinéma ou vice versa, pour renforcer le lien entre les deux formats.  
   - **Séries documentaires ou historiques :**  
     - Proposer des projections de documentaires ou de séries basées sur des faits réels pour un public en quête de contenu éducatif.  
   - **Mise en avant des séries hybrides :**  
     - Explorer les genres émergents ou des combinaisons innovantes qui attirent un public curieux et diversifié.  
   - **Expériences immersives :**  
     - Créer des expériences interactives autour de séries cultes (ex. : reconstitutions d’univers fictifs ou événements costumés).  

L’analyse des genres dans les séries TV révèle une diversité de contenus adaptée à des audiences variées. En proposant un moteur de recherche précis et une programmation basée sur des genres phares ou de niche, le cinéma peut élargir son attractivité tout en répondant aux goûts d’un public en quête de récits engageants et captivants.
<br>

---

### Répartition des Films par Pays
<br>

![Pays](../images/kpi/7b_pays.PNG)
***Source : TmdB***
<br>

#### **Analyse**

1. **Domination des États-Unis :**  
   - Les productions américaines représentent une part écrasante des œuvres dans le cinéma et les séries TV, grâce à la puissance de Hollywood et à l’attrait international de leurs contenus.  
   - Une grande diversité de genres et de formats explique cette position dominante, accompagnée d’une forte capacité de distribution globale.  

2. **Contributions notables d'autres pays :**  
   - **Royaume-Uni :** Reconnu pour ses drames historiques et séries à la production soignée, ce pays est une source majeure de contenus de qualité.  
   - **France :** Positionnée comme un acteur majeur du cinéma mondial, avec des œuvres célébrées pour leur sophistication et leur diversité thématique.  
   - **Inde :** Bollywood et son industrie cinématographique unique apportent une identité forte, marquée par des récits épiques, des danses, et des musiques mémorables.  
   - **Canada :** En partie grâce à des coproductions nord-américaines, il offre un mélange de contenus locaux et internationaux.  
   - **Japon :** La force de l’animation et des films culturels confère au Japon une place importante, attirant un public mondial grâce à des œuvres comme *Spirited Away*.  

3. **Diversité régionale :**  
   - L’Europe, notamment par la France, l’Allemagne et l’Italie, contribue à un riche patrimoine cinématographique et des séries qualitatives, bien que plus localisées.  
   - L’Asie de l’Est, avec le Japon et la Corée du Sud, monte en puissance, notamment grâce à l’explosion des K-dramas et du cinéma d’animation.  

4. **Œuvres globales :**  
   - Certaines œuvres ou coproductions impliquent plusieurs pays, offrant une perspective internationale qui enrichit le contenu et attire un public diversifié.  

#### **Insights pertinents**

1. **Pour le moteur de recherche :**  
   - **Filtres par région et pays :**  
     - Ajouter la possibilité de chercher des œuvres par origine géographique, permettant de cibler des œuvres britanniques, françaises, indiennes, ou japonaises, selon les préférences de l’utilisateur.  
   - **Focus sur la diversité culturelle :**  
     - Proposer des recommandations basées sur des œuvres moins connues mais issues de régions émergentes.  
   - **Recherche multicritères :**  
     - Intégrer des critères croisés, comme pays d’origine et genre, pour une expérience utilisateur enrichie.  

2. **Pour la programmation cinéma :**  
   - **Soirées thématiques :**  
     - Organiser des événements autour de la production d’un pays ou d’une région spécifique (ex. : Bollywood Night, Festival des films britanniques).  
   - **Promotion des pépites internationales :**  
     - Mettre en avant des œuvres de pays moins représentés, renforçant l’attrait pour un public curieux de diversité culturelle.  
   - **Valorisation de l’Europe :**  
     - Créer une programmation dédiée au cinéma européen ou à des coproductions internationales, en misant sur la richesse artistique.  
   - **Focus sur l’Asie :**  
     - Capitaliser sur l’intérêt croissant pour les œuvres japonaises, coréennes, ou chinoises, notamment dans les genres animation, drame et fantastique.  
   - **Films historiques ou documentaires :**  
     - Proposer des films en lien avec l’histoire ou la culture des pays représentés pour des séances éducatives ou immersives.  
 
L’analyse géographique des œuvres met en lumière une forte hégémonie américaine mais aussi une diversité culturelle précieuse. En s’appuyant sur ces données, le cinéma peut enrichir son offre en alternant entre productions populaires et découvertes internationales, tout en offrant un moteur de recherche adapté aux cinéphiles en quête de nouvelles expériences culturelles.
<br>

---

### Films les mieux notés et leurs caractéristiques
<br>

### Top Films 1920 - 1949

![TOP1920_1949](../images/kpi/4_top_films_1920_1949.PNG)
***Source : ImdB - TmdB***
<br>

#### Analyse

- **Top 10 des films selon la note moyenne** :
Les films les mieux notés de cette période incluent des classiques intemporels qui ont marqué l'histoire du cinéma.
Ils sont souvent issus de réalisateurs de renom et bénéficient d'une reconnaissance critique exceptionnelle.
Les genres semblent variés (drame, film noir, comédie romantique).
La majorité des films provient des États-Unis, soulignant l'impact d'Hollywood dès ses débuts.

- **Top 10 selon le nombre de votes** :
Ces films ont une notoriété massive auprès des spectateurs, même aujourd'hui.
La popularité peut être attribuée à des rééditions, des restaurations, ou à une présence régulière dans des rétrospectives ou plateformes de streaming.
Les genres incluent des drames et des films emblématiques souvent étudiés dans les écoles de cinéma.
Là encore, une forte représentation des films américains est notable.

#### Insights pertinents

- **Pour le moteur de recherche** :

Intégrer un filtre spécifique pour les films classiques (années 1920-1949), afin de valoriser cette période.
Inclure des classements selon les deux métriques principales (note et votes), permettant aux spectateurs de choisir entre qualité critique et popularité.
Proposer une catégorie dédiée pour les réalisateurs emblématiques de cette période (Hitchcock, Chaplin, etc.).

- **Pour la programmation cinéma** :

Focus sur les films les mieux notés : Ces œuvres attireraient un public de cinéphiles cherchant à découvrir ou redécouvrir des classiques peu accessibles en salle.
Mise en avant des films les plus votés : Ils garantissent une forte attractivité, notamment grâce à leur popularité persistante et leur impact culturel.
Organiser des cycles thématiques : Proposer des rétrospectives par réalisateur ou par genre dominant (ex. : film noir, comédie romantique, drame).
Prévoir des projections restaurées ou accompagnées de présentations pour enrichir l’expérience et l’intérêt historique.
<br>

---

### Top Films 1950-1979

![TOP1950_1979](../images/kpi/4_top_films_1950_1979.PNG)
***Source : ImdB - TmdB***
<br>

#### Analyse

1. **Top 10 des films selon la note moyenne :**  
   - Les films de cette période incluent des chefs-d’œuvre incontournables qui ont façonné le cinéma moderne.  
   - Les genres dominants sont variés : drame, science-fiction, thriller et comédie.  
   - Les réalisateurs comme Stanley Kubrick, Akira Kurosawa ou Sergio Leone sont fortement représentés, soulignant leur importance artistique.  
   - Hollywood reste dominant, mais l'influence internationale se fait plus marquée (notamment le Japon et l'Europe).  

2. **Top 10 selon le nombre de votes :**  
   - Ces films, largement populaires, ont un impact culturel énorme qui perdure encore aujourd’hui.  
   - On observe une surreprésentation des blockbusters et des œuvres cultes (notamment des films de science-fiction ou de fantasy).  
   - Les sagas et franchises emblématiques commencent à émerger dans cette période (ex. : *Star Wars*).  

#### **Insights pertinents**  

1. **Pour le moteur de recherche :**  
   - Ajouter une section pour les œuvres de 1950 à 1979, avec la possibilité de filtrer par *note* ou *nombre de votes*.  
   - Proposer des recommandations par réalisateurs emblématiques de cette période (Kubrick, Kurosawa, Leone, Fellini).  
   - Inclure un filtre pour les œuvres ayant marqué des genres spécifiques (sci-fi, western spaghetti, drame psychologique).  

2. **Pour la programmation cinéma :**  
   - **Focus sur les films les mieux notés :** Organiser des soirées « chefs-d’œuvre », ciblant les cinéphiles à la recherche de films reconnus pour leur qualité artistique.  
   - **Films les plus votés :** Mettre en avant des blockbusters cultes pour attirer un public plus large, nostalgique des classiques populaires.  
   - **Cycles par genres et réalisateurs :** Par exemple :  
     - Cycle *Stanley Kubrick* avec des projections comme *2001, l’Odyssée de l’Espace* ou *Orange Mécanique*.  
     - Cycle *westerns spaghetti* avec les œuvres de Sergio Leone (*Le Bon, la Brute et le Truand*).  
   - **Événements interactifs :** Ajouter des débats ou des analyses post-projection pour renforcer l’expérience culturelle.  

Cette période, riche en innovations et en classiques incontournables, est idéale pour séduire à la fois un public cinéphile et des amateurs de blockbusters. Le moteur de recherche et la programmation cinéma peuvent ainsi valoriser la diversité et l’impact des films de cette époque.
<br>

---

### Top Films 1980-1999

![TOP1980_1999](../images/kpi/4_top_films_1980_1999.PNG)
***Source : ImdB - TmdB***
<br>

#### Analyse

1. **Top 10 des films selon la note moyenne :**  
   - Cette période est marquée par des œuvres devenues des références culturelles, notamment dans les genres du drame, du thriller psychologique et de la science-fiction.  
   - Les films de cette liste, comme *The Shawshank Redemption* (*Les Évadés*), *Pulp Fiction* ou *Schindler's List*, témoignent d'une période où le storytelling puissant et la profondeur émotionnelle sont au premier plan.  
   - Les réalisateurs de renom comme Steven Spielberg, Quentin Tarantino et David Fincher dominent avec des chefs-d'œuvre intemporels.  
   - Les films internationaux gagnent également en reconnaissance, notamment à travers des productions plus accessibles pour un public mondial.

2. **Top 10 selon le nombre de votes :**  
   - Les films les plus votés de cette période incluent des blockbusters emblématiques tels que *The Matrix*, *The Lord of the Rings* (précurseur avec *The Fellowship of the Ring*) et des films de science-fiction comme *Terminator 2*.  
   - Le cinéma d'action et les franchises dominent le classement, reflétant une explosion des films orientés grand public et le début de l'ère des superproductions à gros budget.  
   - Ces films continuent de bénéficier de vastes communautés de fans, notamment grâce à Internet et aux plateformes comme IMDb. 

#### **Insights pertinents**

1. **Pour le moteur de recherche :**  
   - Ajouter une option spécifique pour explorer les films des années 1980-1999, avec des filtres par *note moyenne* et *popularité* (nombre de votes).  
   - Inclure des catégories par réalisateurs marquants (Tarantino, Spielberg, James Cameron, les Wachowski) pour permettre un ciblage des recherches par affinité cinématographique.  
   - Mettre en avant les sagas et franchises majeures de cette période, notamment pour attirer les fans nostalgiques de ces œuvres.  

2. **Pour la programmation cinéma :**  
   - **Soirées Blockbusters des années 80-90 :** Créer un événement dédié aux superproductions cultes (*Terminator 2*, *Jurassic Park*, *The Matrix*), pour raviver l'intérêt des fans de science-fiction et d'action.  
   - **Hommage aux drames intemporels :** Diffuser des œuvres comme *Les Évadés* ou *Schindler's List* dans un cadre cinéphile avec des analyses ou des débats après projection.  
   - **Cycles thématiques par réalisateur :**  
     - Un cycle Spielberg pour découvrir sa contribution au cinéma (action, drame, aventure).  
     - Un cycle Tarantino avec des films comme *Pulp Fiction* et *Reservoir Dogs*.  
   - **Événements intergénérationnels :** Mettre en avant des films familiaux iconiques de cette période (*E.T.*, *The Lion King*) pour réunir un public de tout âge.  

Cette période, riche en superproductions et en récits emblématiques, est parfaite pour satisfaire une audience diversifiée : des fans de blockbusters, des cinéphiles à la recherche de récits profonds, et des nostalgiques des classiques des années 80-90. Le moteur de recherche et la programmation peuvent ainsi s'adapter aux attentes variées de ce public.
<br>

---

### Top Films 2000-2024

![TOP2000_2024](../images/kpi/4_top_films_2000_2024.PNG)
***Source : ImdB - TmdB***
<br>

#### Analyse

1. **Top 10 des films selon la note moyenne :**  
   - Cette période est dominée par des films alliant puissance narrative et excellence technique, comme *The Dark Knight*, *The Lord of the Rings: The Return of the King*, et *Inception*.  
   - Les genres variés, incluant la fantasy, la science-fiction, et les thrillers psychologiques, séduisent à la fois les critiques et le grand public.  
   - Le cinéma international s’impose également : *Parasite*, une production sud-coréenne, a marqué l’histoire en remportant de multiples distinctions, dont l’Oscar du meilleur film en 2020.  
   - Des réalisateurs visionnaires comme Christopher Nolan, Peter Jackson, et Bong Joon-ho sont omniprésents dans ce classement.

2. **Top 10 selon le nombre de votes :**  
   - Les films les plus votés comprennent des œuvres emblématiques comme *Avengers: Endgame*, *Avatar*, et *The Dark Knight*, illustrant l’hégémonie des franchises Marvel et DC dans le paysage cinématographique.  
   - Cette période reflète l’essor des blockbusters grand public et l’industrialisation des univers cinématographiques partagés (notamment le MCU).  
   - Les films basés sur des sagas populaires (*Harry Potter*, *The Lord of the Rings*, *Star Wars*) continuent de captiver les foules.  
   - La popularité des plateformes de notation en ligne amplifie l’impact des fandoms sur les tendances.  

#### **Insights pertinents**

1. **Pour le moteur de recherche :**  
   - Ajouter un filtre par période spécifique (2000-2024) et par franchise majeure (Marvel, DC, *Harry Potter*, etc.).  
   - Permettre de trier les films par note moyenne et nombre de votes, pour répondre à la fois aux attentes des cinéphiles et des amateurs de blockbusters.  
   - Intégrer des catégories comme :  
     - Films oscarisés (*Parasite*, *The Return of the King*).  
     - Films de réalisateurs renommés (Nolan, Villeneuve, Bong Joon-ho).  
     - Films de science-fiction et fantasy incontournables.  

2. **Pour la programmation cinéma :**  
   - **Marathons Franchises :** Proposer des marathons autour des sagas cultes comme *The Lord of the Rings*, *Harry Potter*, ou l’univers Marvel, pour fidéliser un public jeune et intergénérationnel.  
   - **Cycles Réalisateurs Visionnaires :** Dédiés à des figures majeures comme Christopher Nolan, Denis Villeneuve, ou Peter Jackson, avec des projections accompagnées de discussions thématiques.  
   - **Projections Événements :**  
     - Diffusion de films oscarisés suivie de débats ou de conférences (*Parasite*, *Slumdog Millionaire*).  
     - Hommage aux blockbusters marquants (*Avatar*, *Avengers: Endgame*), couplé à des expériences immersives (3D, IMAX).  
   - **Focus sur le cinéma international :** Proposer des séances axées sur les productions non-anglophones récompensées (*Parasite*, *Amélie*).  

Cette période illustre un équilibre entre la force des blockbusters et des sagas cinématographiques et l’émergence d’œuvres originales et audacieuses. Une stratégie mixte permettrait d’attirer une audience variée, de la génération Marvel aux amateurs de films primés et à fort impact artistique.
<br>

---

### Top Films (Votes < 100000)

![TOPvotes_100000](../images/kpi/4_top_films_votes_100000.PNG)
***Source : ImdB - TmdB***
<br>

#### Analyse

1. **Films Classiques avec Notes Élevées :**  
   - Ces films sont souvent des œuvres méconnues du grand public mais très appréciées par une niche cinéphile.  
   - Les genres représentés varient entre drames, films historiques, documentaires, et films d’auteur.  
   - Le soin apporté à la narration, à la photographie, et aux thématiques universelles est un point commun.  
   - Certaines œuvres proviennent de cinémas moins médiatisés (cinéma scandinave, Asie centrale, cinéma indépendant américain).

2. **Profil des Films :**  
   - La période s'étend sur plusieurs décennies, allant de chefs-d’œuvre classiques à des productions modernes peu exposées médiatiquement.  
   - Les notes élevées témoignent d’une qualité cinématographique exceptionnelle, mais l’audience limitée pourrait s’expliquer par une distribution restreinte ou un marketing faible.  

3. **Niches Culturelles :**  
   - Films reflétant des cultures ou des périodes historiques spécifiques.  
   - Certains films indépendants abordent des thématiques atypiques ou controversées, attirant un public averti.  

#### **Insights pertinents**

1. **Pour le moteur de recherche :**  
   - Mettre en avant une catégorie "Pépites méconnues" avec des films ayant :  
     - Une note > 8/10.  
     - Moins de 100 000 votes.  
   - Ajouter des filtres basés sur :  
     - Le genre cinématographique (drame, documentaire, film historique).  
     - L'origine géographique pour révéler les richesses du cinéma international.  
   - Proposer une recommandation personnalisée pour les cinéphiles curieux.  

2. **Pour la programmation cinéma :**  
   - **Cycle "Trésors Cachés" :** Une série de projections dédiées aux films moins connus mais extrêmement bien notés.  
     - Inclure des introductions ou des discussions avec des critiques ou des cinéastes.  
   - **Ciné-club de niche :**  
     - Inviter des spectateurs à découvrir ces œuvres dans un cadre intimiste.  
     - Organiser des séances thématiques (cinéma d’auteur, exploration de régions cinématographiques peu connues).  
   - **Exploration culturelle :**  
     - Diffuser des films peu votés issus de cinémas spécifiques (scandinave, africain, asiatique).  
     - Mettre en avant le contexte historique ou culturel lors de ces séances.  
   - **Festival des découvertes :** Un mini-festival annuel consacré à ces pépites avec votes des spectateurs pour leur film préféré.  


En valorisant ces films au sein d’un moteur de recherche ou d’une programmation, un cinéma peut offrir une expérience enrichissante et différenciante, attirant une audience curieuse et passionnée par des œuvres de qualité souvent laissées de côté. Cela renforcerait l’image d’un cinéma axé sur la découverte et l’excellence.
<br>

---

### Top Films France (Production Française)

![TOPfilms_france](../images/kpi/4_top_films_france.PNG)
***Source : ImdB - TmdB***
<br>

**Attention !** : Certains films ci dessus sont en partie production française, en partie d'autres pays.

####


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



Pourquoi un cinéma devrait intégrer des séries TV dans sa programmation ou son moteur de recherche ?
Opportunités commerciales :

    Attirer de nouveaux publics :
        Les séries TV ont gagné en popularité ces dernières années, notamment grâce aux plateformes de streaming. Intégrer des séries permettrait d’attirer des spectateurs qui recherchent des formats narratifs longs et immersifs.
        Proposer des marathons ou des projections d’épisodes spéciaux de séries cultes (Drame, Action, ou Comédie) peut séduire un public jeune et les fans de franchises.

    Diversifier l’offre de contenu :
        Les Documentaires et les Animations pourraient être utilisés pour organiser des événements thématiques (éducation, culture pop, etc.).
        Les genres comme Action ou Science-fiction, bien qu’en minorité, sont des atouts pour des projections à thème ou des collaborations avec des festivals.

    Créer de l’engagement :
        Organiser des avant-premières de séries très attendues ou des projections d’épisodes de fin de saison peut fidéliser le public.
        Les projections spéciales permettent de créer une expérience communautaire autour des séries (fans clubs, cosplay, débats).

Avantages d’un moteur de recherche incluant les séries TV :

    Meilleure personnalisation : Enrichir un moteur de recherche avec des séries permettrait de répondre aux goûts variés des spectateurs. Par exemple :
        Recommander des séries Comédie ou Drame pour les amateurs de récits légers ou intenses.
        Proposer des Documentaires ou des séries Historiques pour des publics cherchant un contenu éducatif ou culturel.

    Cross-content : Créer des ponts entre séries et films basés sur des genres communs ou des acteurs partagés.
        Exemple : Un spectateur ayant apprécié un film dramatique pourrait être tenté par une série TV similaire.
