# Script pour l'application Streamlit "Le 23ème Écran".

# ------- INFOS POUR LANCER LE STREAMLIT -------

# Commande pour lancer : streamlit run .\streamlit\streamlite.py
# Afficher le site web hébergé sur Git Hub / Streamlit Cloud : https://movie-recommendation-project-wcs-bleu-sauvage.streamlit.app/



# ------- Import des bibliothèques nécessaires -------

import streamlit as st
import streamlit_authenticator as stauth
import pandas as pd
from streamlit_option_menu import option_menu
# from fuzzywuzzy import process
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import time
import os # lire la feuille de style (chemin absolu)
from rapidfuzz import process, fuzz



# ------- CHEMINS FICHIERS DONNEES -------

logo = "streamlit/logo.png"

style_css = "streamlit/style.css"

df_infos_csv = "donnees/data/df_info.csv.gz"    

df_ml_csv = "machine learning\DF_ML.csv.gz"


# ------- Thème -------

[theme]
primaryColor="#FF4B4B"
backgroundColor="#333"
secondaryBackgroundColor="#F0F2F6"
textColor="#ffffff"
font="sans serif"


# ------- Configuration globale -------


st.set_page_config(
    page_title="Cinéma le 23ème Écran",
    layout="wide")
st.image(logo)



# ------- CHARGEMENT DES DONNEES -------

@st.cache_data
def load_movie_infos():
    df = pd.read_csv(df_infos_csv)
    return df

df_infos = load_movie_infos() 

   

# ------ Fonction de récupération du style CSS ------

def load_css(file_name):
    # Utiliser un chemin relatif basé sur la racine
    file_path = file_name  # Avec style.css dans le même dossier que le script.py
    try:
        with open(file_path) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    except FileNotFoundError:
        st.error("Erreur : Le fichier CSS n'a pas été trouvé. Vérifiez le chemin.")


load_css(style_css)



# ------- Fonctions de navigation -------

# Fonction pour afficher le menu
def afficher_menu():
    return option_menu(
        menu_title=None,
        options=["Accueil", "À propos", "Actualités", "Programmation"],
        menu_icon="cast",  # Icône du menu principal
        default_index=0,  # Option par défaut
        orientation="horizontal"
    )

# Pages spécifiques
def afficher_accueil(search_query=""):
    if search_query:
        results = search(search_query, df_infos['Titre'].tolist())
        if results:
            selected_title = st.selectbox("Sélectionnez un des noms de films les plus proches :", results)
            st.write(f"Vous avez sélectionné : {selected_title}")
            recommandation(df_infos[df_infos['Titre'] == selected_title]['tconst'].values[0])  # Passer uniquement le tconst
        else:
            st.write("Aucun résultat trouvé.")
    else:
        st.write("Commencez à taper pour voir les suggestions.")

def afficher_a_propos():
    st.title("À propos")
    st.write("**Le 23ème Écran**, votre cinéma creusois et innovant.")
    # Ajouter d'autres contenus...

def afficher_actualites():
    st.title("Actualités")
    st.write("**Le 23ème Écran**, les actualités de votre cinéma à Guéret.")
    # Ajouter d'autres contenus...

def afficher_programmation():
    st.title("Programmation")
    st.write("**Le 23ème Écran**, voici les films que nous vous proposons.")
    # Ajouter d'autres contenus...



# ------- Fonction de recherche -------

# Fonction de correspondances des noms de films par rapport à l'entrée utilisateur barre de recherches
def search(query, choices, limit=10, threshold=50):
    results = process.extract(query, choices, limit = limit, scorer=fuzz.WRatio, score_cutoff=80)
    filtered_results = [result[0] for result in results if result[1] >= threshold]
    return filtered_results



# Fonction de similarité avec un modèle de ML
def recommandation(tconst):
    import pandas as pd
    from sklearn.neighbors import NearestNeighbors

    import warnings
    warnings.filterwarnings("ignore", category=UserWarning)
    warnings.filterwarnings("ignore", category=FutureWarning)

    df_test = pd.read_csv("machine learning/DF_ML.csv.gz")

    # ----------------------------------------------------------
    # Préparation des données
    # ----------------------------------------------------------

    index = df_test.index
    df_test_num = df_test.select_dtypes('number')
    df_test_cat = df_test.select_dtypes(['object', 'category', 'string', 'bool'])

    # Normalisation des colonnes numériques
    from sklearn.preprocessing import MinMaxScaler
    SN = MinMaxScaler()
    df_test_num_SN = pd.DataFrame(SN.fit_transform(df_test_num), columns=df_test_num.columns, index=index)

    # Encodage uniquement de la colonne 'nconst'
    df_test_cat_encoded = df_test_cat.copy()
    from sklearn.preprocessing import LabelEncoder
    le = LabelEncoder()
    df_test_cat_encoded['nconst'] = le.fit_transform(df_test_cat_encoded['nconst'].fillna('inconnu'))

    # On assemble le df numérique et le df texte
    df_test_encoded = pd.concat([df_test_num_SN, df_test_cat_encoded], axis=1)

    #On sépare notre df en deux groupes, en fonction de la note
    bons_films = df_test_encoded[df_test_encoded['notes'] >= 0.7]

    # ----------------------------------------------------------
    # KNN sur les caractéristiques numériques
    # ----------------------------------------------------------

    colonnes_a_exclure = ['tconst', 'title', 'tmdb_popularity', 'title_ratings_numVotes', 'imdb_id', 'genres', 'overview', 'overview_lem']
    caracteristiques = df_test_encoded.columns.drop(colonnes_a_exclure, errors='ignore')

    model = NearestNeighbors(n_neighbors=1000, metric='euclidean') # Il faudra tester d'autres combinaisons
    model.fit(bons_films[caracteristiques])

    caract_film = df_test_encoded[df_test_encoded['tconst'] == tconst][caracteristiques]
    distances, indices = model.kneighbors(caract_film)

    if not df_test_encoded[(df_test_encoded['tconst'] == tconst) & (df_test_encoded['notes'] >= 0.7)].empty:
        selection = bons_films.iloc[indices[0]].copy()
        selection['distance_knn'] = distances[0]
    else:
        selection = bons_films.iloc[indices[0]].copy()
        selection = pd.concat([df_test_encoded[df_test_encoded['tconst'] == tconst], selection.iloc[:-1]], axis=0)
        selection['distance_knn'] = distances[0]

    # ----------------------------------------------------------
    # TF-IDF avec lemmatisation
    # ----------------------------------------------------------

    colonnes_poids = {
        'genres': 1,
        'overview_lem': 1,
        'nconst': 1
    }

    # On crée une colonne 'texte' qui combine les valeurs pondérées des colonnes spécifiées
    selection['texte'] = selection.apply(lambda row: 
        ' '.join([
            (str(row[col]) + ' ') * colonnes_poids.get(col, 1)  # Répète la valeur de la colonne selon son poids
            for col in colonnes_poids.keys()
        ]),
        axis=1
    )

    from sklearn.feature_extraction.text import TfidfVectorizer
    vectorizer = TfidfVectorizer(stop_words='english', max_df=0.8)
    tfidf_matrix = vectorizer.fit_transform(selection['texte'])

    model_tfidf = NearestNeighbors(n_neighbors=1000, metric='cosine')
    model_tfidf.fit(tfidf_matrix)

    distances_tfidf, indices_tfidf = model_tfidf.kneighbors(tfidf_matrix[0])
    selection['distance_tfidf'] = distances_tfidf[0]

    # ----------------------------------------------------------
    # Moyenne pondérée des distances
    # ----------------------------------------------------------

    poids_knn = 1
    poids_tfidf = 100

    selection['distance_ponderee'] = (
        poids_knn * selection['distance_knn']) + (poids_tfidf * selection['distance_tfidf']
    ) 

    # Tri final par la distance pondérée
    selection = selection.sort_values(by='distance_ponderee')

    # ----------------------------------------------------------
    # Résultat final
    # ----------------------------------------------------------
    selection_finale = pd.DataFrame(selection['tconst'][1:11]).reset_index(drop=True)

    return afficher_resultats_similarite(selection_finale)



# Fonction d'affichage des résultats de recherche de similarité (ML):
def afficher_resultats_similarite(df_resultats_similarite): 
    # Recherche des informations dans DF_Infos pour les tconst du df_ML
    df_display = df_infos[df_infos['tconst'].isin(df_resultats_similarite['tconst'])]

    # Gestion dynamique du nombre de colonnes
    num_cols = len(df_display)
    cols = st.columns(num_cols)

    
    # Remplir chaque colonne avec les infos d'un film
    for col, (_, row) in zip(cols, df_display.iterrows()):
        with col:
            # Gestion des affiches
            if pd.notna(row["Chemin Affiche"]) and row["Chemin Affiche"]:
                image_lien = f'''
                <a href="javascript:void(0)" 
                onclick="window.parent.sessionStorage.setItem('selected_movie', '{row["Titre"]}'); window.parent.location.reload(true);">
                <img src="https://image.tmdb.org/t/p/w500{row['Chemin Affiche']}" width="300">
                </a>'''
            else:
                # Création d'un bloc noir avec le nom du film
                image_lien = f'''
                <a href="javascript:void(0)" 
                onclick="window.parent.sessionStorage.setItem('selected_movie', '{row["Titre"]}'); window.parent.location.reload(true);"
                style="display: block; width: 300px; height: 400px; background-color: black; color: white; 
                display: flex; justify-content: center; align-items: center; text-align: center; 
                text-decoration: none; font-size: 1.2em;">
                {row["Titre"]}
                </a>'''

            # Afficher le bloc (image ou texte)
            st.markdown(image_lien, unsafe_allow_html=True)

            # Crée un lien cliquable sur le titre avec du style
            titre_lien = f'''
            <a href="javascript:void(0)" 
            onclick="window.parent.sessionStorage.setItem('selected_movie', '{row["Titre"]}'); window.parent.location.reload(true);" 
            style="font-size: 1.5em; color: white; text-decoration: none; font-weight: bold;">
            {row["Titre"]}
            </a>'''
            st.markdown(titre_lien, unsafe_allow_html=True)


            # Calcul des étoiles
            étoile_j = round(row['Note'] / 2)  # Nombre d'étoiles jaunes (note/5)
            étoile_n = 5 - étoile_j  # Nombre d'étoiles vides pour compléter
            étoiles = "⭐" * étoile_j + "⚫" * étoile_n  # Étoiles jaunes + vides

            # Affichage des autres informations avec moins d'espace
            st.markdown(f"<p style='margin: 0;'>{row['Année de Sortie']} - {row['Durée (min)']} min.</p>", unsafe_allow_html=True)
            st.markdown(f"<p style='margin: 0;'>{round(row['Note'], 1)} / 10  - {étoiles}</p>", unsafe_allow_html=True)
            st.markdown(f"<p style='margin: 0;'>{row['genres']}</p>", unsafe_allow_html=True)


    
# Fonction pour afficher les détails du film sélectionné A FINIR ET RELIER AU RESTE NE FONCTIONNE PAS POUR LINSTANT
def afficher_details_film():
    movie_title = st.session_state['selected_movie']
    # Recherche du film dans la base de données
    movie_data = df_infos[df_infos['Titre'] == movie_title]

    # Affichage des informations détaillées du film
    st.title(movie_data['Titre'])
    image_url = f"https://image.tmdb.org/t/p/w500{movie_data['Chemin Affiche']}"
    if movie_data['Chemin Affiche'].isna()== False:
        st.image(image_url, width=300)
    else:
        st.write("Aucune affiche disponible.")

    st.markdown(f"**Année de sortie :** {movie_data['Année de Sortie']}")
    st.markdown(f"**Durée :** {movie_data['Durée (min)']} min")
    st.markdown(f"**Genres :** {movie_data['genres']}")
    st.markdown(f"**Note :** {round(movie_data['Note'], 2)}/10")

    # Bouton pour revenir à la liste des films
    if st.button("Retour à la liste des films"):
        del st.session_state['selected_movie']
        st.rerun()



# ------- Interface Utilisateur (UI) -------
if __name__ == "__main__":
    # Afficher le menu principal
    page = afficher_menu()

    # Gestion de l'état de session
    if "search_query" not in st.session_state:
        st.session_state["search_query"] = ""
    if page != st.session_state.get("current_page", ""):
        st.session_state["search_query"] = ""
        st.session_state["current_page"] = page

    # Logique pour chaque page
    if page == "Accueil":
        st.title("Votre cinéma local et innovant vous accueille")  # Titre spécifique
        search_query = st.text_input(
            "Recherchez un titre de film :", 
            placeholder="Tapez un titre de film...",
            key="search_query"
        )
        if 'selected_movie' in st.session_state:
            afficher_details_film()
        else:
            afficher_accueil(search_query)

    elif page == "À propos":
        afficher_a_propos()

    elif page == "Actualités":
        afficher_actualites()

    elif page == "Programmation":
        afficher_programmation()



# elif page == "Connexion":   
    # st.write("**Le 23ème Écran**, accédez à votre espace privé avec plus de fonctionnalités")

    # authenticator.login() # afficher le formulaire de connexion et vérifier les informations d'identification de l'utilisateur


    # Gérer l'accès en fonction des informations renseignées

    # def accueil():
    #     st.title("Bienvenu sur le contenu réservé aux utilisateurs connectés")

    # if st.session_state["authentication_status"]:
    #     accueil()
        # Le bouton de déconnexion
    #     authenticator.logout("Déconnexion")

# elif st.session_state["authentication_status"] is False:
#     st.error("L'username ou le password est/sont incorrect")
# elif st.session_state["authentication_status"] is None:
#    st.warning('Les champs username et mot de passe doivent être remplie')

# Page les pages vitrines : actualités, programmation, à propos (optionnel)


# Page == "Film", n'apparait pas dans le menu, comment la définie-t-on ?



# Formulaire d'inscription qui alimente :

# Base de gestion des données personnelles utilisateurs (en option avec la connexion)
# - ID
# - Prénom
# - Nom
# - Email
# - Date de naissance
# - Adresse postale
# - CP
# - Ville
# - Pays


# Base de données notations
# - ID utilisateur
# - ID film
# - note