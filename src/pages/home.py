"""Home page shown when the user enters the application"""
import streamlit as st
from package.awesome_streamlit.shared.components import title_awesome, video_youtube, write_md


# pylint: disable=line-too-long
def write():
    """Used to write the page in the app.py file"""
    with st.spinner("Loading Home ..."):

        st.sidebar.title("About")
        st.sidebar.info(
            """
            Demo by Gremloon
            """
        )
        
        title_awesome("Home")


        write_md("https://gremloon-demo.s3-eu-west-1.amazonaws.com/test.md")
                
        st.video("https://www.youtube.com/embed/fNk_zzaMoSs", format='video/mp4', start_time=60)

     
