import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# OpenAI API Configuration
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

# Question Templates
TECHNICAL_TEMPLATES = [
    "Can you describe your experience with {skill}?",
    "How have you used {tool} in past projects?",
    "What challenges have you faced while working with {skill}?",
    "How do you stay updated with the latest developments in {skill}?",
    "Can you explain a complex {skill} concept to a non-technical person?"
]

BEHAVIORAL_TEMPLATES = [
    "Tell me about a time you applied {skill} in a challenging situation.",
    "How do you handle conflicts when working with {tool}?",
    "Describe a situation where you had to learn {skill} quickly.",
    "How do you ensure quality when working with {tool}?",
    "Tell me about a project where you successfully implemented {skill}."
]

# Difficulty modifiers
DIFFICULTY_MODIFIERS = {
    'Easy': "basic",
    'Medium': "intermediate",
    'Hard': "advanced"
}

# GPT Prompt Template
GPT_PROMPT_TEMPLATE = """
Based on the following job description, generate {num_questions} {difficulty} level {question_type} interview questions.
Focus on the following skills and tools: {skills}

Job Description:
{job_description}

Generate questions that are specific, relevant, and challenging.
"""

# File export settings
EXPORT_OPTIONS = {
    'txt': {
        'extension': '.txt',
        'delimiter': '\n\n'
    },
    'csv': {
        'extension': '.csv',
        'delimiter': ','
    }
} 