from dotenv import load_dotenv
from langchain_google_genai.llms import GoogleGenerativeAI
import streamlit as st
import PyPDF2 as pdf
import os
import warnings
warnings.filterwarnings("ignore")

api_key=os.getenv("GEMINI_API_KEY") 

load_dotenv()

# Sidebar for API key input
GEMINI_API_KEY = st.sidebar.text_input(label="🔐 Enter your Gemini-pro API key", type="password")

# Function to get LLM response
def get_response(input_text):
    try:
        llm = GoogleGenerativeAI(
            api_key=GEMINI_API_KEY,
            model="gemini-2.0-flash"
        )
        response = llm.invoke(input_text)
        return response
    except Exception as e:
        return f"An error occurred: {e}"

# Function to extract PDF text
def input_file(file):
    reader = pdf.PdfReader(file)
    text = ""
    for page in reader.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text
    return text

# Static summarization instructions
input_prompt_template = """
Summarize the following health document for both medical professionals and patients.

Health Topic: {jd}

Document Content:
{text}

---

For Medical Professionals:
- Include key medical findings, diagnosis, treatment plan, and relevant clinical terminology.

For Patients:
- Provide a clear and simple explanation of the condition, treatments, and any follow-up steps.
- Use easy-to-understand language.

Format your output into two clear sections: 'For Medical Professionals' and 'For Patients'.
"""

# Streamlit UI
st.title("🏥 HealthCare Report Summarizer")
st.info("Upload a patient record and get summaries for both doctors and patients.")

# Inputs
jd = st.text_area("📝 Enter health topic or description (optional):")
file1 = st.file_uploader("📄 Upload Patient Record (PDF)", type="pdf")
submit = st.button("🧾 Summarize Document")

# Processing logic
if submit:
    if not GEMINI_API_KEY:
        st.warning("Please enter your Gemini API key.")
    elif file1 is not None:
        with st.spinner("Analyzing document, please wait..."):
            text = input_file(file1)
            prompt = input_prompt_template.format(text=text, jd=jd)
            response = get_response(prompt)
            st.write(response)
            st.success("✅ Analysis complete!")
    else:
        st.warning("Please upload a PDF file.")
