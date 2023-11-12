import streamlit as st
import pandas

st.set_page_config(layout="wide")
col1, col2 = st.columns(2)


with col1:
    st.image("images/profile.jpg", width=500)
    ###can add images/photo.png, width=600)


with col2:
    st.title("Kostas Diamantopoulos")
    content = """
    Welcome to my software development portfolio!I am a passionate about software developing looking to change my career 
    and get into the tech industry. In this portfolio you will discover a variety of projects i have created with Python
    with Django, Flask, MySQL databases, API's, Jupyter notebook, Bootstrap, Css, HTML, Git, Anacondas.
    I am familiar with windows and Linux-Debian.
    
    I'm always open to new opportunities. If you'd like to get in touch, please feel free to reach out to my email
    kostas.diam@hotmail.com. Thank you for taking the time to explore my portfolio. I look forward to connecting and
    collaborating with others in the software development community. """

    st.info(content)


col3, empty_col,  col4 = st.columns([1.5, 0.5, 1.5])

df = pandas.read_csv("data.csv", sep=";")

with col3:
    for index, row in df[9:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[source Code]({row['url']}")

with col4:
    for index, row in df[:9].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[source Code]({row['url']}")
