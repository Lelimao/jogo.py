import streamlit as st

st.title("🎮 Pedra, Papel e Tesoura")

opcoes = ("pedra", "papel", "tesoura")

jogador1 = st.selectbox("Jogador 1 escolha:", opcoes)
jogador2 = st.selectbox("Jogador 2 escolha:", opcoes)

if st.button("Ver resultado"):

    if jogador1 == jogador2:
        st.write("🤝 Empate!")

    elif (jogador1 == "pedra" and jogador2 == "tesoura") or \
         (jogador1 == "tesoura" and jogador2 == "papel") or \
         (jogador1 == "papel" and jogador2 == "pedra"):
        st.success("🏆 Jogador 1 venceu!")

    else:
        st.success("🏆 Jogador 2 venceu!")