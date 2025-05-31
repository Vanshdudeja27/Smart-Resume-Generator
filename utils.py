import requests
from job_scraper import scrape_jobs  # Ensure this file exists
# No need to re-import query_ollama; it's part of this file

def query_ollama(prompt, model="gemma:2b"):
    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": model,
                "prompt": prompt,
                "stream": False
            }
        )
        data = response.json()
        return data.get("response", "❌ No response from Ollama.")
    except Exception as e:
        return f"❌ Error: {str(e)}"

def generate_resume(user_bio):
    prompt = f"Create a clean, ATS-friendly resume using the following details:\n{user_bio}"
    return query_ollama(prompt)

def generate_cover_letter(user_bio, job_desc):
    prompt = f"Write a personalized cover letter for this job based on:\nUser Info: {user_bio}\nJob Description: {job_desc}"
    return query_ollama(prompt)

def analyze_skills(user_skills, job_desc):
    prompt = f"Compare the user's skills: {user_skills} with the job description:\n{job_desc}\nHighlight missing or weak areas."
    return query_ollama(prompt)

def generate_interview_questions(job_desc):
    prompt = f"Generate 5 mock interview questions for this job:\n{job_desc}"
    return query_ollama(prompt)

def match_jobs_with_resume(resume_text, keyword="Data Scientist"):
    jobs = scrape_jobs(keyword)
    matches = []

    for job in jobs:
        prompt = f"""
Compare the following RESUME with this JOB DESCRIPTION.

RESUME:
{resume_text}

JOB:
Title: {job['title']}
Company: {job['company']}
Description: {job['description']}

Is this a good match? Reply Yes or No with a reason.
"""
        response = query_ollama(prompt)
        if "Yes" in response[:10]:
            matches.append({
                "title": job["title"],
                "company": job["company"],
                "reason": response.strip(),
                "link": job["apply_link"]
            })

    return matches
