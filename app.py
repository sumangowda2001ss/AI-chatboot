from dotenv import load_dotenv
import streamlit as st
import os
import anthropic


load_dotenv() ## It will match the api_key from the folder. it authenticated with cloud A3 

def get_response(user_contet):

    client = anthropic.Anthropic() ## it will pass the acces to the entropic model called cloud a3.
    messages = client.messages.create( ## it will give the acces to cluade A3 model.
        model="claude-3-haiku-20240307",
        max_tokens=1000,
        system="Generate Details answers for User questions",
        messages=[{"role":"user","content":user_contet}]
        
    )
    return messages.content[0].text  ## use these entire funtion to get sum input from the streamlit and it will give us the output.

st.title("AI Chatboot")## Title of the streamlit.
user_content = st.text_input("Enter text to generate answers:")

if st.button("Generate Answers"):
    if not user_content:
        st.warning("Please, enter any text to generate answers",icons = "⚠")

    generated_titiles = get_response(user_content)
    st.success("Answer generated Succesfully")
    st.text_area("",value=generated_titiles,height=300)

