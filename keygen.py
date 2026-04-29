import streamlit as st
import hashlib

# INSERISCI QUI IL TUO SALE SEGRETO
SALT = "Adelina_inc"

st.set_page_config(page_title="Keygen Privato", page_icon="🔑")
st.title("🔑 Generatore Licenze")
st.write("Inserisci l'ID Hardware del PC.")

hw_id = st.text_input("ID Hardware:", placeholder="Es. A1B2-C3D4...")

if st.button("Genera Codice", type="primary"):
    if hw_id:
        combinazione = hw_id + SALT
        hash_object = hashlib.sha256(combinazione.encode())
        hash_hex = hash_object.hexdigest()
        codice = hash_hex[:8].upper()
        codice_formattato = f"{codice[:4]}-{codice[4:]}"
        st.success(f"Codice: **{codice_formattato}**")
    else:
        st.error("Inserisci un ID.")
