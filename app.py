
import sqlite3
import pandas as pd
import streamlit as st


st.title("Min træningstracker")
st.write("velkommen til min træningstracker! Her kan du logge dine træningssessioner og holde styr på dine fremskridt.")
st.write("Jeg er meget stolt over dette projekt, da det er mit første projekt, hvor jeg har brugt Python og Streamlit til at oprette en simpel webapplikation. Jeg håber, at du vil finde det nyttigt og inspirerende!")

st.subheader("træningsprogram 3 dage split")

forbindelse = sqlite3.connect("traening.db")

ovelser = pd.read_sql_query("SELECT dag, navn, muskelgruppe, saet, rep_min, rep_max FROM ovelser", forbindelse)

st.dataframe(ovelser, hide_index=True) # behøver ikke vise 0,1,2, altså tal på rækkerne 

st.subheader("log dine træningssessioner")


