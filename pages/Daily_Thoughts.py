import streamlit as st

st.header("Enter your thoughts for the day")

date = st.selectbox("Day of the Week", ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"))
thoughts = st.text_input("What are your thoughts on how today went")

if thoughts:
    while True:
        if date == "Monday":
            filepath = "diary/1.Monday.txt"
        elif date == "Tuesday":
            filepath = "diary/2.Tuesday.txt"
        elif date == "Wednesday":
            filepath = "diary/3.Wednesday.txt"
        elif date == "Thursday":
            filepath = "diary/4.Thursday.txt"
        elif date == "Friday":
            filepath = "diary/5.Friday.txt"
        elif date == "Saturday":
            filepath = "diary/6.Saturday.txt"
        elif date == "Sunday":
            filepath = "diary/7.Sunday.txt"
        else:
            print("Please select one of the dates")
        with open(filepath, "w") as file:
            file.write(thoughts)
            break
elif thoughts == "":
    st.text("Please enter a thought")
