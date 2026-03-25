import streamlit as st
import random

# Placar inicial
if "player_score" not in st.session_state:
    st.session_state.player_score = 0
    st.session_state.computer_score = 0
    st.session_state.history = []

st.title("🎮 Rock, Paper, Scissors vs Computer")

options = ["rock", "paper", "scissors"]
emojis = {"rock": "🪨", "paper": "📄", "scissors": "✂️"}

player = st.selectbox("Choose your move:", options)

if st.button("Play"):

    computer = random.choice(options)

    st.write(f"You chose: {emojis[player]} {player}")
    st.write(f"Computer chose: {emojis[computer]} {computer}")

    if player == computer:
        result = "Tie 🤝"
        st.info(result)

    elif (player == "rock" and computer == "scissors") or \
         (player == "scissors" and computer == "paper") or \
         (player == "paper" and computer == "rock"):
        result = "You win! 🎉"
        st.success(result)
        st.session_state.player_score += 1

    else:
        result = "Computer wins! 🤖"
        st.error(result)
        st.session_state.computer_score += 1

    # Histórico salvo
    st.session_state.history.append({
        "You": player,
        "Computer": computer,
        "Result": result
    })

# Placar
st.subheader("🏆 Score")
st.write(f"You: {st.session_state.player_score} | Computer: {st.session_state.computer_score}")

# Histórico
st.subheader("📜 Match History")
if st.session_state.history:
    st.table(st.session_state.history)
else:
    st.write("No games played yet.")

# Botão para reset
if st.button("Reset Game"):
    st.session_state.player_score = 0
    st.session_state.computer_score = 0
    st.session_state.history = []
    st.success("Game reset!")
