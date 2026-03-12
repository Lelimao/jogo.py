import streamlit as st
import random

st.title("🎮 Pedra, Papel e Tesoura vs Computador")

opcoes = ["pedra", "papel", "tesoura"]

jogador = st.selectbox("Escolha sua jogada:", opcoes)

if st.button("Jogar"):

    computador = random.choice(opcoes)

    st.write(f"Você escolheu: {jogador}")
    st.write(f"Computador escolheu: {computador}")

    if jogador == computador:
        st.info("Empate!")

    elif (jogador == "pedra" and computador == "tesoura") or \
         (jogador == "tesoura" and computador == "papel") or \
         (jogador == "papel" and computador == "pedra"):
        st.success("Você venceu!")

    else:
        st.error("Computador venceu!")