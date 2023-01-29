import streamlit as st

st.title("Squat Analysis")
st.markdown('''
This is a demo of the Squat Analysis app. It provides feedback on your squat form and gives you a score based on your form.
''')

recorded_file = 'output_sample.mp4'
sample_vid = st.empty()
sample_vid.video(recorded_file)