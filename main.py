import streamlit as st

#st.set_page_config(layout="wide")
col1, col2 = st.columns(2)
with col1:
    st.image("images/photo.png")

with col2:
    st.title("Opeyemi Oriolowo")
    content = """
    I am Opeyemi Oriolowo, an accomplished IT Support Engineer with a robust background in troubleshooting and resolving complex technical issues. With extensive experience in both remote and desk-side support, I excel in providing user support, performing root cause analysis, and implementing effective solutions to enhance system performance.
    Additionally, I have substantial experience with Python programming and DevOps practices, enabling seamless integration and deployment of applications, as well as automation of processes to improve efficiency and reliability.
    """
    st.info(content)
