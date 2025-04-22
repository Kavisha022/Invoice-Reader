from pdf_extraction import extract_text_from_pdf, langchain_tool

def main():
    pdf_path = "D:\OneDrive - Lowcode Minds Technology Pvt Ltd\Desktop\invoice_reader_project\sample_invoice.pdf" 
    
    # Extract text from the PDF
    text = extract_text_from_pdf(pdf_path)
    
    # Print the extracted text (optional, for debugging)
    print("Extracted Text from Invoice:")
    print(text)
    
    # Process the extracted text to get relevant details
    processed_result = langchain_tool(text)
    
    # Print the processed result in a clean format
    print("\nProcessed Invoice Details:")
    print(processed_result)
    print("\n")

if __name__ == "__main__":
    main()
