⬅️[Retour à l'accueil](../../README.md)

# Méthodologie de l'interface Streamlit

<br>
<p align="center">
  <img src="../images/logo_streamlit.png" alt="Logo Streamlit" width="300">
</p>
<br>

## 1. Introduction

L'application "Le 23ème Écran" est une plateforme interactive Streamlit permettant :

* D'explorer un catalogue de films.
* D'obtenir des recommandations personnalisées basées sur un moteur de Machine Learning.
* D'enrichir l'expérience utilisateur grâce à des informations détaillées sur les films.

Le code repose sur plusieurs modules Python, notamment :

* **Streamlit** pour l'interface utilisateur.
* **Pandas** pour la manipulation de données.
* **Scikit-learn** et**RapidFuzz** pour les recommandations et la recherche.

---

## 2. Architecture globale

### 2.1. Configuration de l'application

La méthode `st.set_page_config()` personnalise la configuration globale de la page :

- `page_title`: Définit le titre de l'onglet du navigateur.

* `layout`: Adopte une disposition large pour maximiser l'espace disponible.

```python
st.set_page_config(
    page_title="Cinéma le 23ème Écran",
    layout="wide")

```

### 2.2. Chargement des données

Les données nécessaires à l'application sont organisés en début de script et chaque ressource : csv, jpeg, etc... est stockée dans une variable dédiée. L'utilisation des données externes et le maintient du script et de l'application sont ainsi facilités.

Deux fichiers principaux sont chargés :

* `df_info.csv.gz` contient des informations générales sur les films.
* `DF_ML.csv.gz` est utilisé pour les modèles de Machine Learning.

Le chargement est optimisé avec `@st.cache_data`** : Cette annotation met en cache les données, accélérant les chargements tout en réduisant la charge sur les ressources système. **Avantage** : Le cache améliore les performances en évitant de recharger les données à chaque exécution.

```python
@st.cache_data
def load_movie_infos():
    df = pd.read_csv(df_infos_csv)
    return df
```

### 2.3. Gestion du style avec CSS

Un fichier CSS externe est utilisé pour styliser l'interface et améliorer l'expérience utilisateur.

```python
with open(file_name) as f:
st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
```

- **Chemins relatifs** : Le fichier`style.css` doit se trouver dans le même répertoire que le script.

* **Gestion des erreurs** : Si le fichier CSS est introuvable, une erreur est affichée avec`st.error()`.


## 3. Fonctionnalités principales

### 3.1 **Navigation dans l'application**

Le menu de navigation est implémenté dans la fonction `afficher_menu()` et affiché avec des colonnes pour structurer l'interface :

* **Concept** : Chaque bouton de menu met à jour la variable`st.session_state["menu_choice"]`.
* **Résultat** : L'application affiche dynamiquement la section correspondante.

```python
def afficher_menu():
    col1, col2 = st.columns([1, 4])
    with col1:
        st.image(logo, use_container_width=True)
    with col2:
        options = ["Accueil", "À propos", "Actualités"]
        cols = st.columns(len(options))
        for i, option in enumerate(options):
            if cols[i].button(option, key=f"bouton_{option}"):
                st.session_state["menu_choice"] = option
```

### 3.2 **Recherche de films**

La recherche s'effectue via la fonction `search()` qui utilise RapidFuzz pour comparer des chaînes :

```python
results = process.extract(query_lower, choices_lower, limit=10, scorer=fuzz.WRatio, score_cutoff=90)
filtered_results = [choices[choices_lower.index(result[0])] for result in results if result[1] >= 50]
```

- **Principe** : La bibliothèque RapidFuzz évalue la similarité textuelle pour identifier les films les plus proches du titre recherché.


### 3.3 **Recommandations basées sur le Machine Learning**

La fonction `recommandation()` combine plusieurs étapes pour générer des recommandations :

1. **Préparation des données** :

   * Les colonnes numériques sont normalisées avec`MinMaxScaler`.
   * Les données catégorielles et numériques sont concaténées.
2. **Modèle de recommandation** :

* `NearestNeighbors` de Scikit-learn est utilisé pour trouver les films similaires en fonction des caractéristiques.
* Les genres et pays du film sélectionné sont utilisés comme filtres.

3. **Affichage des résultats** :

Deux ensembles de recommandations sont générés :

* Films avec des genres et pays similaires.
* Films avec des genres similaires mais des pays différents.

### 3.4 **Affichage interactif**

Les résultats sont affichés sous forme de grilles avec des colonnes dynamiques :

```python
for row_index, row_df in enumerate(rows):
    cols = st.columns(num_cols)
    for col_index, row in enumerate(row_df.iloc):
        with cols[col_index]:
            st.image(f"https://image.tmdb.org/t/p/w500{row['Chemin Affiche']}", width=150)
```

Chaque film est accompagné de détails comme :

* Le titre.
* La note sur 10.
* Le test de Bechdel.



## 4. **Pages spécifiques**

#### 4.1. Page d'accueil avec barre de recherche

L'accueil est conçu pour introduire l'utilisateur à l'application.

La fonction `afficher_accueil()` gère la recherche et les suggestions de films en déclenchant les fonction `search()` et `recommandation()` selon les entrées utilisateur.

```python
search_query = st.text_input("Pour recevoir des suggestions personnalisées :", ...)
results = search(search_query, df_infos['Titre'].tolist())
```

* L'utilisateur saisit un titre dans une barre de recherche.
* La fonction`search()` utilise**RapidFuzz** pour effectuer une correspondance floue :

```python
results = process.extract(query, choices, limit=limit, scorer=fuzz.WRatio, score_cutoff=80)
```

- **Affichage des résultats** :*
  - Les films correspondant à la recherche sont proposés via un menu déroulant (`st.selectbox`).
  - Une fois un film sélectionné, ses détails (titre, durée, genres, affiche, note) s’affichent.

### 4.2. Pages "À propos" et "Actualités"

Les sections "À propos" et "Actualités" offrent des informations supplémentaires sur le cinéma. Elles sont affichées de manière simple, leur contenu pourra être enrichi dans le temps.

```python
def afficher_a_propos():
    st.title("À propos")
    st.markdown("<p>Le 23ème Écran, votre cinéma creusois et innovant.</p>", unsafe_allow_html=True)
```

## 4. Gestion des états et navigation

### 4.1. État de session

Le site exploite les variables de session pour suivre les interactions utilisateur :

* **Menu actif** :`st.session_state["menu_choice"]` mémorise la page actuelle.

### 4.2. Navigation conditionnelle

L'affichage des pages repose sur la valeur de `menu_choice` :

```python
menu_choice = st.session_state.get("menu_choice", "Accueil")
if menu_choice == "Accueil":
    afficher_accueil(st.session_state["search_query"])
elif menu_choice == "A_propos":
    afficher_a_propos()
elif menu_choice == "Actualites":
    afficher_actualites()

```


## Synthèse

L'application "Le 23ème Écran" a été construite en suivant les étapes suivantes :

1. **Chargement des données** : Utilisation de pandas pour charger les données de films et les préparer pour l'affichage et la recommandation.
2. **Interface utilisateur** : Création d'une interface Streamlit conviviale avec un menu de navigation et des champs de recherche.
3. **Modèle de recommandation** : Implémentation d'un modèle d'apprentissage automatique pour recommander des films similaires en utilisant l'algorithme créé précédemment.
4. **Affichage dynamique** : Dynamisation du contenu en fonction des actions de l'utilisateur, avec un affichage d'informations détaillées sur les films sélectionnés.
5. **Personnalisation** : Application d'un style CSS pour rendre l'interface esthétique et agréable à utiliser.

---

## Lancement de l'Application

Vous pouvez accéder à l'application en ligne via Streamlit Cloud à l'adresse suivante :
[https://movie-recommendation-project-wcs-bleu-sauvage.streamlit.app/](https://movie-recommendation-project-wcs-bleu-sauvage.streamlit.app/)


## Améliorations à apporter

### Modulariser les fonctions :

* Diviser le code en modules distincts (chargement des données, logique de recommandation, affichage).
* Regrouper les fonctions similaires dans des classes ou des fichiers séparés (e.g., un fichier pour les données, un autre pour l'interface).

### UI/UX :

- Uniformiser les styles CSS en externalisant les classes dans un fichier CSS bien structuré.

* Améliorer les messages d'erreur ou d'information pour guider l'utilisateur.
* Adapter l'affichage des colonnes pour une meilleure expérience sur mobile (p. ex., passez à 2-3 colonnes si l'écran est étroit).

### Accessibilité et SEO pour Streamlit Cloud :

- Ajouter des descriptions alt et des balises `<meta>` pour rendre l'application plus accessible.

### Ajout d'un espace utilisateur avec connexion :

L'ajout d'un espace privé pour les utilisateurs permettrait de proposer un service plus personnalisé :

- Gestion des abonnements aux listes de diffusions du cinéma : newsletter, programmation à venir, thématiques spécifiques,
- Gestion des données personnelles : nom, prénom, âge, adresse postale, meilleure connaissance du public, notamment géographique et âge,
- Notation des films et historiques des favoris, pour enrichir la connaissance du public local du cinéma,

---

⬅️[Retour à l'accueil](../../README.md)
