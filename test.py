# Import the Streamlit library
import streamlit as st

# Title of the app
st.title("Simple Streamlit App")

# Subheader
st.subheader("Welcome to my first Streamlit app!")

# Text input
name = st.text_input("Enter your name:", placeholder="Type your name here...")

# Slider input
age = st.slider("Select your age:", 0, 100, 25)

# Button
if st.button("Submit"):
    if name:
        st.success(f"Hello, {name}! You are {age} years old.")
    else:
        st.warning("Please enter your name.")
else:
    st.write("Fill out the form and click Submit!")

# Additional Section
st.write("This is a simple app to get started with Streamlit.")
st.markdown("### Features Demonstrated:")
st.markdown("- Title and subheader")
st.markdown("- Text input")
st.markdown("- Slider")
st.markdown("- Button for user interaction")
