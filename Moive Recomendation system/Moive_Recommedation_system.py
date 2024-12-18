import streamlit as st
import pandas as pd
import random

from streamlit import title, button

ds= pd.read_csv('.venv/Movie_Clusters.csv')


def recommandation(movie_name: str, recommendation=5):
    moive_name = movie_name.lower()
    ds['name'] = ds['name'].str.lower()
    moive = ds[ds['name'].str.contains(moive_name, na=False)]
    if not moive.empty:
        cluster = moive['Cluster_name'].values[0]
        moive_clusters = ds[ds['Cluster_name'] == cluster]

        if len(moive_clusters) >= 5:
            recommended = random.sample(list(moive_clusters['name']), recommendation)
        else:
            recommended = list(moive_clusters['name'])

        return recommended
    else:
        print("Movie Does Not found un the database ")


st.title("Movie Recommendation System  By Teacher Noor")
st.write('==============================================')
st.write('Supported Dataset')
st.write('1: Netflix TV Shows And Movies')
st.write('2: HBO TV Shows And Movies')
st.write('3: Amazon TV Shows And Movies')
st.write('==============================================')

movie_names=ds['name'].values

movie=st.selectbox("Search for movie you like ",options=movie_names)

if st.button("Recommend"):
    st.write("Your recommended movies are :")
    recommandations=recommandation(movie)
    st.dataframe(recommandations)

