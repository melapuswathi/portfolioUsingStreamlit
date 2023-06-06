import streamlit as sl#Ensure you have matplotlib installed.
import matplotlib.pyplot as plt
import pandas as pd

# Setting the page configurations
sl.set_page_config(page_title="my portfolio", page_icon="🙍‍♀️",layout="wide")

#Adding background to my page
def add_bg_from_url():
    sl.markdown(
         f"""
         <style>
         .stApp {{
             background: radial-gradient(circle, rgba(238,174,202,0) 82%, rgba(148,187,233,1) 100%);
        }}
         </style>
         """,
         unsafe_allow_html=True
     )

add_bg_from_url() 

# Sharing a little about who am I
#The container kind of groups things together
with sl.container():
    sl.subheader("Hi there, I am SWATHI 👋")
    sl.title("Fervent of Tech")
    # Write function is just like writing normal text on the page. Like a paragraph thing.
    sl.write("I am a girl with lots of passion and hunger to learn and explore things in the field.")

with sl.container():
    #The below will set up a beautiful looking horizontal line for us
    sl.write("---") 
    #The below will divide the page width into two parts
    left_column,right_column = sl.columns(2)

    with left_column:
        sl.title("My projects")
        sl.subheader("Weather Application : React JS")
        sl.write("Weather Application is an application which gives you the real time weather in the searched region")
        sl.subheader("Quiz Application : HTML,CSS,JavaScript")
        sl.write("Quiz application allows you to attempt an easy quiz and gives you the end percentage on its completion")

    with right_column:
        #Image() is used to add images to our page with thier path as an input
        sl.image("./Images/working_on_projects.jpg")
    
    with sl.container():
        sl.write("---")
        left_column,right_column = sl.columns(2)
        with left_column:
            sl.image("./Images/skills.png")
        with right_column:
            sl.title("My skills")
            sl.write("HTML")
            sl.write("CSS")
            sl.write("JavaScript")
            sl.write("C")
            sl.write("Python")
            sl.write("Java")
            sl.write("React JS")
            sl.write("SQL")

with sl.container():
    sl.write("---")
    left_column,right_column = sl.columns(2)
    with left_column:
        sl.title("Hobbies")
        sl.write("📝 Blogging")
        #The below line os code allows us to navigate to another link.
        sl.write("[Find my blogs here ->](https://swathimelapu.hashnode.dev)")
        sl.write("📃 Reading")
        sl.write("🌱 Gardening")
        sl.write("👩‍🏫 Exploring new technologies")
        sl.title("My socials")
        sl.write("[Connect with me on linked In](https://www.linkedin.com/in/swathi-melapu-67b359211/)")
        sl.write("[ My Github profile](https://github.com/melapuswathi)")
    
    with right_column:
        sl.image("./Images/hobbies.jpg")

with sl.container():
        sl.write("---")
        sl.header("Get in touch with me in case of queries. I would love you reply back!")
        sl.write("[Let's Connect](https://form.jotform.com/231539317019051)")


    




            







