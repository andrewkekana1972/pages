import streamlit as st
from ui_theme import apply_theme, page_header, section_title

st.set_page_config(
    page_title="About — Hebrew-Bantu Dictionary",
    page_icon="📖",
    layout="wide",
)

apply_theme()

page_header(
    "About this project",
    "Exploring relationships between Hebrew roots and words preserved across African languages",
)

st.markdown(
    """
The **Hebrew-Bantu Dictionary** explores relationships between Hebrew roots and
words preserved across African languages.

The project is built around the **Ancient Hebrew Lexicon of the Bible (AHLB)**
by Jeff Benner and compares Hebrew roots with words found throughout Bantu and
other African languages.
"""
)

section_title("Features")
st.markdown(
    """
- Search by **English**, **Hebrew**, or **Bantu** words
- Explore related **Strong's numbers**
- Listen to **audio pronunciations**
- View **language distribution maps**
- Examine complete **AHLB root families**
- Discover **words shared across Africa**
"""
)

section_title("Purpose")
st.markdown(
    """
The purpose of the project is to investigate linguistic and cultural
connections among African languages and their relationship to ancient
Hebrew roots.
"""
)

section_title("Sources")
st.markdown(
    """
- Strong's Concordance
- Ancient Hebrew Lexicon of the Bible (AHLB)
- Blue Letter Bible
- Audio recordings and language coordinate data collected for this project
"""
)

section_title("Website")
st.markdown("[HebrewBantu.com](https://hebrewbantu.com)")

st.markdown("---")
st.caption("© Hebrew-Bantu Dictionary Project")
