import streamlit as st
from scrape import scrape_website, extract_body_content, clean_body_content, split_dom_content
from parse import parse_with_groq

st.title("AI Web Scraper")
url= st.text_input("Enter the URL of the website to scrape:")

if st.button("Scrape Website"):
    if url:
        st.write(f"Scraping the website...")
        # Here you would call your scraping function
        # For example: results = scrape_website(url)
        results = scrape_website(url)
        body_content = extract_body_content(results)
        cleaned_content = clean_body_content(body_content)

        st.session_state.dom_content = cleaned_content
        with st.expander("View DOM Content"):
            st.text_area("DOM Content", cleaned_content, height=300)


        print(results)
    else:
        st.error("Please enter a valid URL.")


if "dom_content" in st.session_state:
    parse_description = st.text_area("Describe what you want to parse?")

    if st.button("Parse Content"):
        if parse_description:
            st.write("Parsing the content...")
            dom_chunks= split_dom_content(st.session_state.dom_content)
            results = parse_with_groq(dom_chunks, parse_description)
            st.write(results)
        else:
            st.error("Please enter a valid description.")

