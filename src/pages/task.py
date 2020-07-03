"""Home page shown when the user enters the application"""
import streamlit as st

from package.awesome_streamlit.shared.components import title_awesome, video_youtube, horizontal_ruler

import numpy as np
import matplotlib.pyplot as plt


# pylint: disable=line-too-long
def write():
    """Used to write the page in the app.py file"""
    with st.spinner("Loading About ..."):
        
        horizontal_ruler(True)
        #Sidebar Nav
        hint = st.sidebar.checkbox("Show me a hint")
        if hint:
            st.sidebar.markdown("""
            Write some $\\KaTeX$
            $$
            f(x) = \\int_{-\\infty}^\\infty   \\hat f(\\xi)\\,e^{2 \\pi i \\xi x}   

            \\tilde{a}
            
            $$
            
            """)

        
        title_awesome("A bit of Linear Algebra")        
        st.write("Lets get started with some Audio")
        st.audio("https://gremloon-demo.s3-eu-west-1.amazonaws.com/cppcast-194.mp3", format='audio/mp3', start_time=0)

        st.markdown(
            '''## What is a Vector?'''
        )

        st.markdown(
            '''
            Vectors are everywhere: physics, engineering, mathematics, computer science, video games, and more. Each field's interpretation of what a vector is may be different, but vectors live a similar life in every space.

            The first episode in the wonderful video series, "Essence of Linear Algebra" tells you of three different ideas about vectors [1]:
            [Essence of Linear Algebra](https://www.youtube.com/playlist?list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab).

            1. For physicists, a vector is an "arrow" of a given length (magnitude) and direction. It can represent directional quantities like velocity, force, acceleration.
            2. For computer scientists, a vector is an ordered list of numbers. It can represent a set of variables or features stored in order.
            3. For mathematicians, vectors are generic objects that behave a certain way when they are added or scaled: $\\mathbf{u}+\\mathbf{v}$, $\\alpha\\mathbf{v}$.
            '''
        )
  
        code = st.checkbox("Show me the Code")
        if code:
            with st.echo():
                    V = np.array([[1,1],[-2,2],[4,-7]])
                    origin = [0], [0] # origin point

                    plt.quiver(*origin, V[:,0], V[:,1], color=['r','b','g'], scale=23)
                    st.write("Vector data:")
                    st.write(V)
                    st.pyplot()


        questions = st.checkbox("Show Questions")
        if questions:
            st.image('https://i.ibb.co/71VGGWn/fc7d8422-ae19-42ad-818d-bf79b1251013.png')
            st.text_input('')

            if st.button('Answer'):
                answer_correct = True

                if answer_correct:
                    st.write("This answer is correct")
        
       

            

        
     