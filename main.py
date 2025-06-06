
import streamlit as st
from openai import OpenAI

# usar chave segura
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

st.title("JARVIS")
st.write("Olá, senhor")

if "lista_mensagens" not in st.session_state:
    st.session_state["lista_mensagens"] = []

# mostrar histórico
for mensagem in st.session_state["lista_mensagens"]:
    st.chat_message(mensagem["role"]).write(mensagem["content"])

# entrada do usuário
mensagem_usuario = st.chat_input("Escreva sua mensagem aqui")

if mensagem_usuario:
    st.chat_message("user").write(mensagem_usuario)
    st.session_state["lista_mensagens"].append({"role": "user", "content": mensagem_usuario})

    resposta = client.chat.completions.create(
        model="gpt-4o",
        messages=st.session_state["lista_mensagens"]
    )

    resposta_ia = resposta.choices[0].message.content
    st.chat_message("assistant").write(resposta_ia)
    st.session_state["lista_mensagens"].append({"role": "assistant", "content": resposta_ia})
