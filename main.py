import streamlit as st
import requests
import pickle
import pandas as pd

st.set_page_config(page_title="Movie Recommender", layout="wide")

movies_ = pickle.load(open('data/movies_dict.pkl', 'rb'))
movies_ = pd.DataFrame(movies_)
similarity = pickle.load(open('data/similarity.pkl', 'rb'))

API_KEY = "31e0895bfd96f19816c34fcd487126b4"
BASE_POSTER_URL = "https://image.tmdb.org/t/p/w500"

def get_movie_details(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={API_KEY}&language=en-US"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return None

def get_movie_poster(movie_id):
    details = get_movie_details(movie_id)
    if details and details.get("poster_path"):
        return f"{BASE_POSTER_URL}{details['poster_path']}"
    return "https://via.placeholder.com/200x300?text=No+Image"

def recommend(movie):
    movie_index = movies_[movies_['original_title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommendations = []
    for i in movies_list:
        movie_id = movies_.iloc[i[0]]['movie_id']
        poster = get_movie_poster(movie_id)
        details = get_movie_details(movie_id)

        recommendations.append({
            "title": details["original_title"],
            "poster": poster,
            "release_date": details.get("release_date", "N/A"),
            "rating": details.get("vote_average", "N/A"),
            "genres": ", ".join([genre["name"] for genre in details.get("genres", [])]),
            "overview": details.get("overview", "No description available.")
        })
    return recommendations

st.title("🎬 Movie Recommender System")
selected_movie = st.selectbox("🔍 Select a Movie:", movies_['original_title'].values)

st.markdown(
    """
    <style>
    body {
        background-color: white !important;
        color: black !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

if st.button("🎥 Recommend"):
    recommendations = recommend(selected_movie)

    if recommendations:
        st.markdown('<h3 style="text-align: center;">Recommended Movies</h3>', unsafe_allow_html=True)
        col1, col2, col3, col4, col5 = st.columns(5)

        for idx, movie in enumerate(recommendations):
            with [col1, col2, col3, col4, col5][idx]:
                st.image(movie["poster"], use_container_width=True)
                st.markdown(f"**{movie['title']}**")
                st.markdown(f"📅 {movie['release_date']}  |  ⭐ {movie['rating']}/10")
                st.markdown(f"🎭 {movie['genres']}")
                st.markdown(f"<p style='font-size: 12px; color: gray;'>{movie['overview']}</p>", unsafe_allow_html=True)
    else:
        st.warning("No recommendations found. Try another movie!")
