import streamlit as st
from pdf_extraction import extract_text_from_pdf, langchain_tool

# Streamlit app interface
def main():
    st.title("Invoice PDF Reader")
    
    # File uploader to upload invoice PDF
    uploaded_file = st.file_uploader("Choose an invoice PDF", type="pdf")
    
    if uploaded_file is not None:
        # Save uploaded file temporarily
        with open("uploaded_invoice.pdf", "wb") as f:
            f.write(uploaded_file.getbuffer())
        
        # Extract text from PDF
        text = extract_text_from_pdf("uploaded_invoice.pdf")
        st.text_area("Extracted Text", text, height=300)
        
        # Process the extracted text with Langchain
        processed_result = langchain_tool(text)
        
        st.subheader("Processed Invoice Details:")
        st.write(processed_result)

# Run the Streamlit app
if __name__ == "__main__":
    main()











