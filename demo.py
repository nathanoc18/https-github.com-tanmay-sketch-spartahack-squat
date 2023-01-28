import streamlit as st

st.title("Squat Analysis")

recorded_file = 'output_sample.mp4'
sample_vid = st.empty()
sample_vid.video(recorded_file)