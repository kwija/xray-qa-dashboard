import pandas as pd
import streamlit as st

st.title("Xray Test Dashboard - Démo")

df = pd.read_csv("../tests/sample_xray_data.csv")

st.write("Nombre total de tests :", len(df))
st.write("Répartition des résultats :")
st.bar_chart(df["Result"].value_counts())

st.write("Répartition par famille et résultat :")
pivot = pd.crosstab(df["Family"], df["Result"])
st.dataframe(pivot)
