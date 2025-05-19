# Automated Interview Question Generator

A Streamlit-based web application that generates interview questions based on job descriptions using NLP and AI.

## Features

- Extract skills and tools from job descriptions using spaCy and NLTK
- Generate both technical and behavioral interview questions
- Support for different difficulty levels
- Optional GPT-powered question generation
- Export questions to TXT or CSV format
- Modern and user-friendly interface

## Setup

1. Clone the repository:
```bash
git clone <repository-url>
cd automated-interview-question-generator
```

2. Create a virtual environment and activate it:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install the required packages:
```bash
pip install -r requirements.txt
```

4. Download the spaCy model:
```bash
python -m spacy download en_core_web_sm
```

5. (Optional) Set up OpenAI API key:
Create a `.env` file in the project root and add your OpenAI API key:
```
OPENAI_API_KEY=your_api_key_here
```

## Usage

1. Start the Streamlit app:
```bash
streamlit run app.py
```

2. Open your web browser and navigate to the URL shown in the terminal (usually http://localhost:8501)

3. Paste a job description in the text area

4. Select your preferences:
   - Question Type (Technical/Behavioral/Both)
   - Difficulty Level (Easy/Medium/Hard)
   - Whether to use GPT for question generation

5. Click "Generate Questions" to get your customized interview questions

6. Export the questions in your preferred format (TXT or CSV)

## Project Structure

- `app.py`: Main Streamlit application
- `extractor.py`: NLP processing and skill extraction
- `generator.py`: Question generation logic
- `config.py`: Configuration settings and templates
- `requirements.txt`: Project dependencies

## Dependencies

- streamlit
- spacy
- nltk
- pandas
- openai
- python-dotenv

## Contributing

Feel free to submit issues and enhancement requests! 