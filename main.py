import streamlit as st
from datetime import datetime

#func to display the current time
def display_time():
  now = datetime.now()
  current_time = now.strftime("%H:%M:%S")
  return current_time

#sidebar for navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Homepage", "About"])

#homepage
if page == "Homepage":
  st.title("Homepage")
  st.subheader("Welcome To Homepage")

  #display current time
  st.write(f"### Current time: {display_time()}")

#about page
elif page == "About":
  st.title("About")
  st.subheader("Here's something about me")
  
