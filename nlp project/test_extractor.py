from extractor import SkillExtractor

def main():
    # Create an instance of SkillExtractor
    extractor = SkillExtractor()
    
    # Sample job description
    job_description = """
    We are looking for a Python Developer with experience in Django and Flask frameworks.
    The ideal candidate should have strong knowledge of databases like MySQL and MongoDB.
    Experience with Git, Docker, and AWS is required.
    The candidate should have excellent communication skills and be a team player.
    Knowledge of agile methodologies and CI/CD practices is a plus.
    """
    
    # Process the job description
    skills = extractor.process_job_description(job_description)
    
    # Print the results
    print("\nExtracted Skills:")
    print("\nTechnical Skills:")
    for skill in skills['technical']:
        print(f"- {skill}")
    
    print("\nBehavioral Skills:")
    for skill in skills['behavioral']:
        print(f"- {skill}")

if __name__ == "__main__":
    main() 