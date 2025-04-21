import streamlit as st
import openai

st.title("Movie Rating ")
st.write("Enter a movie summary and get a predicted IMDb rating.")

movie_summary = st.text_area("Movie Summary", height=200)

if movie_summary:
    response = openai.chat.completions.create(
        model="gpt-4o-mini",
        messages = [
            {"role": "system", "content": "You are a helpful assistant that predicts IMDb ratings based on plot synopsis of a movie"},
            {"role": "user", "content": f"Here is a plot synopsis: {movie_summary}\nRating: "}
        ], 
        temperature=0.3, 
        max_tokens=10
    )
    predicted_rating = response.choices[0].message.content
    st.success(f"Predicted IMDb Rating: {predicted_rating}")