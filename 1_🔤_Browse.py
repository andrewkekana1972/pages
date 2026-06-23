"""
Browse page — A–Z directory of all English words in the dictionary.
Click a letter to list every English entry starting with it; click a word
to jump back to the main dictionary page with that term searched.
"""
import csv
import os
import urllib.parse
import streamlit as st

from ui_theme import apply_theme, page_header, section_title

# Resolve CSV relative to project root (one level up from /pages)
CSV_FILE = os.path.join(os.path.dirname(os.path.dirname(__file__)), "bantu_dictionary_HNumbers.csv")

st.set_page_config(
    page_title="Browse — Hebrew–Bantu Dictionary",
    page_icon="🔤",
    layout="wide",
    initial_sidebar_state="collapsed",
)
apply_theme()

# Extra CSS for the A–Z letter grid
st.markdown(
    """
    <style>
    .hb-az {
        display: flex; flex-wrap: wrap; gap: .45rem;
        margin: .5rem 0 1.5rem;
    }
    .hb-az a {
        display: inline-flex; align-items: center; justify-content: center;
        width: 44px; height: 44px;
        background: var(--surface);
        border: 1px solid var(--line);
        border-radius: 10px;
        font-family: 'Fraunces', Georgia, serif;
        font-weight: 700; font-size: 1.05rem;
        color: var(--primary-2);
        text-decoration: none !important;
        box-shadow: var(--shadow-sm);
        transition: all .15s;
    }
    .hb-az a:hover, .hb-az a.active {
        background: var(--primary); color: #fff !important;
        border-color: var(--primary); transform: translateY(-1px);
    }
    .hb-az a.disabled {
        opacity: .35; pointer-events: none;
    }
    .hb-word-grid {
        display: grid;
        grid-template-columns: repeat(auto-fill, minmax(180px, 1fr));
        gap: .5rem; margin-top: .75rem;
    }
    .hb-word-grid a {
        display: block;
        padding: .55rem .85rem;
        background: var(--surface);
        border: 1px solid var(--line);
        border-radius: 10px;
        color: var(--ink);
        text-decoration: none !important;
        font-size: .95rem;
        box-shadow: var(--shadow-sm);
        transition: all .12s;
    }
    .hb-word-grid a:hover {
        border-color: var(--primary);
        color: var(--primary) !important;
        transform: translateY(-1px);
    }
    </style>
    """,
    unsafe_allow_html=True,
)

page_header(
    "Browse the dictionary",
    "Pick a letter to see every English entry starting with it.",
)


@st.cache_data
def load_english_words():
    """Return {letter: sorted [unique english words]}."""
    buckets: dict[str, set[str]] = {}
    try:
        with open(CSV_FILE, "r", encoding="utf-8") as f:
            for row in csv.reader(f):
                if len(row) < 10:
                    continue
                word = row[5].strip()
                if not word:
                    continue
                first = word[0].upper()
                if not first.isalpha():
                    continue
                buckets.setdefault(first, set()).add(word)
    except FileNotFoundError:
        return {}
    return {ltr: sorted(words, key=str.lower) for ltr, words in buckets.items()}


words_by_letter = load_english_words()

if not words_by_letter:
    st.warning("Dictionary file not found. Make sure `bantu_dictionary_HNumbers.csv` "
               "sits next to `dictionary_app.py`.")
    st.stop()

# Selected letter via ?letter=A
params = st.query_params
selected = params.get("letter", "A")
if isinstance(selected, list):
    selected = selected[0]
selected = (selected or "A").upper()[:1]
if selected not in words_by_letter:
    # fall back to the first letter that has entries
    selected = sorted(words_by_letter.keys())[0]

# A–Z bar
section_title("A – Z")
letters_html = "<div class='hb-az'>"
for code in range(ord("A"), ord("Z") + 1):
    ltr = chr(code)
    available = ltr in words_by_letter
    cls = "active" if ltr == selected else ("" if available else "disabled")
    href = f"?letter={ltr}" if available else "#"
    letters_html += f"<a class='{cls}' href='{href}' target='_self'>{ltr}</a>"
letters_html += "</div>"
st.markdown(letters_html, unsafe_allow_html=True)

# Word list for the selected letter
matches = words_by_letter.get(selected, [])
section_title(f"{selected} — {len(matches)} entr{'y' if len(matches)==1 else 'ies'}")

if not matches:
    st.info(f"No English words start with “{selected}”.")
else:
    grid = "<div class='hb-word-grid'>"
    for w in matches:
        href = f"/?q={urllib.parse.quote(w)}"
        grid += f"<a href='{href}' target='_self'>{w}</a>"
    grid += "</div>"
    st.markdown(grid, unsafe_allow_html=True)

st.markdown(
    "<div style='margin-top:2rem;'>"
    "<a href='/' target='_self' style='color:var(--primary);font-weight:600;'>← Back to dictionary</a>"
    "</div>",
    unsafe_allow_html=True,
)
