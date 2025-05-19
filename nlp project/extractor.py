import spacy
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import re

# Download required NLTK data
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

class SkillExtractor:
    def __init__(self):
        # Load spaCy model
        self.nlp = spacy.load("en_core_web_sm")
        self.lemmatizer = WordNetLemmatizer()
        self.stop_words = set(stopwords.words('english'))
        
        # Common technical terms and skills
        self.technical_terms = {
            'programming': ['python', 'java', 'javascript', 'c++', 'ruby', 'php'],
            'frameworks': ['django', 'flask', 'react', 'angular', 'vue', 'spring'],
            'databases': ['mysql', 'postgresql', 'mongodb', 'redis', 'oracle'],
            'tools': ['git', 'docker', 'kubernetes', 'jenkins', 'aws', 'azure'],
            'methodologies': ['agile', 'scrum', 'waterfall', 'devops', 'ci/cd']
        }

    def clean_text(self, text):
        """Clean and preprocess the input text."""
        # Convert to lowercase
        text = text.lower()
        
        # Remove special characters and digits
        text = re.sub(r'[^a-zA-Z\s]', ' ', text)
        
        # Remove extra whitespace
        text = ' '.join(text.split())
        
        return text

    def extract_entities(self, text):
        """Extract named entities using spaCy."""
        doc = self.nlp(text)
        entities = []
        
        for ent in doc.ents:
            if ent.label_ in ['ORG', 'PRODUCT', 'WORK_OF_ART']:
                entities.append(ent.text.lower())
        
        return entities

    def extract_skills(self, text):
        """Extract skills and tools from the text."""
        cleaned_text = self.clean_text(text)
        tokens = word_tokenize(cleaned_text)
        
        # Remove stopwords and lemmatize
        tokens = [self.lemmatizer.lemmatize(token) for token in tokens 
                 if token not in self.stop_words]
        
        # Extract technical terms
        skills = set()
        for category, terms in self.technical_terms.items():
            for term in terms:
                if term in cleaned_text:
                    skills.add(term)
        
        # Add named entities
        entities = self.extract_entities(text)
        skills.update(entities)
        
        return list(skills)

    def categorize_skills(self, skills):
        """Categorize skills into technical and behavioral."""
        technical_skills = []
        behavioral_skills = []
        
        # Common behavioral skills
        behavioral_keywords = {
            'communication', 'leadership', 'teamwork', 'problem-solving',
            'time management', 'adaptability', 'creativity', 'critical thinking'
        }
        
        for skill in skills:
            if skill in behavioral_keywords:
                behavioral_skills.append(skill)
            else:
                technical_skills.append(skill)
        
        return {
            'technical': technical_skills,
            'behavioral': behavioral_skills
        }

    def process_job_description(self, job_description):
        """Process job description and return categorized skills."""
        if not job_description:
            return {'technical': [], 'behavioral': []}
        
        skills = self.extract_skills(job_description)
        return self.categorize_skills(skills) 