skills_data = {
    "Data Scientist": ["python", "machine learning", "sql", "data analysis"],
    "Backend Developer": ["java", "python", "sql", "api"],
    "DevOps Engineer": ["aws", "docker", "kubernetes", "linux"],
    "Cloud Engineer": ["aws", "cloud", "linux", "networking"],
    "AI Engineer": ["python", "machine learning", "deep learning", "ai"]
}

print("=== Tech Stack Recommender ===")

user_skills = input("Enter your skills (comma separated): ").lower().split(",")

user_skills = [skill.strip() for skill in user_skills]

scores = {}

for role, skills in skills_data.items():
    match = len(set(user_skills) & set(skills))
    scores[role] = match

recommended = sorted(scores.items(), key=lambda x: x[1], reverse=True)

print("\nTop Recommendations:")

for role, score in recommended[:3]:
    print(role, "-> Match Score:", score)