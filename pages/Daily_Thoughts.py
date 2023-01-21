import streamlit as st

st.header("Enter your thoughts for the day")

date = st.selectbox("Day of the Week", ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"))
thoughts = st.text_input("What are your thoughts on how today went")

if thoughts:
    while True:
        match date:
            case "Monday":
                filepath = "diary/1.Monday.txt"
            case "Tuesday":
                filepath = "diary/2.Tuesday.txt"
            case "Wednesday":
                filepath = "diary/3.Wednesday.txt"
            case "Thursday":
                filepath = "diary/4.Thursday.txt"
            case "Friday":
                filepath = "diary/5.Friday.txt"
            case "Saturday":
                filepath = "diary/6.Saturday.txt"
            case "Sunday":
                filepath = "diary/7.Sunday.txt"
            case _:
                print("Please select one of the dates")
        with open(filepath, "w") as file:
            file.write(thoughts)
        break
elif thoughts == "":
    st.text("Please enter a thought")
