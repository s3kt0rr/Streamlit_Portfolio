import requests
import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image

st.set_page_config(page_title= "Aryan Singh", page_icon=":computer:", layout="wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

#-----LOADING  ASSETS-------

lottie_coding = load_lottieurl("https://assets8.lottiefiles.com/private_files/lf30_wqypnpu5.json")

image_ass = Image.open("images/121.png")
image_ytd = Image.open("images/ytd.png")


def css_file(file_name):
    with open (file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

css_file("style/style.css")

# -----Header Section -----]

with st.container():

        st.subheader("Hi, I am Aryan :punch: ")
        st.title("A Python Developer From Bangalore")
        st.write("I am passionate about finding ways to use python for problem solving.")
        st.write("[Github](https://github.com/s3kt0rr)")

#-----About-------

with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I do")
        st.write("##")
        st.write(
            """
            I am a Freelance Developer and I am making :
            - Websites and Landing pages for small Buisness and Portfolios for booming artists and studios
            - Automating Repetative Tasks using Python and its Libraries
            - Developing Videogames as an Hobby
            """
        )

    with right_column:
        st_lottie(lottie_coding, height=500, key="coding")


# -----Projects ---- #

with st.container():
    st.write("---")
    st.header("My Projects")
    st.write("##")
    image_column, text_column = st.columns((1,2))

    with image_column:
        st.image(image_ass)

    with text_column:
        st.subheader("Automated Security System")
        st.write(
            
            """
            A sinmple yet Advanced python based security system with various use cases like Motion Detection, Alarm, Face Detection and many more using 
            pythons unique libraries like OpenCV and a Fully Function GUI using Tkinter.
            """
        )
        st.markdown("[Github Source](https://github.com/s3kt0rr/Automated_Security_System)")


with st.container():
    image_col, text_col = st.columns((1,2))
    with image_col:
        st.image(image_ytd)
    with text_col:
        st.subheader("Minimal Youtube Downloader")
        st.write(
            """
            A Fully Functional yet minimal (Tkinter)GUI Based YouTube Downloader made with the help of "pytube" a youtube library for downloading and extracting information
            from youtube videos with the link.
            """
        )
        st.markdown("[Github Source](https://github.com/s3kt0rr/Minimal-Youtube-Downloader)")


#-----contact form----

with st.container():
    st.write("---")
    st.header("Get in Touch !")
    st.write("##")

    cont_form = """
    <form action="https://formsubmit.co/developeraryansingh@gmail.com" method="POST">
     <input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder = "Your Name" required>
     <input type="email" name="email" placeholder = "Your Email" required>
     <textarea name="message" placeholder="Your message here" required></textarea>
     <button type="submit">Send</button>
    </form>
    """

    lef_col, righ_col =st.columns(2)
    with lef_col:
        st.markdown(cont_form, unsafe_allow_html=True)
    with righ_col:
        st.empty()

#---Footer----

with st.container():
    st.write("##")

    

footer="""

<!--Footer--> 
<footer style="height:auto; background-color:#F7C201;">
  <h1><Made with 🤍 at DigitalOcean</h1>
</footer>
"""
st.markdown(footer,unsafe_allow_html=True)

