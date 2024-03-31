import streamlit as st
import PyPDF2
import re
from io import BytesIO

def extract_text_from_pdf(uploaded_file):
    with BytesIO(uploaded_file.read()) as f:
        reader = PyPDF2.PdfReader(f)
        num_pages = len(reader.pages)
        metadata = reader.metadata
        text = ""
        for page_num in range(num_pages):
            page_text = reader.pages[page_num].extract_text()
            if re.search(r"\w", page_text):
                text += page_text
    return metadata, num_pages, text

def main():
    st.title("textify")
    st.subheader('textify is a tool for extracting information from PDF', divider='rainbow')
    
    uploaded_file = st.file_uploader("upload a PDF file", type="pdf")
    if uploaded_file is not None:
        metadata, num_pages, text = extract_text_from_pdf(uploaded_file)
        
        st.write("Metadata:", metadata)
        st.write("Number of pages:", num_pages)
        st.write("Extracted text:", text)

if __name__ == "__main__":
    main()
