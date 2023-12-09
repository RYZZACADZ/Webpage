import requests
import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image


# Find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="My Webpage", page_icon=":tada:", layout="wide")


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style/style.css")

# ---- LOAD ASSETS ----
lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_fcfjwiyb.json")
img_contact_form = Image.open("ryzza.jpg")
img_lottie_animation = Image.open("ryzza1.jpg")

# ---- HEADER SECTION ----
with st.container():
    st.subheader("Hi, I am Ryzza Cadelina:wave:")
    st.title("A Computer Engineering Student from SNSU")
    st.write(
        "I am a SK member in our Barangay Cayawan in Municipality of Malimono."
    )
    st.write("[Learn More >](https://pythonandvba.com)")

# ---- WHAT I DO ----
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("Drug Awareness")
        st.write("##")
        st.write(
            """
            On my Facebook Page I am posting Slogan about Drug Awareness:
            - Seeking a path to break free from the chains of substance abuse.
            - Struggling to overcome the cycle of addiction and seeking support.
            - Aspiring to spread awareness about the dangers of drugs and make a positive impact.
            - Realizing the need for change in our communities and standing against the grip of addiction."

            If this sounds interesting to you, consider liking and turning on the notifications, so you don’t miss any content.
            """
        )
        st.write("[Facebook Page >](https://www.facebook.com/profile.php?id=61554521967444&mibextid=hIlR13)")
    with right_column:
        st_lottie(lottie_coding, height=300, key="coding")

# ---- PROJECTS ----
with st.container():
    st.write("---")
    st.header("Video Suggestion")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_lottie_animation)
    with text_column:
        st.subheader("Student Drug and Alcohol Awareness")
        st.write(
            """
            Is a program designed to educate students about the risks and consequences 
            of drug and alcohol abuse. It aims to increase awareness, promote responsible decision-making, 
            and provide support resources to help students make informed choices regarding their health and well-being. 
            The program may include information on the effects of substances, prevention strategies, and avenues for seeking help if needed.
            """
        )
        st.markdown("[Watch Video...](https://youtu.be/HxXgVbYXVEs?si=_o9sUrBCbKyYl9v4)")
with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_contact_form)
    with text_column:
        st.subheader("Drug Abuse Awareness | eLearning Course")
        st.write(
            """
            is a concise online educational program designed to inform individuals about the risks and 
            consequences of drug abuse. The course likely covers essential information, preventive measures,
            and resources through an electronic learning platform, enabling participants to enhance their 
            understanding of drug-related issues in a convenient and accessible manner.
.
            """
        )
        st.markdown("[Watch Video...](https://youtu.be/a-PWkIZ0vUY?si=tbWLKsR6jmBcJtou)")

# ---- CONTACT ----
with st.container():
    st.write("---")
    st.header("Get In Touch With Me!")
    st.write("##")

    # Documention: https://formsubmit.co/ !!! CHANGE EMAIL ADDRESS !!!
    contact_form = """
    <form action="https://formsubmit.co/ryzzacadz@MAIL.COM" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()