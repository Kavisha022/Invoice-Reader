# 🧾 Invoice PDF Reader using LangChain & Streamlit

This project is a **Streamlit-based web application** that reads invoice PDFs, extracts text, and processes it using **LangChain + OpenAI** to retrieve meaningful information like:

- ✅ Vendor Name  
- ✅ Customer Name  
- ✅ Invoice Date  

It ignores line items, totals, and prices to focus on high-level invoice metadata.

---

## 📦 Features

- Upload and read any invoice PDF
- Text extraction using **pdfplumber**
- Intelligent extraction using **LangChain + OpenAI**
- Clean Streamlit interface
- Also includes a CLI version for terminal use

---


---

## 🚀 How It Works

1. Upload a PDF invoice in the Streamlit UI.
2. The text is extracted using `pdfplumber`.
3. The extracted text is passed to a LangChain prompt template.
4. An OpenAI-powered LLM processes and returns key invoice fields.
5. Results are displayed in a clean, readable format.

---
