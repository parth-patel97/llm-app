import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.environ["GEMINI_API_KEY"])

def main():
    st.title("Symptom Checker and Medical Advice")

    # User Input
    symptoms = st.text_area("Enter your symptoms, separated by commas:")
    concerns = st.text_area("Enter your concerns:")

    if st.button("Get Advice"):
        if symptoms and concerns:
            # Construct OpenAI prompt
            prompt = f"User is experiencing symptoms: {symptoms}. They are concerned and want to know possible medical conditions associated with these symptoms and any general advice."

            model = genai.GenerativeModel("gemini-1.5-flash")
            response = model.generate_content(prompt)
            # # Get OpenAI response
            # response = openai.Completion.create(
            #     engine="text-davinci-003",
            #     prompt=prompt,
            #     max_tokens=300,
            #     temperature=0.1,
            # )

            # Display OpenAI response
            st.write("Possible Conditions and General Advice:")
            st.write(response.text)


if __name__ == "__main__":
    main()
