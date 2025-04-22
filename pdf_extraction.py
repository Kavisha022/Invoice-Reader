import pdfplumber
from langchain.prompts import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain

# Function to extract text from the invoice PDF
def extract_text_from_pdf(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        text = ""
        for page in pdf.pages:
            text += page.extract_text()
    return text

# Create a simple tool to process the extracted text with Langchain
def langchain_tool(text):
    # Initialize Langchain with OpenAI and simple prompt processing
    prompt_template = """
    Given the following invoice text, please extract the following:
    1. Vendor Name
    2. Customer Name
    3. Invoice Date
    Exclude any itemized list, quantities, prices and total amounts.

    Invoice Text: {text}
    """
    prompt = PromptTemplate(input_variables=["text"], template=prompt_template)

    # Pass the OpenAI API key directly
    openai_api_key = "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"  # Replace with your actual API key
    chat_openai = ChatOpenAI(temperature=0.5, openai_api_key=openai_api_key)
    
    chain = LLMChain(prompt=prompt, llm=chat_openai)
    
    result = chain.run(text=text)
    return result