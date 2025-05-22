                                           🏥 Health Document Summarizer
                                                                                                        

This Streamlit-based app summarizes health-related documents (PDFs) for both medical professionals and patients, using Google's Gemini Pro LLM.

🚀 Features
🔐 Secure API key input via sidebar

📄 Upload patient health records in PDF format

🤖 Summarizes content using Gemini 2.0 Flash model

🧑‍⚕️ Dual output:

Medical summary for professionals

Easy-to-understand summary for patients

🛠️ Tech Stack
Python

Streamlit

LangChain (GoogleGenerativeAI integration)

PyPDF2

dotenv

📦 Installation
Clone the repository:

  git clone https://github.com/your-username/health-doc-summarizer.git
  cd health-doc-summarizer

Install dependencies:

  pip install -r requirements.txt


Set up environment variables:
Create a .env file with your Gemini API key:

GEMINI_API_KEY=your_google_gemini_api_key


🧪 Running the App
  streamlit run app.py
  Then open the URL provided (typically http://localhost:8501/) in your browser.

📥 How to Use
  Enter an optional health topic or description.
  
  Upload a PDF patient health document.
  
  Enter your Gemini API key in the sidebar.
  
  Click Summarize Document.
  
  View summaries tailored for:
  
    Medical Professionals: Technical diagnosis, clinical findings, and treatments.
    
    Patients: Simple explanation and recommended steps.

🔒 Security
  Your API key is not stored and is only used during your session.

🧾 Example Output
For Medical Professionals:
- Diagnosis: Type 2 Diabetes Mellitus
- Treatment: Metformin, lifestyle changes
- Notes: Follow-up required in 3 months

For Patients:
- You have been diagnosed with type 2 diabetes.
- Your doctor recommends medication and dietary changes.
- Schedule a follow-up visit in 3 months.
