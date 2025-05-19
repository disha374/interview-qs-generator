import streamlit as st
import pandas as pd
from extractor import SkillExtractor
from generator import QuestionGenerator
from config import EXPORT_OPTIONS

# Set page config
st.set_page_config(
    page_title="Automated Interview Question Generator",
    page_icon="💼",
    layout="wide"
)

def main():
    st.title("💼 Automated Interview Question Generator")
    st.markdown("""
    This tool helps you generate relevant interview questions based on job descriptions.
    Simply paste a job description, select your preferences, and get tailored questions!
    """)
    
    # Create sidebar for options
    st.sidebar.header("Options")
    num_questions = st.sidebar.slider("Number of Questions", 1, 10, 5)
    difficulty = st.sidebar.selectbox("Difficulty Level", ["Easy", "Medium", "Hard"])
    question_type = st.sidebar.selectbox("Question Type", ["Technical", "Behavioral", "Both"])
    use_gpt = st.sidebar.checkbox("Use GPT (requires API key)", value=False)
    
    # Main content area
    job_description = st.text_area("Paste Job Description Here", height=200)
    
    if st.button("Generate Questions"):
        if job_description:
            try:
                # Initialize extractors
                skill_extractor = SkillExtractor()
                question_generator = QuestionGenerator()
                
                # Extract skills
                skills = skill_extractor.process_job_description(job_description)
                
                # Display extracted skills
                st.subheader("Extracted Skills")
                col1, col2 = st.columns(2)
                
                with col1:
                    st.write("Technical Skills:")
                    for skill in skills['technical']:
                        st.write(f"- {skill}")
                
                with col2:
                    st.write("Behavioral Skills:")
                    for skill in skills['behavioral']:
                        st.write(f"- {skill}")
                
                # Generate questions
                st.subheader("Generated Questions")
                questions = question_generator.generate_questions(
                    job_description=job_description,
                    skills=skills,
                    question_type=question_type,
                    difficulty=difficulty,
                    use_gpt=use_gpt
                )
                
                for i, question in enumerate(questions, 1):
                    st.write(f"{i}. {question}")
                    
            except Exception as e:
                st.error(f"An error occurred: {str(e)}")
        else:
            st.warning("Please enter a job description first!")

if __name__ == "__main__":
    main() 