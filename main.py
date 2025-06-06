#passo 0: titulo
#passo 1: input do chat a cada mensagem enviada:
    #motrar msg envida 
    #motrar resposta

import streamlit as st

st.write("chatBOT com IA")

st.session_state["mensagens"]

prompt = st.chat_input("escrava sua mensagem aqui")

if prompt:
    st.chat_message("user").write(prompt)