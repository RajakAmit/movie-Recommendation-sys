import pickle
from audioop import reverse

import streamlit as st
import requests
import pandas as pd




def fetch_poster(movie_id):
    response=requests.get('https://api.themoviedb.org/3/movie/{}?api_key=941cde1c52d15f779f9d81f2c00269bb&language=en-US'.format(movie_id))
    data= response.json()
    print(data)
    return "http://image.tmdb.org/t/p/w500/"+data['poster_path']

def recommend(selected_movie):
    movie_index = movie[movie['title'] == selected_movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)),reverse=True, key= lambda x: x[1])[1:6]


    recommended_movie=[]
    recommended_movie_poster=[]

    for i in movie_list:
        movie_id=movie.iloc[i[0]].movie_id

        recommended_movie.append(movie.iloc[i[0]].title)
        #fetch poster from api

        recommended_movie_poster.append(fetch_poster(movie_id))
    return recommended_movie,recommended_movie_poster



movie_dict=pickle.load(open('movie_dict.pkl','rb'))
movie=pd.DataFrame(movie_dict)

similarity=pickle.load(open('similarity.pkl','rb'))


st.title('Movie Recommender System')

selected_movie_name = st.selectbox(
    "How would you like to be contacted?",
    movie['title'].values)

# st.write("Recommend:", selected_movie_name)
st.button("Reset", type="primary")
if st.button("Recommend"):
    names,posters =recommend(selected_movie_name)
    col1, col2, col3,col4,col5 = st.columns(5)

    with col1:
        st.text(names[0])
        st.image(posters[0])

    with col2:
        st.text(names[1])
        st.image(posters[1])

    with col3:
        st.text(names[2])
        st.image(posters[2])

    with col4:
        st.text(names[3])
        st.image(posters[3])

    with col5:
        st.text(names[4])
        st.image(posters[4])







