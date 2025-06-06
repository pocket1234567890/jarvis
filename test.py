import streamlit as st

st.write("Jarvis")

if "mensagens" not in st.session_state:
    st.session_state["mensagens"] = []
    msg = st.chat_input("escrava sua mensagem aqui")