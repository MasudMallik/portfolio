import streamlit as st

education=st.Page(
    page="details/education.py",
    icon="🕵️‍♂️",
    title="education",
)
home=st.Page(
    page="details/home.py",
    icon="🏠",
    title="Home",
    default=True
)
projects=st.Page(
    page="details/projects.py",
    icon="🕵️‍♂️",
    title="projects",
)
cert=st.Page(
    page="details/certificate.py",
    title="Certificates",
    icon="📄"
)
skill=st.Page(
    page="details/skills.py",
    title="skills",
    icon="📄"
)
Experience=st.Page(
    page="details/experience.py",
    icon="👷",
    title="Experience"
)

pg=st.navigation(
    {
        "info":[home,education,cert,skill,projects,Experience],
      
    }
)

pg.run()