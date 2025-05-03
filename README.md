# AI-Powered Resume Screening Application

This project is a web-based tool that helps users evaluate how well their resume matches a given job description. It uses natural language processing (NLP) techniques to extract useful insights and provide suggestions for improvement.

## What this app does

Once you enter a job description and upload your resume (in PDF format), the app gives you the following feedback:

1. **Tell me about the resume**  
   Summarizes what skills and experience your resume highlights.

2. **How can I improve my skills?**  
   Suggests areas you could work on to better match the job description.

3. **What keywords are missing?**  
   Identifies important keywords from the job description that are not found in your resume.

4. **Percentage match**  
   Calculates how closely your resume matches the job description using text similarity.

## Technologies used

- Python  
- Streamlit (for the user interface)  
- scikit-learn (for TF-IDF and cosine similarity)  
- NLTK (for text preprocessing)  
- PyPDF2 (to extract text from PDF resumes)
