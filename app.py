import streamlit as st

st.title("🏒 NHL Tulosveikkaaja")

# Syötteet
kotijoukkue = st.text_input("Kotijoukkueen nimi")
vierasjoukkue = st.text_input("Vierasjoukkueen nimi")
playoff = st.selectbox("Onko kyseessä playoff-peli?", ["Kyllä", "Ei"]) == "Kyllä"

# Ennustuspainike
if st.button("Veikkaa voittaja"):
    # Tässä kutsutaan myöhemmin muiden tekemää ennustefunktiota
    st.write("Syötetyt tiedot:")
    st.write(f"Kotijoukkue: {kotijoukkue}")
    st.write(f"Vierasjoukkue: {vierasjoukkue}")
    st.write(f"Onko playoff: {playoff}")
    st.success("(Tähän tulee ennustetulos myöhemmin)")
