import streamlit as st
import requests

API_URL = "https://0d1d-35-230-11-195.ngrok-free.app/predict"

st.title("Financial RAG Chatbot")
st.write("Ask financial questions based on company earnings reports!")

# User input
query = st.text_input("Enter your financial query:")

if st.button("Get Answer"):
    if query:
        # Send request to Colab API
        response = requests.post(API_URL, json={"query": query})
        
        if response.status_code == 200:
            data = response.json()
            st.success(f"**Answer:** {data['answer']}")
            st.info(f"**Confidence Score:** {data['confidence_score']}")
        else:
            st.error(f"Error: {response.json().get('error', 'Unknown error')}")
    else:
        st.warning("Please enter a query!")
