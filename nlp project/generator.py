import random
import openai
from config import (
    TECHNICAL_TEMPLATES,
    BEHAVIORAL_TEMPLATES,
    DIFFICULTY_MODIFIERS,
    GPT_PROMPT_TEMPLATE,
    OPENAI_API_KEY
)

class QuestionGenerator:
    def __init__(self):
        self.openai_client = openai.OpenAI(api_key=OPENAI_API_KEY) if OPENAI_API_KEY else None

    def generate_template_questions(self, skills, question_type, difficulty):
        """Generate questions using predefined templates."""
        questions = []
        templates = TECHNICAL_TEMPLATES if question_type == 'Technical' else BEHAVIORAL_TEMPLATES
        
        if question_type == 'Both':
            templates = TECHNICAL_TEMPLATES + BEHAVIORAL_TEMPLATES
        
        # Select skills based on question type
        relevant_skills = skills['technical'] if question_type == 'Technical' else skills['behavioral']
        if question_type == 'Both':
            relevant_skills = skills['technical'] + skills['behavioral']
        
        if not relevant_skills:
            return ["No relevant skills found for the selected question type."]
        
        # Generate questions using templates
        for _ in range(min(9, len(relevant_skills))):
            skill = random.choice(relevant_skills)
            template = random.choice(templates)
            question = template.format(skill=skill, tool=skill)
            questions.append(question)
        
        return questions

    def generate_gpt_questions(self, job_description, skills, question_type, difficulty):
        """Generate questions using GPT if API key is available."""
        if not self.openai_client:
            return None
        
        try:
            # Prepare the prompt
            skills_str = ', '.join(skills['technical'] + skills['behavioral'])
            prompt = GPT_PROMPT_TEMPLATE.format(
                num_questions=9,
                difficulty=DIFFICULTY_MODIFIERS[difficulty],
                question_type=question_type.lower(),
                skills=skills_str,
                job_description=job_description
            )
            
            # Generate questions using GPT
            response = self.openai_client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are an expert interviewer who generates relevant and challenging interview questions."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.7,
                max_tokens=500
            )
            
            # Extract and format questions
            questions = response.choices[0].message.content.split('\n')
            questions = [q.strip() for q in questions if q.strip()]
            
            return questions[:9]  # Return top 9 questions
            
        except Exception as e:
            print(f"Error generating GPT questions: {str(e)}")
            return None

    def generate_questions(self, job_description, skills, question_type, difficulty, use_gpt=True):
        """Generate questions using either templates or GPT."""
        if use_gpt and self.openai_client:
            gpt_questions = self.generate_gpt_questions(
                job_description, skills, question_type, difficulty
            )
            if gpt_questions:
                return gpt_questions
        
        # Fallback to template-based questions
        return self.generate_template_questions(skills, question_type, difficulty) 