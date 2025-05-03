import streamlit as st
import fitz  # PyMuPDF for PDF reading
import re
import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
nltk.download('punkt')
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Function to extract text from PDF
def extract_text_from_pdf(file):
    text = ""
    doc = fitz.open(stream=file.read(), filetype="pdf")
    for page in doc:
        text += page.get_text()
    return text

# Function to clean and tokenize text
def preprocess(text):
    text = text.lower()
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text)
    tokens = word_tokenize(text)
    tokens = [word for word in tokens if word not in stopwords.words('english')]
    return ' '.join(tokens)

# Function to compare JD and resume text
def compare_texts(jd_text, resume_text):
    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform([jd_text, resume_text])
    similarity = cosine_similarity(vectors[0:1], vectors[1:2])[0][0]
    return similarity * 100, vectorizer.get_feature_names_out(), vectors

# Extract keywords
def extract_keywords(text):
    words = word_tokenize(preprocess(text))
    return set(words)

# Streamlit UI
st.title("AI Powered Resume Screening")

job_desc = st.text_area("Enter Job Description")
resume_file = st.file_uploader("Upload Resume (PDF only)", type=["pdf"])

if job_desc and resume_file:
    resume_text = extract_text_from_pdf(resume_file)
    clean_jd = preprocess(job_desc)
    clean_resume = preprocess(resume_text)

    match_percent, feature_names, vectors = compare_texts(clean_jd, clean_resume)

    if st.button("Tell me about the resume"):
        st.subheader("Resume Summary")
        st.write(resume_text[:1000] + ("..." if len(resume_text) > 1000 else ""))

    if st.button("How can I improve my skills"):
        jd_keywords = extract_keywords(job_desc)
        resume_keywords = extract_keywords(resume_text)
        missing_keywords = jd_keywords - resume_keywords
        st.subheader("Suggested Skills to Improve")
        st.write(", ".join(missing_keywords) if missing_keywords else "No missing skills detected!")

    if st.button("What are the keywords that are missing"):
        jd_keywords = extract_keywords(job_desc)
        resume_keywords = extract_keywords(resume_text)
        missing_keywords = jd_keywords - resume_keywords
        st.subheader("Missing Keywords")
        st.write(", ".join(missing_keywords) if missing_keywords else "Your resume covers all the keywords!")

    if st.button("Percentage match"):
        st.subheader("Match Percentage")
        st.write(f"Your resume matches the job description by {match_percent:.2f}%")
