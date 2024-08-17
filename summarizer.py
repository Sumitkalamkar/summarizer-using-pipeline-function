from transformers import pipeline
import streamlit as st

summarizer = pipeline('summarization')

st.title('Summarizer')


text = st.text_area("Enter the text you want to summarize")

if st.button('Get Summary'):
    if text:
        st.header('Summury:') 
        with st.spinner("Generating Summary...."):
            summary = summarizer(text, max_length=200, min_length=50, do_sample=False)
            st.write(summary[0]['summary_text'])
    else:
            st.write("Please enter some text to summarize.")
