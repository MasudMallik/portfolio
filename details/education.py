import streamlit as st
st.title("Education")
st.divider()
st.html('''<h1>Bachelor of Technology (B.Tech) </h1>''')
st.text(''' DEPT:   Artificial Intellagence And Machine Learning 
College Name:    St. Thomas’ College of Engineering And Technology 
Expected Graduation:    2027 
''')
with st.expander("Sgpas"):
    col1,col2=st.columns(2)
    col1.write("Semester")
    col2.write("SGPA")
    col1.divider()
    col2.divider()
    col1.write("sem1: ")
    col2.write("8.8")
    col1.write("sem2: ")
    col2.write("8.73")
    col1.write("sem3: ")
    col2.write("9.05")
    col1.write("sem4: ")
    col2.write("8.05")
st.write("\n")
st.html('''<h1>Higher Secondary(12th),Pure science </h1>''')
st.text(''' School Name:     Collins Institite  
Percentage:     78.40% 
Year:   2023 | Board:    WBCHSE
''')
with st.expander("Grades"):
    col1,col2=st.columns(2)
    col1.write("SUBJECT")
    col2.write("GRADE")
    col1.divider()
    col2.divider()
    col1.write("BENGALI: ")
    col2.write("A+")
    col1.write("ENGLISH: ")
    col2.write("A+")
    col1.write("BIOLOGY: ")
    col2.write("A")
    col1.write("CHEMISTRY: ")
    col2.write("B+")
    col1.write("PHYSICS: ")
    col2.write("A")
    col1.write("MATHEMATICS: ")
    col2.write("A+")
st.write("\n")
st.html('''<h1>Madhyamik(10th) </h1>''')
st.text(''' School Name:     St. Peter’s High School   
Percentage:      91.14% 
Year:   2021 | Board:   WBBSE
''')
with st.expander("Grades"):
    col1,col2=st.columns(2)
    col1.write("SUBJECT")
    col2.write("GRADE")
    col1.divider()
    col2.divider()
    col1.write("First language(BENGALI:) ")
    col2.write("AA")
    col1.write("Second language(ENGLISH:) ")
    col2.write("A+")
    col1.write("MATHEMATICS: ")
    col2.write("AA")
    col1.write("PHYSICAL SCIENCE: ")
    col2.write("AA")
    col1.write("LIFE SCIENCE: ")
    col2.write("AA")
    col1.write("HISTORY: ")
    col2.write("A+")
    col1.write("GEOGRAPHY: ")
    col2.write("AA")

