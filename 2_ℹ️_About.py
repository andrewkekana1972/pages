import streamlit as st
from ui_theme import apply_theme, page_header, section_title

st.set_page_config(
    page_title="About — Hebrew-Bantu Dictionary",
    page_icon="📖",
    layout="wide",
)

st.markdown("""
<style>

/* Google Fonts */
@import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@400;600;700&family=Cormorant+Garamond:wght@400;500;600&display=swap');

/* Page background */
.stApp{
    background:#F8F3EA;
}

/* Hide Streamlit header */
header[data-testid="stHeader"]{
    background:transparent;
}

section[data-testid="stSidebar"]{
    background:#F8F3EA;
}

/* Main page */
.main .block-container{
    max-width:900px;
    padding-top:2rem;
    padding-bottom:4rem;
}

/* Hero title */
.hh-title{
    font-family:'Cinzel',serif;
    font-size:3rem;
    text-align:center;
    color:#2F2F2F;
    letter-spacing:.08em;
    margin-bottom:.25rem;
}

/* Motto */
.hh-motto{
    font-family:'Cormorant Garamond',serif;
    font-style:italic;
    text-align:center;
    font-size:1.6rem;
    color:#7A5A2E;
    margin-bottom:2rem;
}

/* Subtitle */
.hh-subtitle{
    font-family:'Cormorant Garamond',serif;
    text-align:center;
    font-size:1.25rem;
    color:#555;
    margin-bottom:4rem;
}

/* Chapter heading */
.hh-heading{
    font-family:'Cinzel',serif;
    font-size:2.1rem;
    color:#5B4323;
    margin-top:3rem;
    margin-bottom:.6rem;
}

/* Body text */
.hh-body{
    font-family:'Cormorant Garamond',serif;
    font-size:1.35rem;
    line-height:1.75;
    color:#2F2F2F;
}

/* Quotation */
.hh-quote{
    text-align:center;
    font-family:'Cormorant Garamond',serif;
    font-style:italic;
    font-size:2rem;
    color:#7A5A2E;
    margin:4rem 0;
}

</style>
""", unsafe_allow_html=True)

apply_theme()

st.markdown("""

<div style="text-align:center;font-size:4.5rem;margin-top:2rem;">
𓃾
</div>

<div class="hh-title">
THE HEBREW HERITAGE PROJECT
</div>

<div class="hh-motto">
Language remembers.
</div>

<div class="hh-subtitle">
Exploring Ancient Hebrew through the Languages of Africa
</div>

""", unsafe_allow_html=True)


st.markdown('<div class="hh-heading">Mission</div>', unsafe_allow_html=True)

st.markdown("""

<div class="hh-body">

It all began with a desire to teach the Bible to my children in a way that was truthful and edifying to their character.

As I was lying on the floor reading from a picture Bible to my daughter, a question troubled me.

<b>Did the Israelites really look like this?</b>

That simple question began a journey that eventually became the Hebrew Heritage Project.

The deeper I searched, the more I realised that language preserves memory.

</div>

""", unsafe_allow_html=True)


st.markdown("""

<div class="hh-quote">

"Language remembers."

</div>

""", unsafe_allow_html=True)


st.markdown('<div class="hh-heading">The Project</div>', unsafe_allow_html=True)

st.markdown("""

<div class="hh-body">

The Hebrew Heritage Project explores relationships between Ancient Hebrew and the languages spoken throughout Africa.

Rather than beginning with assumptions, the project begins with questions, follows linguistic evidence, and invites readers to explore the data for themselves.

The Dictionary, the Ancient Word Explorer, and the Heritage Library together form a growing platform dedicated to this research.

</div>

""", unsafe_allow_html=True)


st.markdown('<div class="hh-heading">Research Principles</div>', unsafe_allow_html=True)

st.markdown("""

<div class="hh-body">

• Begin with questions, not conclusions.<br><br>

• Language remembers.<br><br>

• Culture gives language meaning.<br><br>

• Similarity alone is never proof.<br><br>

• Evidence should be examined across many African languages.

</div>

""", unsafe_allow_html=True)


st.markdown("---")

st.caption("© The Hebrew Heritage Project")
