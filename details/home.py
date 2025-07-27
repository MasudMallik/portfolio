import streamlit as st

col1,col2=st.columns(2)
col1.image("MY_IMG.jpg",width=200,)
col3,col4,col5,col6=st.columns(4)
col3.markdown("[linkedin_profile](https://www.linkedin.com/in/masud-mallik-a27538334?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app)")
col4.markdown("[Git-hub](https://github.com/MasudMallik)")
col5.write("tel:+919163176197")
col6.write("email: masudmallik96@gmail.com")
col2.title("Masud Mallik")
col2.text("3rd year AI & ML Student")
st.divider()
st.subheader("Objective")
st.text('''
I’m a 3rd-year undergraduate student pursuing a degree in Artificial Intelligence and Machine Learning (AIML), with a strong foundation in programming languages such as Python, C, R, and SQL. While I'm still at the beginning of my journey in Machine Learning, I’m deeply curious about how intelligent systems work and how data can be used to solve real-world problems.
Over time, I’ve developed several Python-based projects, which have helped me strengthen my logical thinking and problem-solving skills. I'm now actively exploring the fundamentals of machine learning — including data preprocessing, model building, and evaluation — through self-learning, coursework, and small practice projects.
My interest lies in understanding how data drives decisions, and I’m eager to learn more about AI, data analysis, and automation technologies. I enjoy working on practical coding tasks and always look for opportunities to improve and apply my skills in meaningful ways.
I’m currently seeking opportunities—such as internships, collaborative projects, or mentorships—that allow me to grow in a learning-focused environment while contributing to impactful projects.
 ''')
st.divider()

