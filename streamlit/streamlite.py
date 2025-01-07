# Script pour l'application Streamlit "Le 23ème Écran".

# ------- INFOS POUR LANCER LE STREAMLIT -------
# Commande pour lancer sur Windows : streamlit run .\streamlit\streamlite.py
# Afficher le site web hébergé sur Git Hub / Streamlit Cloud : https://movie-recommendation-project-wcs-bleu-sauvage.streamlit.app/

# Autre fichier à supprimer quand dev finalisé :
# Commande pour lancer sur Windows : streamlit run .\streamlit\streamlit2.py


# ------- Import des bibliothèques nécessaires -------
import streamlit as st
import pandas as pd
from streamlit_option_menu import option_menu
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import os
from rapidfuzz import process, fuzz
from sklearn.neighbors import NearestNeighbors
from sklearn.preprocessing import MinMaxScaler


# ------- CHEMINS FICHIERS DONNEES -------
logo = "streamlit/logo.png"
style_css = "streamlit/style.css"
df_infos_csv = "donnees/data/df_info.csv.gz"
df_ml_csv = "machine learning/DF_ML.csv.gz"
image_cinema = "donnees/images/Cinéma.JPG"
image_cinema2 = "donnees/images/23_2.JPG"


# ------- CONFIGURATION GLOBALE -------
st.set_page_config(
    page_title="Cinéma le 23ème Écran",
    layout="wide")


# ------- CHARGEMENT DES DONNEES -------
@st.cache_data
def load_movie_infos():
    try:
        return pd.read_csv(df_infos_csv)
    except FileNotFoundError:
        st.error("Erreur : Impossible de charger le fichier des informations des films.")
        return pd.DataFrame()  # Retourner un DataFrame vide en cas d'erreur

# ------ Fonction de récupération du style CSS ------
def load_css(file_name):
    file_path = file_name
    try:
        with open(file_path) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    except FileNotFoundError:
        st.error("Erreur : Le fichier CSS n'a pas été trouvé. Vérifiez le chemin.")


df_infos = load_movie_infos()

load_css(style_css)


# ------- Fonction de similarité avec un modèle de ML -------
def recommandation(tconst):
    # Chargement des données
    df_ml = pd.read_csv(df_ml_csv)

    # Récupération des valeurs genre et pays qui correspondent au film sélectionné
    df_selection = df_ml[df_ml['tconst'] == tconst]
    colonnes_genre = [
        'Action', 'Adventure', 'Animation', 'Biography', 'Comedy', 'Crime',
        'Documentary', 'Drama', 'Family', 'Fantasy', 'Game-Show', 'History',
        'Horror', 'Music', 'Musical', 'Mystery', 'News', 'Reality-TV',
        'Romance', 'Sci-Fi', 'Sport', 'Talk-Show', 'Thriller', 'War', 'Western'
    ]
    colonnes_pays = [
        'tmdb_US', 'tmdb_FR', 'tmdb_GB', 'tmdb_DE', 'tmdb_JP', 'tmdb_IN',
        'tmdb_IT', 'tmdb_CA', 'tmdb_ES', 'tmdb_MX', 'tmdb_HK', 'tmdb_BR',
        'tmdb_SE', 'tmdb_SU', 'tmdb_PH', 'tmdb_KR', 'tmdb_AU', 'tmdb_CN',
        'tmdb_AR', 'tmdb_RU', 'tmdb_DK', 'tmdb_NL', 'tmdb_BE', 'tmdb_AT',
        'tmdb_TR', 'tmdb_PL', 'tmdb_CH', 'tmdb_XC', 'tmdb_FI', 'tmdb_NO',
        'tmdb_IR', 'tmdb_XG', 'tmdb_EG', 'tmdb_NG', 'tmdb_ZA'
    ]

    genre = [colonne for colonne in df_selection.columns if df_selection[colonne].iloc[0] == True and colonne in colonnes_genre]
    pays = [colonne for colonne in df_selection.columns if df_selection[colonne].iloc[0] == True and colonne in colonnes_pays]

    index = df_ml.index
    df_ml_num = df_ml.select_dtypes('number')
    df_ml_cat = df_ml.select_dtypes(['object', 'category', 'string', 'bool'])

    # Normalisation des colonnes numériques
    SN = MinMaxScaler()
    df_ml_num_SN = pd.DataFrame(SN.fit_transform(df_ml_num), columns=df_ml_num.columns, index=index)

    df_ml_encoded = pd.concat([df_ml_num_SN, df_ml_cat], axis=1)
    
    # Création d'une liste de colonnes à utiliser pour le modèle
    caracteristiques = df_ml_encoded.columns.drop(['tconst', 'nconst', 'title', 'title_ratings_numVotes', 'rating', 
        'Action', 'Adventure', 'Animation', 'Biography', 'Comedy', 'Crime',
        'Documentary', 'Drama', 'Family', 'Fantasy', 'Game-Show', 'History',
        'Horror', 'Music', 'Musical', 'Mystery', 'News', 'Reality-TV',
        'Romance', 'Sci-Fi', 'Sport', 'Talk-Show', 'Thriller', 'War', 'Western', 
        'tmdb_US', 'tmdb_FR', 'tmdb_GB', 'tmdb_DE', 'tmdb_JP', 'tmdb_IN',
        'tmdb_IT', 'tmdb_CA', 'tmdb_ES', 'tmdb_MX', 'tmdb_HK', 'tmdb_BR',
        'tmdb_SE', 'tmdb_SU', 'tmdb_PH', 'tmdb_KR', 'tmdb_AU', 'tmdb_CN',
        'tmdb_AR', 'tmdb_RU', 'tmdb_DK', 'tmdb_NL', 'tmdb_BE', 'tmdb_AT',
        'tmdb_TR', 'tmdb_PL', 'tmdb_CH', 'tmdb_XC', 'tmdb_FI', 'tmdb_NO',
        'tmdb_IR', 'tmdb_XG', 'tmdb_EG', 'tmdb_NG', 'tmdb_ZA'])
    
    # Sélection des films en fonction de la note
    bons_films = df_ml_encoded[df_ml_encoded['notes'] >= 0.7]

    # On veut que nos recommandations aient automatiquement un genre en commun et un pays de prod en commun avec le film selectionné
    bons_films = bons_films[bons_films[genre].any(axis=1)] if genre else bons_films
    bons_films = bons_films[bons_films[pays].any(axis=1)] if pays else bons_films

    # Création de notre modèle
    model = NearestNeighbors(n_neighbors=6, metric='euclidean')
    model.fit(bons_films[caracteristiques])

    # On déclare les caractéristiques du film sélectionné par l'utilisateur
    caract_film = df_ml_encoded[df_ml_encoded['tconst'] == tconst][caracteristiques]

    # Calcul des distances et indices des voisins
    distances, indices = model.kneighbors(caract_film)

    # Affichage de la sélection des films en fonction des indices trouvés par le modèle
    if caract_film['notes'].values[0] > 0.7:
        distances = distances[0][1:6]
        indices = indices[0][1:6]
        selection = bons_films.iloc[indices]['tconst']
    else:
        distances = distances[0][0:5]
        indices = indices[0][0:5]
        selection = bons_films.iloc[indices]['tconst']

    selection = pd.DataFrame(selection).reset_index(drop=True)

    # 2e reco : 5 films avec genre commun et pays différent

    # Sélection des films en fonction de la note
    bons_films2 = df_ml_encoded[df_ml_encoded['notes'] >= 0.7]

    # On veut que nos recommandations aient automatiquement un genre en commun et un pays de prod différent de celui du film selectionné
    bons_films2 = bons_films2[bons_films2[genre].any(axis=1)] if genre else bons_films
    bons_films2 = bons_films2[~bons_films2[pays].any(axis=1)] if pays else bons_films

    # Création de notre modèle
    model2 = NearestNeighbors(n_neighbors=6, metric='euclidean')
    model2.fit(bons_films2[caracteristiques])

    distances2, indices2 = model2.kneighbors(caract_film)

    # Affichage de la sélection des films en fonction des indices trouvés par le modèle
    if caract_film['notes'].values[0] > 0.7:
        distances2 = distances2[0][1:6]
        indices2 = indices2[0][1:6]
        selection2 = bons_films2.iloc[indices2]['tconst']
    else:
        distances2 = distances2[0][0:5]
        indices2 = indices2[0][0:5]
        selection2 = bons_films2.iloc[indices2]['tconst']

    selection2 = pd.DataFrame(selection2).reset_index(drop=True)
    
    if selection.equals(selection2):
        st.session_state["nb_selection"] = 1

    return afficher_resultats_similarite(selection, selection2)


# ------- Fonctions de navigation -------

def afficher_menu():
    col1, col2 = st.columns([1, 3]) # Structure en 4 colonnes pour l'en-tête
    with col1:
        st.image(logo, use_container_width=True)
    with col2:
        if "menu_choice" not in st.session_state:
            st.session_state["menu_choice"] = "Accueil" 
        options = ["Accueil", "À propos", "Actualités"]
        cols = st.columns(len(options))
        for i, option in enumerate(options):
            if cols[i].button(option, key=f"menu_bouton_{option}"):
                st.session_state["menu_choice"] = option
                # Réinitialiser la recherche quand l'utilisateur clique sur "Accueil"
                if option == "Accueil":
                    st.session_state["search_query"] = ""
                    if 'nb_selection' in st.session_state:
                        del st.session_state['nb_selection']
                    if 'search_query' in st.session_state:
                        del st.session_state['search_query']
                    st.rerun()

# Fonction qui identifie les noms de films les plus proches avec le texte entré dans la barre de recherches
def search(query, choices):
    if 'nb_selection' in st.session_state:
        del st.session_state['nb_selection']
    # Convertir les chaînes en minuscules
    query_lower = query.lower()
    choices_lower = [choice.lower() for choice in choices]

    # Effectuer la recherche sur les chaînes en minuscules
    results = process.extract(query_lower, choices_lower, limit=10, scorer=fuzz.WRatio, score_cutoff=90)
    
    # Filtrer les résultats en conservant uniquement les éléments dont le score est suffisant
    filtered_results = [choices[choices_lower.index(result[0])] for result in results if result[1] >= 50]
    
    return filtered_results



def handle_movie_selection(titre, tconst):
    st.session_state["search_query"] = titre
    st.session_state["menu_choice"] = "Accueil"
    if 'nb_selection' in st.session_state:
        del st.session_state['nb_selection']


def afficher_accueil():
    st.markdown(
        """
        ## Bienvenue au **23ème Écran**, votre cinéma local au cœur de la Creuse !
        Ici, nous ne nous contentons pas de projeter des films : nous célébrons le septième art avec passion et convivialité, dans une ambiance qui répond aux attentes de chaque spectateur.

        En plus de notre programmation en salle, découvrez notre moteur de recommandations personnalisées. 
        Il s’appuie sur vos goûts pour vous proposer des films qui correspondent à vos préférences. 
        Mais ce n’est pas tout : nous vous invitons également à élargir vos horizons avec notre sélection "Sortir des sentiers battus". 
        Celle-ci regroupe des œuvres audacieuses : créations internationales, films d’auteur, productions indépendantes... toujours choisies pour leur qualité et leur originalité. Plus d'infos : visitez notre page "A propos"
        """
    )
    st.markdown("<div class='search-container'>", unsafe_allow_html=True)
    
    # Réinitialiser la recherche si elle n'existe pas
    if "search_query" not in st.session_state:
        st.session_state["search_query"] = ""

    search_query = st.text_input(
        "Pour recevoir des suggestions personnalisées :",
        value=st.session_state["search_query"],
        placeholder="Renseignez le titre d'un film que vous appréciez...",
        key="search_input"
    )
    
    if st.session_state.get("search_query"):
        search_query = st.session_state["search_query"]
        st.session_state["search_query"] = "" # Réinitialiser la recherche après l'utilisation
        
    st.markdown("</div>", unsafe_allow_html=True)
    
    if search_query:
        
        # Créer une colonne combinée "Titre (Année)" dans le DataFrame
        df_infos['Titre_Affiche'] = df_infos['Titre'] + " (" + df_infos['Année de Sortie'].astype(str) + ")"

        results = search(search_query, df_infos['Titre_Affiche'].tolist())
        if results:
            # Créer un dictionnaire associant "Titre (Année)" au tconst
            options = {}
            for _, row in df_infos[df_infos['Titre_Affiche'].isin(results)].iterrows():
                options[row['Titre_Affiche']] = row['tconst']
            
            # Sélectionner le film dans la selectbox
            selected_title = st.selectbox("Sélectionnez un film :", list(options.keys()), key="film_select")
            
            # Récupérer le tconst correspondant au film sélectionné
            tconst_selectionne = options[selected_title]
            
            st.markdown(f"<h2>Votre sélection</h2>", unsafe_allow_html=True)
            
            col3, col4 = st.columns([1, 3])
            col5, col6 = st.columns([1, 3])
            
            # Affichage des détails du film sélectionné
            film_info = df_infos[df_infos['tconst'] == tconst_selectionne].iloc[0]
            
            with col3:
                st.markdown(f"<h3>{film_info['Titre']} ({film_info['Année de Sortie']})</h3>", unsafe_allow_html=True)
            
            with col5:
                if pd.notna(film_info["Chemin Affiche"]):
                    st.image(f"https://image.tmdb.org/t/p/w500{film_info['Chemin Affiche']}", width=150)
                else:
                    st.markdown(
                        f"<div style='width: 150px; height: 225px; background-color: black; color: white; display: flex; justify-content: center; align-items: center; text-align: center;'>{film_info['Titre']}</div>",
                        unsafe_allow_html=True
                    )
            
            with col6:
                st.markdown(f"Synopsis : {film_info['Synopsis']}")
                st.markdown(f"Durée : {film_info['Durée (min)']} min")
                st.markdown(f"{film_info['genres']}")
                etoiles_jaunes = "⭐" * int(round(film_info['Note'] / 2))
                st.markdown(f"{round(film_info['Note'],1)}/10 {etoiles_jaunes}")
                st.markdown(f"{int(film_info['Indice Bechdel'])}/3 🙍‍♀️ Test de Bechdel")
            
            # Appeler la fonction de recommandation avec le tconst
            recommandation(tconst_selectionne)
        else:
            st.write("Aucun résultat trouvé.")
    else:
        st.write("Commencez à taper pour voir les suggestions.")



def afficher_resultats_similarite(selection, selection2):
    st.markdown(f"<h2>Nos recommandations</h2>", unsafe_allow_html=True)
    df_display = df_infos.set_index('tconst').loc[selection['tconst']].reset_index()
    
    num_cols = 5
    rows = [df_display.iloc[i:i + num_cols] for i in range(0, len(df_display), num_cols)]

    for row_index, row_df in enumerate(rows):
        cols = st.columns(num_cols)

        for col_index, row in enumerate(row_df.iloc):
            with cols[col_index]:
                if pd.notna(row["Chemin Affiche"]):
                    st.image(f"https://image.tmdb.org/t/p/w500{row['Chemin Affiche']}", width=150)
                else:
                    st.markdown(
                        f"<div style='width: 150px; height: 225px; background-color: black; color: white; display: flex; justify-content: center; align-items: center; text-align: center;'>{row['Titre']}</div>",
                        unsafe_allow_html=True
                    )

                st.markdown(f"**{row['Titre']}**", unsafe_allow_html=True)
                st.markdown(f"{row['Année de Sortie']} - {row['Durée (min)']} min")
                st.markdown(f"{row['genres']}")

                etoiles_jaunes = "⭐" * round(row['Note'] / 2)
                st.markdown(f"{round(row['Note'],1)}/10 {etoiles_jaunes}")
                st.markdown(f"{int(row['Indice Bechdel'])}/3 🙍‍♀️ Test de Bechdel")

                unique_key = f"bouton_{row['tconst']}_{row_index}_{col_index}"
                if st.button("Voir les détails de ce film", 
                           key=unique_key,
                           on_click=handle_movie_selection,
                           args=(row['Titre'], row['tconst'])):
                    pass

                st.markdown(f"<br>", unsafe_allow_html=True)

        for col in cols[len(row_df):]:
            with col:
                st.empty()
        
    if 'nb_selection' not in st.session_state:
        st.markdown(f"<h2>Sortir des sentiers battus</h2>", unsafe_allow_html=True)
        df_display = df_infos.set_index('tconst').loc[selection2['tconst']].reset_index()
        
        num_cols = 5
        rows = [df_display.iloc[i:i + num_cols] for i in range(0, len(df_display), num_cols)]

        for row_index, row_df in enumerate(rows):
            cols = st.columns(num_cols)

            for col_index, row in enumerate(row_df.iloc):
                with cols[col_index]:
                    if pd.notna(row["Chemin Affiche"]):
                        st.image(f"https://image.tmdb.org/t/p/w500{row['Chemin Affiche']}", width=150)
                    else:
                        st.markdown(
                            f"<div style='width: 150px; height: 225px; background-color: black; color: white; display: flex; justify-content: center; align-items: center; text-align: center;'>{row['Titre']}</div>",
                            unsafe_allow_html=True
                        )

                    st.markdown(f"**{row['Titre']}**", unsafe_allow_html=True)
                    st.markdown(f"{row['Année de Sortie']} - {row['Durée (min)']} min")
                    st.markdown(f"{row['genres']}")

                    etoiles_jaunes = "⭐" * round(row['Note'] / 2)
                    st.markdown(f"{round(row['Note'],1)}/10 {etoiles_jaunes}")
                    st.markdown(f"{int(row['Indice Bechdel'])}/3 🙍‍♀️ Test de Bechdel")

                    unique_key = f"bouton_{row['tconst']}_{row_index}_{col_index}"
                    if st.button("Voir les détails de ce film", 
                            key=unique_key,
                            on_click=handle_movie_selection,
                            args=(row['Titre_Affiche'], row['tconst'])):
                        pass

                    st.markdown(f"<br>", unsafe_allow_html=True)

            for col in cols[len(row_df):]:
                with col:
                    st.empty()


def afficher_a_propos():
    st.markdown("<header>", unsafe_allow_html=True)
    st.title("À propos")

    st.image(image_cinema2, width=400, caption="Le 23ème Ecran, en plein coeur de la ville !")
    
    st.markdown(
        """
        ### Notre histoire  
        Niché au cœur de **Guéret**, le cinéma **Le 23ème Écran** est né d’une ambition claire : revitaliser l’offre culturelle de notre région. Nous proposons une programmation riche et variée, mêlant **grands classiques**, **nouveautés incontournables**, et **pépites indépendantes**, pour satisfaire toutes les générations et répondre à toutes les envies.  

        ### Une expérience cinématographique unique  
        - **Un confort moderne** : Profitez de salles équipées des dernières technologies pour une qualité d’image et de son exceptionnelle.  
        - **Des événements exclusifs** : Avant-premières, soirées thématiques, rencontres avec des réalisateurs ou des acteurs… Chaque séance peut devenir un moment d’échange unique.  
        - **Un espace détente** : Venez partager un instant convivial autour d’un café ou discuter cinéma avant ou après votre séance.  

        ### Le moteur de recommandations : votre guide cinéphile  
        Pour prolonger votre expérience, nous avons développé un **moteur de recommandations personnalisé**.  
        Avec cet outil intuitif, disponible directement sur notre site, découvrez des films qui reflètent vos goûts et laissez-vous surprendre par des suggestions originales. Qu’il s’agisse d’un grand classique ou d’une œuvre indépendante, nous vous aidons à explorer le cinéma à votre manière, en toute simplicité.  

        ### Une ouverture sur le monde du cinéma  
        Au **23ème Écran**, nous croyons que le cinéma est une porte ouverte sur d’autres horizons. Nos choix de programmation incluent des documentaires captivants, des trésors méconnus et des films qui invitent à réfléchir, ressentir et découvrir. Soucieux de diversité et de représentation, nous intégrons également l’**indice Bechdel** à nos descriptions, pour vous aider à explorer les œuvres avec un regard éclairé.  

        ### Notre mission  
        Notre objectif est simple : faire du cinéma une expérience mémorable pour chacun. Nous avons à cœur de soutenir les talents locaux et internationaux, tout en innovant pour offrir une expérience accessible et connectée.  

        **Merci d’être à nos côtés dans cette aventure. Nous avons hâte de vous accueillir dans nos salles pour partager ensemble la magie du cinéma.**
        """,
        unsafe_allow_html=True
    )
    st.markdown("</header>", unsafe_allow_html=True)


def afficher_actualites():
    st.title("Actualités")
    st.markdown(
        """
        ## 🎥 Les Dernières Nouvelles du 23ème Écran !
        Découvrez toutes les actualités de votre cinéma préféré à Guéret. Restez informé des événements, avant-premières et nouveautés qui font vivre notre salle !
        """
    )

    st.subheader("✨ Événements à venir")
    st.markdown(
        """
        - **Vendredi 12 janvier 2025 : Avant-première exclusive**  
          Venez découvrir *"Les Lumières de la Creuse"*, un documentaire inédit sur notre région, suivi d'une discussion avec le réalisateur.
        
        - **Samedi 20 janvier 2025 : Soirée rétrospective**  
          Thème : *Les chefs-d'œuvre des années 80*. Plongez dans l'univers de Spielberg, Lucas, et bien d'autres !
        
        - **Dimanche 28 janvier 2025 : Atelier cinéma pour enfants**  
          Atelier créatif pour apprendre à réaliser un court-métrage, dès 10 ans (sur réservation).
        """
    )

    st.subheader("🎞 Nouveautés à l'affiche")
    st.markdown(
        """
        - **"La Montagne Sacrée"** : Une épopée fascinante sur les mystères des contes tibétains.  
          (Salle 2, tous les jours à 17h30)  
        - **"Cœurs à Contre-temps"** : Une comédie romantique à ne pas manquer !  
          (Salle 1, séances à 15h et 20h)  
        - **"Le Dernier Horizon"** : Le blockbuster de l'année, en 4K et Dolby Atmos.  
          (Salle 1, séances à 14h, 18h et 21h30)
        """
    )

    st.subheader("🌟 Focus sur le cinéma local")
    st.markdown(
        """
        - **"Regards sur la Creuse"** : Une sélection de courts-métrages réalisés par des talents locaux.  
          Projection gratuite, dimanche 14 janvier à 16h (Salle 3).  

        - **Festival du film régional** : Soutenons le cinéma de chez nous avec une programmation unique du 22 au 28 février 2025.
        """
    )

    st.subheader("📅 Réservez vos places dès maintenant !")
    st.markdown(
        """
        - **Réservations en ligne :** Rendez-vous sur notre site pour réserver vos billets en toute simplicité.  
        - **Tarifs réduits :** Profitez de nos tarifs avantageux pour les étudiants, seniors et familles.
        """
    )
    
    st.image(image_cinema, width=400, caption="Votre cinéma au cœur des événements 🎬")


# ------- Interface Utilisateur (UI) -------
if "search_query" not in st.session_state:
    st.session_state["search_query"] = ""
if "current_page" not in st.session_state:
    st.session_state["current_page"] = "Accueil"

# Navigation
afficher_menu()

# Affichage du contenu en fonction du menu choisi
menu_choice = st.session_state.get("menu_choice", "Accueil")

if menu_choice == "Accueil":
    afficher_accueil()
elif menu_choice == "À propos":
    afficher_a_propos()
elif menu_choice == "Actualités":
    afficher_actualites()