"""Main module for the streamlit app"""
import streamlit as st
from package.awesome_streamlit.shared.components import write_page
import package.awesome_streamlit as ast

import src.pages.task
import src.pages.home


ast.core.services.other.set_logging_format()

PAGES = {
    "Home": src.pages.home,
    "Task": src.pages.task,
}


def main():
    """Main function of the App"""
    #st.sidebar.image()
    st.sidebar.image('./assets/img/gremloon_red.png')
    selection = st.sidebar.radio("Go to", list(PAGES.keys()))

    page = PAGES[selection]

    with st.spinner(f"Loading {selection} ..."):
        write_page(page)
    
   


if __name__ == "__main__":
    main()
