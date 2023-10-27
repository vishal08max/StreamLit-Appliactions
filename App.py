from PIL import Image
import requests
import streamlit as st
from streamlit_lottie import st_lottie
st.set_page_config(page_title="My Webpage", page_icon=":tada:",layout="wide")
img = Image.open("Bio_pic.png")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_fcfjwiyb.json")
lottie_bio = load_lottieurl("https://lottie.host/f1a64b9c-13a2-4c3c-8da9-ce30ce818acb/RHdp1wB2Vm.json")
lottie_certify = load_lottieurl("https://lottie.host/6a1988ac-a562-4ba6-ab12-cc0d3dcedf5b/IFStiNQc3y.json")
lottie_interest = load_lottieurl("https://lottie.host/0140f76e-af6e-4318-a7ba-975f4e56daa1/IDLbNnBO42.json")
lottie_contact = load_lottieurl("https://lottie.host/efb2c9f6-da60-45c0-b52b-4be37d2b287e/yJJoyovjOC.json")
lottie_awards = load_lottieurl("https://lottie.host/b6137027-23d8-4a46-b452-abd6058ef824/GFXjYKEMY6.json")
lottie_hobbies = load_lottieurl("https://lottie.host/a50c3997-e9e5-420a-81b2-34f245db26f3/pG4kDmjPjh.json")

# ---- Header Section ---- #
with st.container():
        st.title("Profile Overview:")
        st.image(img)
        left_column, right_column = st.columns(2)
        st.subheader("Hi, I am Vishal Raj :wave:")
        st.title("Aspiring Fresher Computer Science Student | Software Engineer | Data Analyst From Bangalore.")
        st.write("A Passionate and Detail-oriented Computer Science Graduate seeking to embark on a Dynamic journey in the world of Technology. Armed with a solid foundation in computer science principles and hands-on experience in cutting-edge technologies, I am eager to contribute my skills to innovative projects and solutions.")
        
        
# ---- What I do ----- #
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.title("What I do:")
        st.write("##")
        st.write(
            """
            Passionate about turning raw data into meaningful insights, I am a results-driven Data Analyst with a keen eye for detail and a knack for uncovering trends. Armed with a Computer Science Engineering With Artificial Intelligence and Machine Learning from Don Bosco Institute Of Technology and 5 years of hands-on experience in the field, I have honed my analytical skills to transform complex datasets into actionable recommendations.
            """
        )
    with right_column:
       st_lottie(lottie_bio, height=300, key="bio")

# ---- Skills Section ---- #
with st.container():
    st.write("---")
    st.title("My Skills:")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("Programming Language")
        st.write("""
            Python | Javascript | C """)

        st.header("Frontend tools")
        st.write("""HTML | CSS | StreamLit""")

        st.header("""Backend Tools""")
        st.write("""MySQL | Django""")

        st.subheader("Data Structures and Algorithms")    
    with right_column:
        st.header("Data & Visualisation")
        st.write("""Pandas | Numpy | Matplotlib""")

        st.header("ReactJS")    
        st.write("""Hooks""")

        st.header("""ML Libraries""")
        st.write("""Scikit-Learn""")
    
# ---- Projects ----- #
with st.container():
    st.write("---")
    st.title("My Projects:")
    st.write("##")
    left_column, right_column = st.columns(2)
    with left_column:
            st.header("Major And Minor Projects:")
            st.write(
                """
                Python Projects:
                1. Hard Rock Cafe Restaurant:
                Using Python Core based on classes and objects, I have developed a Restaurant
                project which will take orders and prints the bill for customer.

                2. Rental Vehicle System:
                Vehicle Rental System using Python Core which will give rental plans for 2 wheelers
                and 4 wheelers including 18% GST tax in the form of Command Line.

                3. Python Automate WhatsApp Messenger:
                Mini Project on Python Core Called PythonAutomateWhatsApp Messenger which
                is a code built for WhatsApp, which will send the message for respected Person
                automatically on scheduled time.

                Machine Learning Projects:
                
                4. House Price Prediction:
                Developed a House Price Prediction Model based on the number of BHKs and
                Bathrooms, implemented using Machine learning - Linear RegressionAlgorithm
                and Data Science techniques, can provide valuable insights for real estate
                stakeholders.
                """
            )
    with right_column:
        st_lottie(lottie_coding, height=300, key="coding")

# --- Certificates --- #
with st.container():
    st.write("---")
    st.title("Certificates:")
    left_column, right_column = st.columns(2)
    with left_column:
            st.header("Cyber Security and Ethical Hacking:")
            st.write("""Internship Course Completed
            Through Rinex - IIT Kharagpur""")

            st.header("Artificial Intelligence and Machine Learning:")
            st.write("""Internship Course Completed
            Through Rinex - IIT Kharagpur""")

            st.header("Freshers Labs:")
            st.write(""" Internship Completed In The Field Of Data Science and Machine Learning""")
    with right_column:
       st_lottie(lottie_certify, height=300, key="certify")

# --- Awards --- #
with st.container():
    st.write("---")
    st.title("Awards:")
    left_column, right_column = st.columns(2)
    with left_column:
            st.header("Hackathons:")
            st.write("""
            Has participated in Hackathons \n
            Has participated in Technical Competitions like Project Building and Debugging.""")

    with right_column:
       st_lottie(lottie_awards, height=300, key="awards")

# --- Interests --- #
with st.container():
    st.write("---")
    st.title("Interests:")
    left_column, right_column = st.columns(2)
    with left_column:
            st.header("Competative Coding:")
            st.write("""Python""")

            st.header("Data Science and Machine Learning")
            
            st.header("Python")
    with right_column:
        st_lottie(lottie_interest, height=300, key="interest")
            
# --- Hobbies --- #
with st.container():
    st.write("---")
    st.title("Hobbies:")
    left_column, right_column = st.columns(2)
    with left_column:
            st.header("Painting")

            st.header("Sketching")
            
            st.header("Listening To Music")

            st.header("Dancing")
    with right_column:
        st_lottie(lottie_hobbies, height=300, key="hobbies")

# ---- Contact ---- #
with st.container():
    st.write("---")
    st.title("Get In Touch With Me!")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("Contact:")
        st.write("📞9148150888")

        st.header("LinkdIn:")
        st.write("https://www.linkedin.com/in/vishal-raj-n-285372273/")

        st.header("GitHub - Projects Studio:")
        st.write("https://github.com/vishal08max")

    with right_column:
        st_lottie(lottie_contact, height=300, key="contact")
    
