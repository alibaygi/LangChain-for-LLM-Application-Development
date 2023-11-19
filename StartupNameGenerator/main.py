import streamlit as st
import langchain_sng_helper

st.title("Startup Name Generator")
business = st.sidebar.selectbox(
    "Pick a Business", ("Technology and Software Services", "Healthcare and Wellness", "Sustainability and Clean Energy",
                        "E-commerce and Retail Tech", "Fintech", "EdTech"))


if business:
    response = langchain_sng_helper.generate_startup_name_and_roles(business)
    st.header(response['startup_name'].strip())
    roles = response['roles'].strip().split(",")
    st.write("**Roles Items**")
    for item in roles:
        st.write("-", item)


# streamlit run main.py
# /Documents/Educational/NLP_langchain_indian/1_langchain_crash_course/StartupNameGenerator$ streamlit run main.py
# Command to run Docker image: docker run -d -p 8501:8501 <streamlit-app-name>:latest
