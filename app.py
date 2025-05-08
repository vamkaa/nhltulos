import streamlit as st

#Valintasivu
st.title("🏒 NHL Tulosveikkaaja")
st.subheader("Valitse ennustettava kohde:")

# Valitaan kumpaa ennustetaan
valinta = st.selectbox("Mitä haluat ennustaa?", ["Ottelun voittaja", "Pelaajan maalin todennäköisyys"])

# Ennustelomake ottelun voittajalle
if valinta == "Ottelun voittaja":
    st.header("⚔️ Ennusta ottelun voittaja")
    
    # Syötteet
    kotijoukkue = st.text_input("Kotijoukkueen nimi")
    vierasjoukkue = st.text_input("Vierasjoukkueen nimi")
    playoff = st.selectbox("Onko kyseessä playoff-peli?", ["Kyllä", "Ei"]) == "Kyllä"

    # Ennustuspainike
    if st.button("Veikkaa voittaja"):
        st.write("Syötetyt tiedot:")
        st.write(f"Kotijoukkue: {kotijoukkue}")
        st.write(f"Vierasjoukkue: {vierasjoukkue}")
        st.write(f"Onko playoff: {playoff}")
        st.success("(Tähän tulee ottelun ennustetulos myöhemmin)")

# Ennustelomake pelaajan maalille
elif valinta == "Pelaajan maalin todennäköisyys":
    st.header("🥅 Ennusta pelaajan maalin todennäköisyys")
    
    # Syöte: pelkkä pelaajan nimi
    pelaaja = st.text_input("Pelaajan nimi")

    # Ennustuspainike
    if st.button("Laske maalin todennäköisyys"):
        st.write("Syötetyt tiedot:")
        st.write(f"Pelaaja: {pelaaja}")
        st.success("(Tähän tulee maalin todennäköisyys myöhemmin)")
